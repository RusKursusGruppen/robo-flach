import gspread
from oauth2client.service_account import ServiceAccountCredentials as SC


class Gbot():
  def __init__(self):
    scope = [
      'https://spreadsheets.google.com/feeds',
      'https://www.googleapis.com/auth/drive'
    ]
    credentials = SC.from_json_keyfile_name('../google-credentials.json', scope)
    client = gspread.authorize(credentials)
    self.sheet = client.open('Frokost Regnskab').worksheet('robo-flach')
    self.columns = []

  def fillNames(self, names):
    names.sort()
    self.sheet.update_cell(1, 1, 'DATES')
    for i in range(2, len(names) + 1):
        self.sheet.update_cell(1, i,  names[i - 2] )
        self.columns.append((names[i - 2], i))
