import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

@anvil.server.callable
def query_database(query:str):
  with sqlite3.connect(data_files["movies.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def query_database_dict_All_Movies():
  query = 'SELECT * FROM MOVIE'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_database_dict_Ratings():
  query = 'SELECT * FROM RATING'
  with sqlite3.connect(data_files["movies.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]
