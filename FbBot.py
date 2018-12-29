from fbchat import Client
from fbchat.models import *
from tqdm import tqdm

class FbBot():
  def __init__(self, email, password):
    self.client = Client(email, password)
    self.thread_id = '1920112608081580'
    self.group = self.client.fetchThreadInfo(self.thread_id)[self.thread_id]

  def getListOfNames(self):
    # Returns a list of all names in chat.
    self.users = [self.client.fetchUserInfo(uid)
                  for uid in tqdm(self.group.participants)]
    return [self._formatName(str(user)) for user in self.users]
    
  def _formatName(self, user):
    return tuple(user.split('USER ')[1].split(')')[0].split('('))
  

  def lunchMessages():
    lunches = self.getLunches()
    
    [
      {'date': "27/11/17", 'participants': [navne]}
    ]
  def _getLunches(self):
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
        ppl.append({'date': message.timestamp, 'msgid': message.uid, 'reactions': message.reactions[MessageReaction.YES]})
      
    return ppl
  #<Message (mid.$gAAbSVQ3u9qxsx4QIFlmlj7Eq0Rb9): 'Hvis man vil spise med skal man like min besked 👍', mentions=[] emoji_size=None attachments=[]>
    

f = FbBot("", "")
#print(f.getListOfNames())
print(f._getLunches())
