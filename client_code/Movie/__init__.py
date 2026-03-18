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
    self.IM_Cover.source = rev['CoverURL']

    revR = anvil.server.call('query_database_dict_Ratings', rev['MID'])
    self.RP_Ratings.items=revR
    
    revA = anvil.server.call('query_database_dict_Actors', rev['MID'])

    for row in revA:
      
      picture=Image(source=row['ImageURL'])
      name=Label(text=row['Name'])

      lin_panel=LinearPanel()
      lin_panel.add_component(picture)
      lin_panel.add_component(name)

      self.FP_Actors.add_component(lin_panel)


    revS = anvil.server.call('query_database_dict_Success', rev['MID'])
    print(revS)
    
    # Any code you write here will run before the form opens.

  @handle("Homepage", "click")
  def Homepage_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Homepage')
