import gspread
from oauth2client.service_account import ServiceAccountCredentials as SC
import pandas as pd

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

  def lunches_to_table(lunches, names):
    weeks = []
    dates = []
    for lunch in lunches:
      year, week_nr, _ = lunch['date'].isocalendar()
      week = str(year) + '-' + str(week_nr)
      if week not in dates:
        row = {'date' : week}
        for name in names:
          row[name] = 0
        dates.append(week)
        weeks.append(row)

    weeks = pd.DataFrame(weeks)
    weeks = weeks[['date'] +list(weeks.columns[:-1])]

    for lunch in lunches:
      year, week_nr, _ = lunch['date'].isocalendar()
      week_row = weeks[weeks['date'] == str(year) + '-' + str(week_nr)]
      for name in lunch['reactions']:
        week_row[name] = week_row[name] + 1
      weeks[weeks['date'] == str(year) + '-' + str(week_nr)] = week_row
    return weeks
