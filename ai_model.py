import chess
import random

#---------------------- PeSTO TABLES -----------------------------#
mg_value = [82, 337, 365, 477, 1025,  0]
eg_value = [94, 281, 297, 512,  936,  0]

mg_pawn_table=[
      0,   0,   0,   0,   0,   0,  0,   0,
     98, 134,  61,  95,  68, 126, 34, -11,
     -6,   7,  26,  31,  65,  56, 25, -20,
    -14,  13,   6,  21,  23,  12, 17, -23,
    -27,  -2,  -5,  12,  17,   6, 10, -25,
    -26,  -4,  -4, -10,   3,   3, 33, -12,
    -35,  -1, -20, -23, -15,  24, 38, -22,
      0,   0,   0,   0,   0,   0,  0,   0]


eg_pawn_table=[
      0,   0,   0,   0,   0,   0,   0,   0,
    178, 173, 158, 134, 147, 132, 165, 187,
     94, 100,  85,  67,  56,  53,  82,  84,
     32,  24,  13,   5,  -2,   4,  17,  17,
     13,   9,  -3,  -7,  -7,  -8,   3,  -1,
      4,   7,  -6,   1,   0,  -5,  -1,  -8,
     13,   8,   8,  10,  13,   0,   2,  -7,
      0,   0,   0,   0,   0,   0,   0,   0]
mg_knight_table=[
    -167, -89, -34, -49,  61, -97, -15, -107,
     -73, -41,  72,  36,  23,  62,   7,  -17,
     -47,  60,  37,  65,  84, 129,  73,   44,
      -9,  17,  19,  53,  37,  69,  18,   22,
     -13,   4,  16,  13,  28,  19,  21,   -8,
     -23,  -9,  12,  10,  19,  17,  25,  -16,
     -29, -53, -12,  -3,  -1,  18, -14,  -19,
    -105, -21, -58, -33, -17, -28, -19,  -23]

eg_knight_table=[
    -58, -38, -13, -28, -31, -27, -63, -99,
    -25,  -8, -25,  -2,  -9, -25, -24, -52,
    -24, -20,  10,   9,  -1,  -9, -19, -41,
    -17,   3,  22,  22,  22,  11,   8, -18,
    -18,  -6,  16,  25,  16,  17,   4, -18,
    -23,  -3,  -1,  15,  10,  -3, -20, -22,
    -42, -20, -10,  -5,  -2, -20, -23, -44,
    -29, -51, -23, -15, -22, -18, -50, -64]

mg_bishop_table=[
    -29,   4, -82, -37, -25, -42,   7,  -8,
    -26,  16, -18, -13,  30,  59,  18, -47,
    -16,  37,  43,  40,  35,  50,  37,  -2,
     -4,   5,  19,  50,  37,  37,   7,  -2,
     -6,  13,  13,  26,  34,  12,  10,   4,
      0,  15,  15,  15,  14,  27,  18,  10,
      4,  15,  16,   0,   7,  21,  33,   1,
    -33,  -3, -14, -21, -13, -12, -39, -21]

eg_bishop_table=[
    -14, -21, -11,  -8, -7,  -9, -17, -24,
     -8,  -4,   7, -12, -3, -13,  -4, -14,
      2,  -8,   0,  -1, -2,   6,   0,   4,
     -3,   9,  12,   9, 14,  10,   3,   2,
     -6,   3,  13,  19,  7,  10,  -3,  -9,
    -12,  -3,   8,  10, 13,   3,  -7, -15,
    -14, -18,  -7,  -1,  4,  -9, -15, -27,
    -23,  -9, -23,  -5, -9, -16,  -5, -17]

mg_rook_table=[
     32,  42,  32,  51, 63,  9,  31,  43,
     27,  32,  58,  62, 80, 67,  26,  44,
     -5,  19,  26,  36, 17, 45,  61,  16,
    -24, -11,   7,  26, 24, 35,  -8, -20,
    -36, -26, -12,  -1,  9, -7,   6, -23,
    -45, -25, -16, -17,  3,  0,  -5, -33,
    -44, -16, -20,  -9, -1, 11,  -6, -71,
    -19, -13,   1,  17, 16,  7, -37, -26]

