# AUTOGENERATED! DO NOT EDIT! File to edit: 01_pgn2csv.ipynb (unless otherwise specified).

__all__ = ['pgn2df', 'pgn2csv']

# Cell
import chess.pgn
import pandas as pd

# Cell
def pgn2df(pgn):
    """Put the data from the PGN headers into a dataframe.
    """
    game = chess.pgn.read_game(pgn)
    game_info = []
    while game:
        game_info.append(dict(game.headers))
        game = chess.pgn.read_game(pgn)
    df = pd.DataFrame(game_info)
    return df

# Cell
def pgn2csv(in_pgn, out_csv):
    """Extract the data from a PGN file to a CSV.
    """
    with open(in_pgn) as pgn:
        df = pgn2df(pgn)
    df.to_csv(out_csv)