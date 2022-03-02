# ChessData
> Tools for analyzing chess data.


Access chess games with public APIs, convert chess formats like PGNs to data-friendly formats like CSVs, and analyze moves with chess engines.

## About

Chess is a rich area for data analysis. Records of billions (!) of games are available for free. These can be mined not only for chess insights, but to research other areas of interest including explainable AI, fraud detection, and many others. But chess games are typically not stored in formats suitable for data analysis.

This library contains tools to make it easier to do research with chess data. It allows you to convert PGNs - the most common format for chess games, which is human-readable but poorly suited to data analysis - and converts them to data-friendly formats like CSVs. It also contains utilities for using a chess engine to analyze the quality of moves in large numbers of games.

## Install

`pip install chessdata`

## How to use

```python
from chessdata.etf import pgn2df
```

```python
pgn = open("data/magnus.pgn")
```

```python
df = pgn2df(pgn)
```

|    | Event            | Site                         | Date       | Round   | White         | Black         | Result   |   BlackElo |   BlackRatingDiff | BlackTitle   | ECO   | Termination   | TimeControl   | UTCDate    | UTCTime   | Variant   |   WhiteElo |   WhiteRatingDiff | WhiteTitle   |
|---:|:-----------------|:-----------------------------|:-----------|:--------|:--------------|:--------------|:---------|-----------:|------------------:|:-------------|:------|:--------------|:--------------|:-----------|:----------|:----------|-----------:|------------------:|:-------------|
|  0 | Rated Blitz game | https://lichess.org/lAV0T0zl | 2021.12.23 | ?       | DrNykterstein | may6enexttime | 1-0      |       2974 |                -2 | GM           | B20   | Normal        | 180+0         | 2021.12.23 | 23:28:07  | Standard  |       3212 |                +2 | GM           |
|  1 | Rated Blitz game | https://lichess.org/Nfk9W01S | 2021.12.23 | ?       | may6enexttime | DrNykterstein | 0-1      |       3209 |                +3 | GM           | E48   | Time forfeit  | 180+0         | 2021.12.23 | 23:21:54  | Standard  |       2977 |                -3 | GM           |
|  2 | Rated Blitz game | https://lichess.org/mpxofZFJ | 2021.12.23 | ?       | DrNykterstein | may6enexttime | 1-0      |       2979 |                -2 | GM           | B20   | Time forfeit  | 180+0         | 2021.12.23 | 23:15:48  | Standard  |       3207 |                +2 | GM           |
|  3 | Rated Blitz game | https://lichess.org/hjSxkukT | 2021.12.23 | ?       | may6enexttime | DrNykterstein | 0-1      |       3204 |                +3 | GM           | E48   | Normal        | 180+0         | 2021.12.23 | 23:10:43  | Standard  |       2982 |                -3 | GM           |
|  4 | Rated Blitz game | https://lichess.org/5cgs1l6r | 2021.12.23 | ?       | DrNykterstein | may6enexttime | 1-0      |       2984 |                -2 | GM           | B20   | Normal        | 180+0         | 2021.12.23 | 23:07:55  | Standard  |       3202 |                +2 | GM           |

Please see the notebooks for more examples and use cases.
