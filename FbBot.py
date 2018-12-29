from fbchat import Client
from fbchat.models import *
from tqdm import tqdm

class FbBot():
  def __init__(self, email, password):
    self.client = Client(email, password)
    self.thread_id = '1920112608081580'

  def getListOFNames():
    # Returns a list of all names in chat.
    pass

  def lunchMessages():
    [
      {'date': "27/11/17", 'participants': [navne]}
    ]
