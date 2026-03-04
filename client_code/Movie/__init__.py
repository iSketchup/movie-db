from ._anvil_designer import MovieTemplate
from ..rater import rater
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Movie(MovieTemplate):
  def __init__(self, id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    rev = anvil.server.call('query_database_dict_All_Movies')
    rev = rev[id-1]
    print(rev)
    self.IM_Cover.source = rev['CoverURL']

    rev = anvil.server.call('query_database_dict_Ratings', rev['MID'])
    print(rev)
    self.RP_Ratings.items=rev
    # Any code you write here will run before the form opens.

  @handle("Homepage", "click")
  def Homepage_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Homepage')
