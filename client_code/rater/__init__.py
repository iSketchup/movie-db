from ._anvil_designer import raterTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class rater(raterTemplate):
  def __init__(self, rating, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.rating = rating
    self.set_stars(rating)
  
  def set_stars(self, count):
    """Füllt die Sterne bis zur gewählten Zahl aus."""
    self.rating = count
    stars = [self.star_1, self.star_2, self.star_3, self.star_4, self.star_5]
    
    for i, star in enumerate(stars):
      if i < count:
        star.icon = "fa:star"   # Gefüllter Stern
        star.foreground = "#FFD700" # Goldgelbe Farbe
      else:
        star.icon = "fa:star-o" # Leerer Stern
        star.foreground = "theme:Gray 500"
        
  def star_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.set_stars(1)

  def star_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.set_stars(2)

  def star_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.set_stars(3)

  def star_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.set_stars(4)

  def star_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.set_stars(5)
