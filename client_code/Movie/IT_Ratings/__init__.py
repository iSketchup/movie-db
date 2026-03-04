from ._anvil_designer import IT_RatingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import rater

class IT_Ratings(IT_RatingsTemplate):
  def __init__(self, rating, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  
    # Any code you write here will run before the form opens.
    neuer_rater = rater(rating)

    self.content_panel.add_component(neuer_rater)