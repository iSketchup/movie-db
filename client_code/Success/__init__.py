from ._anvil_designer import SuccessTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Success(SuccessTemplate):
  def __init__(self,MID, **properties):
    self.init_components(**properties)
    self.displa(MID)

def display_movie_success(self, movie_id):
  # 1. Call your existing server function
  # Note: This returns a list of dictionaries
  results = anvil.server.call('query_database_dict_Success', movie_id)

  if results:
    # Get the first record (since MID is UNIQUE in your schema) 
    stats = results[0]

    # 2. Format and display Profit & Budget as Currency
    # Using Python f-string formatting for commas and 2 decimal places
    profit = stats.get('Profit', 0)
    budget = stats.get('Budget', 0)
    self.label_profit.text = f"Profit: ${profit:,.2f}"
    self.label_budget.text = f"Budget: ${budget:,.2f}"

    # 3. Format Ticket Sales and Views with commas
    sales = stats.get('Ticket_sales', 0)
    views = stats.get('Views', 0)
    self.label_sales.text = f"Tickets Sold: {sales:,}"
    self.label_views.text = f"Total Views: {views:,}"

    # 4. Optional: Add a "Net Success" color logic
    if profit > budget:
      self.label_profit.foreground = "#2e7d32" # Success Green
    else:
      self.label_profit.foreground = "#c62828" # Alert Red

  else:
    self.label_profit.text = "No success data found for this ID."