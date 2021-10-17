from celery import Celery
import ai_model
import chess
import os
import ssl
REDIS_URL=os.getenv("REDIS_URL") + "?ssl_cert_reqs=none"
celery_app = None
try:
	celery_app=Celery('tasks',backend=REDIS_URL,broker=REDIS_URL)
except:
	print("/n/n/n/n/n url is ",REDIS_URL)
celery_app.conf.update(broker_pool_limit=None,broker_url=REDIS_URL,result_backend=REDIS_URL)
@celery_app.task
def generate_machine_move(fen):
    board=chess.Board()
    board.set_fen(fen)
    machine_move=ai_model.predict(board)
    board.push(machine_move)
    return board.fen()
