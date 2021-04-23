from celery import Celery
import ai_model
import chess
import os
celery_app=Celery('tasks',backend='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-34-197-240-190.compute-1.amazonaws.com:14819',broker='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-34-197-240-190.compute-1.amazonaws.com:14819')
celery_app.conf.update(broker_pool_limit=None,broker_url='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-34-197-240-190.compute-1.amazonaws.com:14819',result_backend='redis://:p1cfadf555e1f6b0a0fcd1f54f8554aebe4ce57b086bf86bb05eb15d343ceebd0@ec2-34-197-240-190.compute-1.amazonaws.com:14819')
@celery_app.task
def generate_machine_move(fen):
	for i in range(10):
		print("generate machine move",i)
	return "bar"
	#board=chess.Board()
    #board.set_fen(fen)
    #machine_move=ai_model.predict(board)
    #board.push(machine_move)
    #return board.fen()