eg_rook_table=[
    13, 10, 18, 15, 12,  12,   8,   5,
    11, 13, 13, 11, -3,   3,   8,   3,
     7,  7,  7,  5,  4,  -3,  -5,  -3,
     4,  3, 13,  1,  2,   1,  -1,   2,
     3,  5,  8,  4, -5,  -6,  -8, -11,
    -4,  0, -5, -1, -7, -12,  -8, -16,
    -6, -6,  0,  2, -9,  -9, -11,  -3,
    -9,  2,  3, -1, -5, -13,   4, -20]

mg_queen_table=[
    -28,   0,  29,  12,  59,  44,  43,  45,
    -24, -39,  -5,   1, -16,  57,  28,  54,
    -13, -17,   7,   8,  29,  56,  47,  57,
    -27, -27, -16, -16,  -1,  17,  -2,   1,
     -9, -26,  -9, -10,  -2,  -4,   3,  -3,
    -14,   2, -11,  -2,  -5,   2,  14,   5,
    -35,  -8,  11,   2,   8,  15,  -3,   1,
     -1, -18,  -9,  10, -15, -25, -31, -50]

eg_queen_table=[
     -9,  22,  22,  27,  27,  19,  10,  20,
    -17,  20,  32,  41,  58,  25,  30,   0,
    -20,   6,   9,  49,  47,  35,  19,   9,
      3,  22,  24,  45,  57,  40,  57,  36,
    -18,  28,  19,  47,  31,  34,  39,  23,
    -16, -27,  15,   6,   9,  17,  10,   5,
    -22, -23, -30, -16, -16, -23, -36, -32,
    -33, -28, -22, -43,  -5, -32, -20, -41]

mg_king_table=[
    -65,  23,  16, -15, -56, -34,   2,  13,
     29,  -1, -20,  -7,  -8,  -4, -38, -29,
     -9,  24,   2, -16, -20,   6,  22, -22,
    -17, -20, -12, -27, -30, -25, -14, -36,
    -49,  -1, -27, -39, -46, -44, -33, -51,
    -14, -14, -22, -46, -44, -30, -15, -27,
      1,   7,  -8, -64, -43, -16,   9,   8,
    -15,  36,  12, -54,   8, -28,  24,  14]

eg_king_table=[
    -74, -35, -18, -18, -11,  15,   4, -17,
    -12,  17,  14,  17,  17,  38,  23,  11,
     10,  17,  23,  15,  20,  45,  44,  13,
     -8,  22,  24,  27,  26,  33,  26,   3,
    -18,  -4,  21,  24,  27,  23,   9, -11,
    -19,  -3,  11,  21,  23,  16,   7,  -9,
    -27, -11,   4,  13,  14,   4,  -5, -17,
    -53, -34, -21, -11, -28, -14, -24, -43]

mg_pesto_table=[
    mg_pawn_table,
    mg_knight_table,
    mg_bishop_table,
    mg_rook_table,
    mg_queen_table,
    mg_king_table]

eg_pesto_table=[
    eg_pawn_table,
    eg_knight_table,
    eg_bishop_table,
    eg_rook_table,
    eg_queen_table,
    eg_king_table]

gamephaseInc=[0,0,1,1,1,1,2,2,4,4,0,0]

mg_table=[[0 for _ in range(64)] for _ in range(12)]
eg_table=[[0 for _ in range(64)] for _ in range(12)]
def init_tables():
    for p in range(6):
        pc=2*p
        for sq in range(64):
            mg_table[pc][sq] = mg_value[p] + mg_pesto_table[p][square2index(sq)]
            mg_table[pc+1][sq] = mg_value[p] + mg_pesto_table[p][sq]
            eg_table[pc][sq] = eg_value[p] + eg_pesto_table[p][square2index(sq)]
            eg_table[pc+1][sq] = eg_value[p] + eg_pesto_table[p][sq]

def piece2index(piece):
    return 2*(piece.piece_type - 1) + 1 - piece.color
