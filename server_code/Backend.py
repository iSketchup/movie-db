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
def query_database_dict_Ratings(id:int):
  query = f'SELECT * FROM RATING WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_database_dict_Actors(id:int):
  query = f'SELECT * FROM ACTOR WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_database_dict_Success(id:int):
  query = f'SELECT * FROM Success WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_database_dict_Studio(id:int):
  query = f'SELECT * FROM STUDIO WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_database_dict_Genre(id:int):
  query = f'SELECT * FROM GENRE WHERE MID={id}'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]