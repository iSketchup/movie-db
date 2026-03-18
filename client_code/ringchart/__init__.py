from ._anvil_designer import ringchartTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ringchart(ringchartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
  def update_score_ring(self, score):
    # This calls a Javascript function we'll add in a second
    # or you can set the component's HTML directly:
  
    # Calculate color based on score (Green for high, Yellow for mid, Red for low)
    color = "#21d07a" if score >= 70 else "#d2d531" if score >= 40 else "#db2360"
    bg_color = "#204529" if score >= 70 else "#423d0f" if score >= 40 else "#571435"
  
    self.call_js("updateScore", score, color, bg_color)

  
