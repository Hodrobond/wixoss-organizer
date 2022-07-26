from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.request import urlopen
import json
from sqlalchemy import Integer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from db import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///wixoss'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def get_url(page: Integer):
  return "https://www.takaratomy.co.jp/products/en.wixoss/card/itemsearch.php?p=" + str(page) + "&ord=asc&sor=&"

def add_card(card: init_db.Cards):
  transformed_card = init_db.Cards(
      id = card["ID"],
      product_type = card["product_type"],
      jpn_card_no = card["JPN_card_no"],
      card_no = card["card_no"],
      name = card["name"],
      color = card["color"],
      card_type = card["card_type"],
      rarity = card["rarity"],
      cost = card["cost"],
      level = card["level"],
      limits = card["limits"],
      master = card["master"],
      lrig_signi_type = card["LRIG_SIGNI_type"],
      guard_coin_timing = card["guard_coin_timing"],
      grow_cost = card["grow_cost"],
      power = card["power"],
      content = card["content"],
      power_text = card["power_text"],
      fllabor_text = card["fllabor_text"],
      artist = card["artist"],
      flg = card["flg"],
      sdate = card["sdate"],
  )

  try:
      insert_table = db.session.add(transformed_card)
      print(transformed_card)
      # insert_table = insert(init_db.Cards).values(transformed_card)
      # insert_table.on_conflict_do_nothing(
      #   index_elements=['id']
      # )
      db.session.commit()

  except SQLAlchemyError as e:
    print(e)
    error = str(e)
    print(error)
    pass

def crawl_cards():
  print("crawling")
  response = urlopen(get_url(0)).read()
  data_json = json.loads(response.decode('utf-8'))
  max_count = data_json["count"]
  count = len(data_json["items"])
  for card in data_json["items"]:
      print("card", card["ID"])
      add_card(card)

  page = 1
  while(count < int(max_count)):
    response = urlopen(get_url(page)).read()
    data_json = json.loads(response.decode('utf-8'))

    for card in data_json["items"]:
      print("card", card["ID"])
      add_card(card)
    page += 1
    count += len(data_json["items"])
