from flask import Flask
from flask import render_template,request,jsonify
from tasks import celery_app,generate_machine_move
from celery.result import AsyncResult

app = Flask(__name__)
#DO NOT MODIFY!!!
START_FEN ='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#starting board
@app.route('/')
def start():
    global START_FEN
    return render_template("index.html",fen_var=START_FEN)

#make a move, spawn a task generating the machine's move
@app.route('/move',methods=['GET','POST'])
def move():
    global START_FEN
    if request.method == "GET":
        return render_template("index.html",fen_var=START_FEN)
    
    if request.method == "POST":
        jsdata = request.form['fen_string']
        result = generate_machine_move.delay(jsdata)
        return jsonify({'task_id':result.id}) 

#get the machine's move from the task result, if the task has finished executing.
@app.route("/move_response/<task_id>")
def move_response(task_id):
    result=generate_machine_move.AsyncResult(task_id)
    machine_fen=""
    if result.ready():
        machine_fen=result.get()    
    return jsonify({'newBoard':render_template("index.html",fen_var=machine_fen),'ready':result.ready()})
         

if __name__ == '__main__':
    app.run() 
