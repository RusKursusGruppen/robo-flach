from fbchat import Client
import fbchat.models

client = Client("hamstervile@hotmail.com", "tomatcykel123")

thread_id = '1920112608081580'

group = client.fetchGroupInfo(thread_id)['1920112608081580']

group.
