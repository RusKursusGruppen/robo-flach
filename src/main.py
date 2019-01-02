from src.FbBot import FbBot
from src.googleBot import Gbot
from datetime import date
from tqdm import tqdm
import time

gbot = Gbot()
fbot = FbBot()


lunches = gbot.lunches_to_table(
  fbot.getLunches(),
  [name for name, _ in fbot.names]
)


lunches
