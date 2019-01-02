## Robo-Flach
#### The helper for our lunch club.
The club works by one person writing "anybody up for lunch?" in a messenger
thread, the people that want to join then reacts to the message with a `👍` 
emoji.

## Set-up
Run the following set of commands to get a local development environment
```bash
$ pip3 install virtualenv
$ virtualenv -p `which python3` virtualenv
$ source virtualenv/bin/activate
$ pip install -r requirements.txt
$ pip install git+https://github.com/carpedm20/fbchat.git@refs/pull/371/head
```
You also need two credential files, one must be located at `src/config.ini` and
it must contain the following.
```ini
[FACEBOOK]
email = <email>
password = <password>
thread_id = <Thread_id>
```
The other credential file is for the google sheet, follow the 
[setup guide][google guide] to obtain the file.

## Dependencies
The two main dependencies are [FBchat][fbChat] which is the library used for
interaction with messenger, and [Gspread](https://gspread.readthedocs.io) that
interacts with Google Sheets.


## Code Structure
The code is split into two parts, one part the does the balance sheet and keeps
tracks of lunches. The other part is a chatbot that does fun/annoying things.

* [src/FbBot.py][FbBot] and [googleBot.py][googleBot]
    These files wrap around the apis for messenger and sheets. They are used
    for the balance sheet part of the code.
* [src/main.py][main]
    This files combines the two above parts to get the lunch balance, the file
    is made to be run about once per week with no state. **Only place code that
    is [Idempotent](https://en.wikipedia.org/wiki/Idempotence)**
* [src/chatBot.py][chatbot]
    This is the _fun_ part of the code, here the bot actually writes in the
    chat, this file extends the class described [here][class]. The code is
    event driven so look at the functions of the form `onEventHappend` for
    instance `onMessage`. Additional Inspiration can be found
    [here](https://fbchat.readthedocs.io/en/master/examples.html)



## TODO
* [ ] Write message about lunch on every weekday
* [ ] Welcome new members and add them to sheet
* [ ] Add jokes and shit to chatbot
* [ ] Any ideas?

## Done
* [X] ~~Write function that gets all names~~
* [X] ~~Write function that gets all lunches~~
* [X] ~~Function that creates a the table of lunhces~~
* [X] ~~Environment setup~~

[google guide]: https://gspread.readthedocs.io/en/latest/oauth2.html
[fbbot]: https://github.com/RusKursusGruppen/robo-flach/blob/master/src/FbBot.py
[fbChat]: https://fbchat.readthedocs.io/en/master/#
[main]: https://github.com/RusKursusGruppen/robo-flach/blob/master/src/main.py
[googleBot]: https://github.com/RusKursusGruppen/robo-flach/blob/master/src/googleBot.py
[chatbot]: https://github.com/RusKursusGruppen/robo-flach/blob/master/src/chatbot.py
[class]: https://fbchat.readthedocs.io/en/master/api.html
