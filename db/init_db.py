from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///wixoss'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cards(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key = True)
    product_type = db.Column(db.String(256))
    jpn_card_no = db.Column(db.String(256))
    card_no = db.Column(db.String(256))
    name = db.Column(db.String(256))
    color = db.Column(db.String(256))
    card_type = db.Column(db.String(256))
    rarity = db.Column(db.String(256))
    cost = db.Column(db.String(256))
    level = db.Column(db.Integer)
    limits = db.Column(db.String(256))
    master = db.Column(db.String(256))
    lrig_signi_type = db.Column(db.String(256))
    guard_coin_timing = db.Column(db.String(256))
    grow_cost = db.Column(db.String(256))
    power = db.Column(db.Integer)
    content = db.Column(db.String(1024))
    power_text = db.Column(db.String(256))
    fllabor_text = db.Column(db.String(256))
    artist = db.Column(db.String(256))
    flg = db.Column(db.String(256))
    sdate = db.Column(db.DateTime)

def init_cards_db():
  db.create_all()
  print("Cards table created")

  # add a row
  # comment out after the 1st run
  # table_row = models.Cards(name="My Name", email="myemail@mail.com", phone="123456")
  # db.session.add(table_row)
  # db.session.commit()

  # read the data
  # row = models.Cards.query.filter_by(name="My Name").first()
  # print("Found:", row.email, row.phone)
