import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3


@anvil.server.callable
def query_database_dict_All_Movies():
  query = 'SELECT * FROM MOVIE'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Ratings(id: int):
  query = f'SELECT * FROM RATING WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Actors(id: int):
  """Returns all actors for a given movie MID, via MOVIE_ACTOR junction table."""
  query = f'''
        SELECT ACTOR.*
        FROM ACTOR
        JOIN MOVIE_ACTOR ON ACTOR.AID = MOVIE_ACTOR.AID
        WHERE MOVIE_ACTOR.MID = {id}
    '''
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Success(id: int):
  query = f'SELECT * FROM Success WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Studio(id: int):
  """Returns all studios for a given movie MID, via MOVIE_STUDIO junction table."""
  query = f'''
        SELECT STUDIO.*
        FROM STUDIO
        JOIN MOVIE_STUDIO ON STUDIO.SID = MOVIE_STUDIO.SID
        WHERE MOVIE_STUDIO.MID = {id}
    '''
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Genre(id: int):
  """Returns all genres for a given movie MID, via MOVIE_GENRE junction table."""
  query = f'''
        SELECT GENRE.*
        FROM GENRE
        JOIN MOVIE_GENRE ON GENRE.GID = MOVIE_GENRE.GID
        WHERE MOVIE_GENRE.MID = {id}
    '''
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_database_dict_Movie(sid: int):
  """Returns all movies for a given studio SID, via MOVIE_STUDIO junction table."""
  query = f'''
        SELECT MOVIE.*
        FROM MOVIE
        JOIN MOVIE_STUDIO ON MOVIE.MID = MOVIE_STUDIO.MID
        WHERE MOVIE_STUDIO.SID = {sid}
    '''
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_ratings_by_studio(sid: int):
  query = f'''
        SELECT MOVIE.Title, AVG(RATING.rating) as AvgRating
        FROM MOVIE
        JOIN MOVIE_STUDIO ON MOVIE.MID = MOVIE_STUDIO.MID
        JOIN RATING ON MOVIE.MID = RATING.MID
        WHERE MOVIE_STUDIO.SID = {sid}
        GROUP BY MOVIE.MID, MOVIE.Title
        ORDER BY AvgRating DESC
    '''
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]