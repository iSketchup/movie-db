from ._anvil_designer import IT_ActorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class IT_Actor(IT_ActorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.IM_Actor.source = self.item['ImageURL']
    self.LB_Actor.text = self.item['Name']
