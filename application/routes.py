#!/usr/bin/python3

from application import app, db
from application.models import Players
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


@app.route('/players', methods=['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def players():
    if request.method =="GET":
       return render_template("players.html", query=Players.query.all())