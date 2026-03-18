from ._anvil_designer import StudioTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Studio(StudioTemplate):
  def __init__(self, sid,  **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.RP_Movies.items = anvil.server.call('query_database_dict_Movie', sid)
  
    # Any code you write here will run before the form opens.

  @handle("lk_Homepage", "click")
  def lk_Homepage_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Homepage')
