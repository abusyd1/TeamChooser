#!usr/bin/python3

from application import app, db
from application.models import Players

db.drop_all()
db.create_all()
db.session.add_all([
    Players(name = "Hussain Ahmed", position = "Forward", attack_rating = 90, defense_rating = 60, runner = False),
    Players(name = "Abul Shaher", position = "Defence", attack_rating = 75, defense_rating = 85, runner = True),
    Players(name = "Jamiul Hoque", position = "Forward", attack_rating = 85, defense_rating = 70, runner = False),
    Players(name = "Abu Shuu", position = "Defence", attack_rating = 70, defense_rating = 80, runner = False)])
db.session.commit()