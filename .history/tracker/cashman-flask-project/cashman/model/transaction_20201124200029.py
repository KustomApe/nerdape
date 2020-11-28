import datetime as dt

from marshmallow import Schema, fields

class Transaction():
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount