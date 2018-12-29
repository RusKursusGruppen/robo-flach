# Robo-Flach
Vores hjælper i  frokostklubben.

Den virker ved at tjekke alle beskeder igennem i RKG frokost chatten og skriver
i et google sheet hvem der har meldt sig på frokost den dag.


## Opsætning
Kør følgende i din terminal for at opsætte koden.
```bash
$ pip3 install virtualenv
$ virtualenv -p `which python3` virtualenv
$ source virtualenv/bin/activate
$ pip install -r requirements.txt
$ pip install git+https://github.com/carpedm20/fbchat.git@refs/pull/371/head
```
For at få login oplysninger skal du skrive til Flach eller Benja.

## TODO
* [ ] Update google sheet in batches
* [ ] Sort columns by lunch frequency
* [ ] Finish `main.py`
