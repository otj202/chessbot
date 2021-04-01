from flask import Flask
from flask import render_template,request,jsonify
import chess
app = Flask(__name__)
import ai_model

@app.route('/')
def start():
    start_fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    return render_template("index.html",fen_var=start_fen)

@app.route('/move',methods=['GET','POST'])
def move():

    start_fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    if request.method == "GET":
        return render_template("index.html",fen_var=start_fen)
    
    if request.method == "POST":
    
        jsdata = request.form['fen_string']
        board=chess.Board()        
        board.set_fen(jsdata)
        print(board)
        machine_move=ai_model.predict(board)
        print("machine has chosen ",machine_move)
        board.push(machine_move)
        machine_fen=board.fen()
        return jsonify({'fen_response':render_template("index.html",fen_var=machine_fen)}) 


if __name__ == '__main__':
    app.run() 
