#!/usr/bin/python3

from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length


class Players(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    attack_rating = db.Column(db.Integer, nullable=False)
    defense_rating = db.Column(db.Integer, nullable=False)
    runner = db.Column(db.Boolean, default=False)