def square2index(square):
    return 8*(7 - (square // 8)) + square % 8

#PeSTO evaluation function
def f(MACHINE_COLOR,board):
    if board.is_checkmate():
        return -901 if MACHINE_COLOR == board.turn else 901
    WHITE=0
    BLACK=1
    mg=[0,0]
    eg=[0,0]
    gamePhase=0
    for square in chess.SQUARES:
        pc=board.piece_at(square)
        if pc is not None:
            mg[pc.color]+=mg_table[piece2index(pc)][square]  
            eg[pc.color]+=eg_table[piece2index(pc)][square]
            gamePhase += gamephaseInc[piece2index(pc)]
    mgScore=mg[board.turn] - mg[1-board.turn]    
    egScore=eg[board.turn] - mg[1-board.turn]
    mgPhase=gamePhase
    if mgPhase > 24:
        mgPhase = 24
    egPhase = 24 - mgPhase
    mul=1 if MACHINE_COLOR == board.turn else -1
    return mul * (mgScore * mgPhase + egScore * egPhase)/24


  
piece_vals = {chess.PAWN:1,chess.KNIGHT:3,chess.BISHOP:3,chess.ROOK:5,chess.QUEEN:9,chess.KING:200}

#PIECE MATRICES. 
#can be improved by using PeSTO, recognizing when it's the early game, when the middle, when the endgame.
piece_matrices = {
 chess.KING: 
 [[-3,-4,-4,-5,-5,-4,-4,-3],
  [-3,-4,-4,-5,-5,-4,-4,-3],
  [-3,-4,-4,-5,-5,-4,-4,-3],
  [-3,-4,-4,-5,-5,-4,-4,-3],
  [-2,-3,-3,-4,-4,-3,-3,-2],
  [-1,-2,-2,-2,-2,-2,-2,-1],
  [2,2,0,0,0,0,2,2],
  [2,3,1,0,0,1,3,2]],
 chess.QUEEN:
 [[-2,-1,-1,-0.5,-0.5,-1,-1,-2],
  [-1,0,0,0,0,0,0,-1],
  [-1,0,0.5,0.5,0.5,0.5,0,-1],
  [-0.5,0,0.5,0.5,0.5,0.5,0,-0.5],
  [0,0,0.5,0.5,0.5,0.5,0,-0.5],
  [-1,0.5,0.5,0.5,0.5,0.5,0,-1],
  [-1,0,0.5,0,0,0,0,-1],
  [-2,-1,-1,-0.5,-0.5,-1,-1,-2]],
 chess.ROOK:
 [[0,0,0,0,0,0,0,0],
  [0.5,1,1,1,1,1,1,0.5],
  [-0.5,0,0,0,0,0,0,-0.5],
  [-0.5,0,0,0,0,0,0,-0.5],
  [-0.5,0,0,0,0,0,0,-0.5],
  [-0.5,0,0,0,0,0,0,-0.5],
  [-0.5,0,0,0,0,0,0,-0.5],
  [0,0,0,0.5,0.5,0,0,0]],
 chess.BISHOP:
 [[-2,-1,-1,-1,-1,-1,-1,-2],
  [-1,0,0,0,0,0,0,-1],
  [-1,0,0.5,1,1,0.5,0,-1],
  [-1,0.5,0.5,1,1,0.5,0.5,-1],
  [-1,0,1,1,1,1,0,-1],
  [-1,1,1,1,1,1,1,-1],
  [-1,0.5,0,0,0,0,0.5,-1],
  [-2,-1,-1,-1,-1,-1,-1,-2]],
 chess.KNIGHT:
 [[-5,-4,-3,-3,-3,-3,-4,-5],
  [-4,-2,0,0,0,0,-2,-4],
  [-3,0,1,1.5,1.5,1,0,-3],
  [-3,0.5,1.5,2,2,1.5,0.5,-3],
  [-3,0,1.5,2,2,1.5,0,-3],
  [-3,0.5,1,1.5,1.5,1,0.5,-3],
  [-4,-2,0,0.5,0.5,0,-2,-4],
  [-5,-4,-3,-3,-3,-3,-4,-5]],
 chess.PAWN:
 [[0,0,0,0,0,0,0,0],
  [5,5,5,5,5,5,5,5],
  [1,1,2,3,3,2,1,1],
  [0.5,0.5,1,2.5,2.5,1,0.5,0.5],
  [0,0,0,2,2,0,0,0],
  [0.5,-0.5,-1,0,0,-1,-0.5,0.5],
  [0.5,1,1,-2,-2,1,1,0.5],
  [0,0,0,0,0,0,0,0]]
}

#TODO: implement this
def _square2index(pc,square):
    mult = 1 if pc.color == chess.WHITE else -1
    squareStr = chess.square_name(square)
    y = ord(squareStr[0]) - ord('a')
    x = int(squareStr[1]) - 1 if pc.color == chess.BLACK else  -int(squareStr[1])
    return x,y

def g(MACHINE_COLOR,board):
    if board.is_checkmate():
        return -900 if MACHINE_COLOR == board.turn else 900
    tot = 0
    #count material, add piece matrix value.
    for square in chess.SQUARES:
        pc = board.piece_at(square)
        if pc is not None:
            mult = 1 if pc.color == MACHINE_COLOR else -1
            x,y = _square2index(pc,square)  
            tot += mult * (piece_vals[pc.piece_type] + 0.05 * piece_matrices[pc.piece_type][x][y])
   #mobility                 
    orig=board.turn
    board.turn=MACHINE_COLOR
    tot +=  0.05 * board.legal_moves.count()
    board.turn=chess.WHITE if MACHINE_COLOR == chess.BLACK else chess.BLACK
    tot -= 0.05 *  board.legal_moves.count()
    board.turn=orig
     
    #move pieces off the back rank    
    square_mul=1 if MACHINE_COLOR == chess.WHITE else -1
    for square in chess.SquareSet.ray(chess.A1,chess.H1):
        if board.piece_at(square) is None:
            tot += square_mul * .022
    for square in chess.SquareSet.ray(chess.A8,chess.H8):
        if board.piece_at(square) is None:  
            tot -= square_mul * .022
    return tot
def f_prime(MACHINE_COLOR,board):
    if board.is_checkmate():
        return -900 if MACHINE_COLOR == board.turn else 900
    tot = 0
    for square in chess.SQUARES:
        pc = board.piece_at(square)
        if pc is not None:
            mult = 1 if pc.color == MACHINE_COLOR else -1
            x,y = _square2index(pc,square)  
            tot += mult * (piece_vals[pc.piece_type] + 0.1 * piece_matrices[pc.piece_type][x][y])
            
    orig=board.turn
    board.turn=MACHINE_COLOR
    tot +=  0.1 * board.legal_moves.count()
    board.turn=chess.WHITE if MACHINE_COLOR == chess.BLACK else chess.BLACK
    tot -= 0.1 *  board.legal_moves.count()
    board.turn=orig
    return tot



def old_stateless_find_max_move(MACHINE_COLOR,board,alpha,beta,depth):
    if depth == 0:
        return None,f(MACHINE_COLOR,board)
    mvs=board.legal_moves
    if board.turn == MACHINE_COLOR:         
        mx = -901
        mxMove=None
        for mv in mvs:
            board.push(mv)
            succMove,succMx = old_stateless_find_max_move(MACHINE_COLOR,board,max(mx,alpha),beta,depth-1)
            board.pop()
            if succMx is None:
                continue
            if succMx >= beta:
                return None,None
            if succMx > mx:
                mx = succMx
                mxMove = mv
        return mxMove,mx
    else:
        mn = 901
        mnMove = None
        for mv in mvs:
            board.push(mv)
            succMove,succMn = old_stateless_find_max_move(MACHINE_COLOR,board,alpha,min(mn,beta),depth-1)
            board.pop()
            if succMn is None:
                continue
            if succMn <= alpha: 
                return None,None
            if succMn < mn:
                mn = succMn
                mnMove = mv
        return mnMove,mn
def stateless_find_max_move(MACHINE_COLOR,board,alpha,beta,depth):
    if depth == 0:
        coolBd,val=quiesce(MACHINE_COLOR,board,alpha,beta,3)
        if coolBd is None:
            return None,None,None
        return coolBd.copy(),None,val 
    mvs=board.legal_moves
    if board.turn == MACHINE_COLOR:         
        mx = -9001
        mxMove=None
        mxCoolBd=None
        for mv in mvs:
            board.push(mv)
            coolBd,succMove,succMx = stateless_find_max_move(MACHINE_COLOR,board,max(mx,alpha),beta,depth-1)
            board.pop()
            if succMx is None:
                continue
            if succMx >= beta:
                return None,None,None
            if succMx > mx:
                mx = succMx
                mxMove = mv
                mxCoolBd=coolBd
        
        return mxCoolBd,mxMove,mx
    else:
        mn = 9001
        mnMove = None
        mnCoolBd=None
        for mv in mvs:
            board.push(mv)
            coolBd,succMove,succMn = stateless_find_max_move(MACHINE_COLOR,board,alpha,min(mn,beta),depth-1)
            board.pop()
            if succMn is None:
                continue
            if succMn <= alpha: 
                return None,None,None
            if succMn < mn:
                mnCoolBd=coolBd
                mn = succMn
                mnMove = mv
        return mnCoolBd,mnMove,mn

def _negamax(MACHINE_COLOR,board,alpha,beta,depth):
    if depth == 0:
        val=quiesce(MACHINE_COLOR,board,alpha,beta,10)
        return val   #    return f(MACHINE_COLOR,board)
    
    mvs=board.legal_moves
    for mv in mvs:
        board.push(mv)
        bestVal=-_negamax(MACHINE_COLOR,board,-beta,-alpha,depth-1)
        board.pop()
        if bestVal >= beta:
            return beta
        if bestVal > alpha:
            alpha = bestVal
    return alpha

def negamax(MACHINE_COLOR,board,alpha,beta,depth):
    mvs=board.legal_moves
    bestMv=None
    for mv in mvs:
        board.push(mv)
        bestVal=-_negamax(MACHINE_COLOR,board,-beta,-alpha,depth-1)
        board.pop()
        if bestVal >= beta:
            return beta
        if bestVal > alpha:
            alpha = bestVal
            bestMv=mv
    return bestMv,alpha
#is the move a check or capture
def is_loud(board,mv):
    ret = board.is_capture(mv)
    board.push(mv)
    ret = ret and board.is_check()
    board.pop()
    return ret 
#returns a function to pass to filter, to check if a move is loud
def make_is_loud(board):
    def _is_loud(mv):
        return is_loud(board,mv)    
    return _is_loud

def quiesce(MACHINE_COLOR,board,alpha,beta,depth):
    local_val=f(board.turn,board) 
    if depth == 0:
        return local_val
    if local_val >= beta: 
        return beta
      
    alpha=max(alpha,local_val) 
    mvs=filter(make_is_loud(board),list(board.legal_moves))
    #mvs=filter(board.is_capture,list(board.legal_moves))
    for mv in mvs:
        board.push(mv)
        score=-quiesce(MACHINE_COLOR,board,-beta,-alpha,depth-1)
        board.pop()
        if score >= beta:
                
            return beta
        if score>alpha:
            if score >= beta:
                return beta    
            alpha=score 
    return alpha

#the whole point of this program is to implement this function Zwa
def old_predict(board):
    init_tables()
    ret = old_stateless_find_max_move(board.turn,board,-902,902,4)
    print("with a value of",ret[1])
    return ret[0]
def predict(board):
    init_tables() 
    #ret = stateless_find_max_move(board.turn,board,-9002,9002,4)
    ret=negamax(board.turn,board,-9002,9002,4)
    print("with a value of ",ret[1])
    return ret[0]
def machine_game():
    board = chess.Board()
    board.set_fen("5b1r/4p1p1/p3k3/1p1rPn1p/4Q3/PP6/5PPP/4R1K1 w - - 0 29")    
    while not(board.is_game_over()):
        mv = None
        if board.turn == chess.WHITE:
             mv=board.parse_san(input("enter your move:"))
            # mv = predict(board)
        else:
             #mv=board.parse_san(input("enter your move:"))
             mv = predict(board)

        if mv is None:
                    
            print("move is none and boolean isWhite'sTurn is ",board.turn==chess.WHITE)
        print("boolean isWhite'sTurn is ",board.turn==chess.WHITE)
        board.push(mv)
        print("and the after the move, the board is \n")
        print(board)
        print(board.fen())
    print("its over and the result is ",board.result())
if __name__ == "__main__": 
    
    machine_game()


