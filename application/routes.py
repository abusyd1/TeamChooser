#!/usr/bin/python3

from application import app, db
from application.models import Players
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route('/players', methods=['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def players():
    if request.method =="GET":
       return render_template("players.html", query=Players.query.all())

@app.route('/team2', methods=['GET', 'POST'])
def team1():
    query = Players.query.all()
    team1 = []
    team2 = []
    for player in query:
        if player.attack_rating > 85:
            team1.append(player.name)
        else:
            team2.append(player.name)
    if request.method =="GET":
       return render_template("team2.html", team1=team1, team2=team2)