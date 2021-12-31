# AUTOGENERATED! DO NOT EDIT! File to edit: 02_engine_analysis.ipynb (unless otherwise specified).

__all__ = ['evaluate_game', 'evaluate_pgn']

# Cell
import chess.engine
import chess.pgn
import pandas as pd

# Cell
def evaluate_game(game, engine, limit=chess.engine.Limit(time=.1)):
    board = game.board()
    moves = game.mainline_moves()
    evals = []
    for move in moves:
        board.push(move)
        info = engine.analyse(board, limit=limit)
        score = info["score"].pov(chess.WHITE).score()
        evals.append(score)
    return evals

# Cell
def evaluate_pgn(pgn, engine, limit=chess.engine.Limit(time=.1)):
    game = chess.pgn.read_game(pgn)
    all_evals = []
    while game:
        all_evals.append(evaluate_game(game, engine, limit))
        game = chess.pgn.read_game(pgn)
    df = pd.DataFrame(all_evals)
    return df