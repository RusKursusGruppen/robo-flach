from FbBot import FbBot
from googleBot import Gbot
from datetime import date
from tqdm import tqdm
import time

gbot = Gbot()
fbot = FbBot('robo-flach@rotendahl.dk', 'frokost')

lunches = gbot.lunches_to_table(
  fbot.getLunches(),
  [name for name, uid in fbot.names]
)
cell_list = gbot.sheet.range('A1:B5')
cell_list[0].value = "lol"
print(cell_list[0])
for cell in cell_list:
  cell.value = "jon er dum"
gbot.sheet.update_cells(cell_list)
def fillNamesAndDates(lunch, row_nr):
  gbot.sheet.update_cell(row_nr, 1, lunch['date'])
  for name in lunch['reactions']:
    gbot.sheet.update_cell(row_nr, nameToCol(name), 1)


def nameToCol(target_name):
  for name, col in gbot.columns:
    if name == target_name:
      return col


def get_empty_row():
  row_nr = 1
  while gbot.sheet.cell(row_nr, 1).value != '':
    row_nr += 1
    return row_nr


def input_lunches():
  gbot.fillNames([name for name, id in fbot.names])
  row_nr = get_empty_row()
  lunches = fbot._getLunches()
  for lunch in tqdm(lunches):
    fillRow(lunch, row_nr)
    time.sleep(1)
    row_nr += 1

input_lunches()
