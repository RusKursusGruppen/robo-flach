from FbBot import FbBot
from googleBot import Gbot
from datetime import date
from tqdm import tqdm
import time

gbot = Gbot()
fbot = FbBot()

lunches = gbot.lunches_to_table(
  fbot.getLunches(),
  [name for name, uid in fbot.names]
)
end_row, end_col = lunches.shape
#ranger(row1,col1,row2,col2)
cell_list = gbot.sheet.range(1, 1, end_row, end_col)
cnt = 0
for i in range(end_row):
  for j in range(end_col):
    cell_list[cnt].value = lunches.iloc[i,j]
    cnt += 1
gbot.sheet.update_cells(cell_list)

def fillNamesAndDates(lunch, row_nr):
  gbot.sheet.update_cell(row_nr, 1, lunch['date'])
  for name in lunch['reactions']:
    gbot.sheet.update_cell(row_nr, nameToCol(name), 1)

lunches.columns
