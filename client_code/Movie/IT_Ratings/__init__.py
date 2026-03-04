from ._anvil_designer import IT_RatingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables 
from ...rater import rater

class IT_Ratings(IT_RatingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    print(self.item)
    # Any code you write here will run before the form opens.
    neuer_rater = rater(self.item['rating'])

    self.column_panel.add_component(neuer_rater)

    self.LB_Comment.text = self.item['Comment']
    self.LB_TimeStamp.text = self.item['Timestamp']