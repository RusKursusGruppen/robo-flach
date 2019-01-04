import configparser

from fbchat import Client, log
from fbchat.models import *


class ChatBot(Client):

  def __init__(self):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['FACEBOOK']
    self.thread_id = config['thread_id']
    super().__init__(config['email'], config['password'])
    self.nicknames = {
      '1622678436' : 'Rus',
      '100000065006084': 'Rus',
      '100005477323629': 'Rus',
      '1063982976': 'Rus',
      '1068485193': 'Rus',
      '1280462502': 'Rus',
      '1117141997': 'Rus',
      '1791694781': 'Rus',
      '1161199585': 'Frisk Pige',
      '100000114374787': 'Bjon',
      '100001439663466': 'Skidt i Munden',
      '100001701883744': 'Bro',
      '100002684466673': 'Er lort men bestemmer alt',
      '100032061722593': 'RoboRus',
      '1314645780': 'Kan ikke Kode',
      '1373142153': 'Brokke brok',
      '1382662153': 'August sutter',
      '1445119765': 'pleb',
      '1813893027': 'Patten',
      '533405762': 'Lurker',
      '898295234': 'ArinBjön',
      '100002788986214': "Carl",
      '1217108195': 'Den gode Rotendahl'
    }
    self._checkAllNicks()

  def onNicknameChange(self, author_id, uid, new_nickname, thread_id,
                       thread_type, **kwargs):
    if self.thread_id == thread_id and uid in self.nicknames and \
     self.nicknames[uid] != new_nickname:
      log.info("{} changed {}'s' nickname. It will be changed back".format(
          author_id, uid))
      self.changeNickname(
          self.nicknames[uid],
          uid,
          thread_id=thread_id,
          thread_type=thread_type)

  def _checkAllNicks(self):
    actual_nicks = self.fetchGroupInfo(self.thread_id)[self.thread_id].nicknames
    for uid in self.nicknames:
      if self.nicknames[uid] != actual_nicks[uid]:
        self.changeNickname(self.nicknames[uid], uid, thread_id=self.thread_id,
                  thread_type=ThreadType.GROUP)


client = ChatBot()
client.listen()
