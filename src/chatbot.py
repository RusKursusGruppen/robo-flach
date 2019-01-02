from fbchat import Client, log
from fbchat.models import *
import configparser

class ChatBot(Client):
  def __init__(self):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['FACEBOOK']
    self.thread_id = config['thread_id']
    super().__init__(config['email'], config['password'])
    self.nicknames = {
        '100001439663466': "Skidt i Munden",
        '1813893027': "Patten",
        '100002788986214': "Carl",
        '100001701883744': 'Bro',
        '1314645780': 'Kan ikke Kode',
        '100000114374787': 'Bjon',
        '1217108195': 'Truntebasse'
    }

  def onNicknameChange(self, a_id, changed, new_nick, t_id, t_type, **kwargs):
    if self.thread_id == t_id and changed in self.nicknames and \
    self.nicknames[changed] != new_nick:
      log.info("{} changed {}'s' nickname. It will be changed back".format(
          a_id, changed_for))
      self.changeNickname(
          self.nicknames[changed], changed, thread_id=t_id, thread_type=t_type)


client = ChatBot()
client.listen()
