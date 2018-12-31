from fbchat import Client
from fbchat.models import *
from tqdm import tqdm
from datetime import date as dt
class FbBot():
  def __init__(self, email, password):
    self.client = Client(email, password)
    self.thread_id = '1920112608081580'
    self.group = self.client.fetchThreadInfo(self.thread_id)[self.thread_id]
    self.names = self.getListOfNames()

  def getListOfNames(self):
    # Returns a list of all names in chat.
    self.users = [self.client.fetchUserInfo(uid)
                  for uid in tqdm(self.group.participants)]
    return [self._formatName(str(user)) for user in self.users]

  def _formatName(self, user):
    name, uid = tuple(user.split('USER ')[1].split(')')[0].split('('))
    return (name[:-1], uid)


  def getLunches(self):
    cnt = self.group.message_count + 1
    flach_id = '100002684466673'
    frokost_besked = 'Hvem spiser med i dag?'
    messages = self.client.fetchThreadMessages(
      self.thread_id, cnt)
    messages = messages[::-1]
    ppl = []
    for message in messages:
      if (message.author == flach_id and
          (message.text is not None and
           frokost_besked in message.text)):
        date = int(message.timestamp) // 1000 # Fucking miliseconds
        ppl.append({
          'date': dt.fromtimestamp(date),
          'msgid': message.uid,
          'reactions': [self._idToName(user) for user, react in
            message.reactions.items() if react == MessageReaction.YES]
        })
    return ppl


  def _idToName(self, target_id):
    for name, uid in self.names:
      if uid == target_id:
        return name
