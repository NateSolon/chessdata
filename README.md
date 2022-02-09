# ChessData
> Tools for analyzing chess data.


Access chess games with public APIs, convert chess formats like PGNs to data-friendly formats like CSVs, and analyze moves with chess engines.

## About

Chess is a rich area for data analysis. Records of billions (!) of games are available for free. These can be mined not only for chess insights, but to research other areas of interest including explainable AI, fraud detection, and many others. But chess games are typically not stored in formats suitable for data analysis.

This library contains tools to make it easier to do research with chess data. It allows you to convert PGNs - the most common format for chess games, which is human-readable but poorly suited to data analysis - and converts them to data-friendly formats like CSVs. It also contains utilities for using a ches

## Install

`git clone https://github.com/NateSolon/chessdata.git`

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

```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event</th>
      <th>Site</th>
      <th>Date</th>
      <th>Round</th>
      <th>White</th>
      <th>Black</th>
      <th>Result</th>
      <th>BlackElo</th>
      <th>BlackRatingDiff</th>
      <th>BlackTitle</th>
      <th>ECO</th>
      <th>Termination</th>
      <th>TimeControl</th>
      <th>UTCDate</th>
      <th>UTCTime</th>
      <th>Variant</th>
      <th>WhiteElo</th>
      <th>WhiteRatingDiff</th>
      <th>WhiteTitle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rated Blitz game</td>
      <td>https://lichess.org/lAV0T0zl</td>
      <td>2021.12.23</td>
      <td>?</td>
      <td>DrNykterstein</td>
      <td>may6enexttime</td>
      <td>1-0</td>
      <td>2974</td>
      <td>-2</td>
      <td>GM</td>
      <td>B20</td>
      <td>Normal</td>
      <td>180+0</td>
      <td>2021.12.23</td>
      <td>23:28:07</td>
      <td>Standard</td>
      <td>3212</td>
      <td>+2</td>
      <td>GM</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rated Blitz game</td>
      <td>https://lichess.org/Nfk9W01S</td>
      <td>2021.12.23</td>
      <td>?</td>
      <td>may6enexttime</td>
      <td>DrNykterstein</td>
      <td>0-1</td>
      <td>3209</td>
      <td>+3</td>
      <td>GM</td>
      <td>E48</td>
      <td>Time forfeit</td>
      <td>180+0</td>
      <td>2021.12.23</td>
      <td>23:21:54</td>
      <td>Standard</td>
      <td>2977</td>
      <td>-3</td>
      <td>GM</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rated Blitz game</td>
      <td>https://lichess.org/mpxofZFJ</td>
      <td>2021.12.23</td>
      <td>?</td>
      <td>DrNykterstein</td>
      <td>may6enexttime</td>
      <td>1-0</td>
      <td>2979</td>
      <td>-2</td>
      <td>GM</td>
      <td>B20</td>
      <td>Time forfeit</td>
      <td>180+0</td>
      <td>2021.12.23</td>
      <td>23:15:48</td>
      <td>Standard</td>
      <td>3207</td>
      <td>+2</td>
      <td>GM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rated Blitz game</td>
      <td>https://lichess.org/hjSxkukT</td>
      <td>2021.12.23</td>
      <td>?</td>
      <td>may6enexttime</td>
      <td>DrNykterstein</td>
      <td>0-1</td>
      <td>3204</td>
      <td>+3</td>
      <td>GM</td>
      <td>E48</td>
      <td>Normal</td>
      <td>180+0</td>
      <td>2021.12.23</td>
      <td>23:10:43</td>
      <td>Standard</td>
      <td>2982</td>
      <td>-3</td>
      <td>GM</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rated Blitz game</td>
      <td>https://lichess.org/5cgs1l6r</td>
      <td>2021.12.23</td>
      <td>?</td>
      <td>DrNykterstein</td>
      <td>may6enexttime</td>
      <td>1-0</td>
      <td>2984</td>
      <td>-2</td>
      <td>GM</td>
      <td>B20</td>
      <td>Normal</td>
      <td>180+0</td>
      <td>2021.12.23</td>
      <td>23:07:55</td>
      <td>Standard</td>
      <td>3202</td>
      <td>+2</td>
      <td>GM</td>
    </tr>
  </tbody>
</table>
</div>



Please see the notebooks for more examples and use cases.
