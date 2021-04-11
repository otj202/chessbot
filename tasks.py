from celery import Celery
import ai_model
import chess
celery_app=Celery('tasks',backend='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-35-169-115-180.compute-1.amazonaws.com:9969',broker='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-35-169-115-180.compute-1.amazonaws.com:9969')

@celery_app.task
def generate_machine_move(fen):
    board=chess.Board()
    board.set_fen(fen)
    machine_move=ai_model.predict(board)
    board.push(machine_move)
    return board.fen()