from flask import Flask, redirect, render_template
from datetime import datetime as dt
import json
import requests

app = Flask(__name__)
global deck
#new deck
#вне маршрута, тк базовая функция
def get_deck():
    deck_id =json.loads( requests.post('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').text)['deck_id']
    return deck_id



@app.route('/')
#когда человек запустил сервис, отрисовываем стартовую страницу
def start_page():
    deck=get_deck()
    return render_template('index.html', deck_id=deck)
    
@app.route('/<deck_id>/new_card')
def get_card(deck_id, cards_cnt='1'):
    card = json.loads(requests.post('https://deckofcardsapi.com/api/deck/'+deck_id+'/draw/?count='+cards_cnt).text)['cards']
    return render_template('index.html', card=card, deck_id=deck)



if __name__ == '__main__':
    app.run()
