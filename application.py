from flask import Flask
from flask import render_template,request,jsonify
from tasks import celery_app,generate_machine_move
from celery.result import AsyncResult
import chess
import ai_model

app = Flask(__name__)

@app.route('/')
def start():
    start_fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    return render_template("index.html",fen_var=start_fen)

#TODO in javascript, change on success to poll /move_response/<task_id>
@app.route('/move',methods=['GET','POST'])
def move():
    start_fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    if request.method == "GET":
        return render_template("index.html",fen_var=start_fen)
    
    if request.method == "POST":
        jsdata = request.form['fen_string']
        result = generate_machine_move.delay(jsdata)
        print("created this task:",result.id)
        return jsonify({'task_id':result.id}) 

#in javascript, stop polling when len(machine_fen) > 0
@app.route("/move_response/<task_id>")
def move_response(task_id):
    print("polling this task:",task_id) 
    result=generate_machine_move.AsyncResult(task_id)
    machine_fen=""
    print("result.ready() is ",result.ready())
    if result.ready():
        machine_fen=result.get()
    print("machine_fen is ",machine_fen, "of type", type(machine_fen))
    
    return jsonify({'newBoard':render_template("index.html",fen_var=machine_fen),'ready':result.ready()})
         

if __name__ == '__main__':
    app.run() 
