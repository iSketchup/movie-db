from ._anvil_designer import StudioTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Studio(StudioTemplate):
  def __init__(self, sid, **properties):
    self.init_components(**properties)
    self.RP_Movies.items = anvil.server.call('query_database_dict_Movie', sid)
    self.load_ratings_chart(sid)

  @handle("lk_Homepage", "click")
  def lk_Homepage_click(self, **event_args):
    open_form('Homepage')

  def load_ratings_chart(self, studio_id):
    data = anvil.server.call('query_ratings_by_studio', studio_id)

    titles = [row['Title'] for row in data]
    ratings = [row['AvgRating'] for row in data]

    self.plot_1.data = [{
      'type': 'bar',
      'orientation': 'h',
      'x': ratings,
      'y': titles,
      'marker': {'color': '#4A90E2'},
      'text': [f"{r:.1f}" for r in ratings],
      'textposition': 'outside'
        }]
        
    self.plot_1.layout = {
      'xaxis': {
        'range': [0, 10],
        'title': 'Ø Rating',
        'color': '#ffffff',
        'gridcolor': '#444444',
        'zerolinecolor': '#444444'
      },
      'yaxis': {
        'automargin': True,
        'color': '#ffffff',
        'gridcolor': '#444444'
      },
      'paper_bgcolor': 'transparent',
      'plot_bgcolor': 'transparent',
      'font': {'color': '#ffffff'},
      'margin': {'l': 150, 'r': 40, 't': 20, 'b': 40},
      'height': max(200, len(titles) * 50)
    }