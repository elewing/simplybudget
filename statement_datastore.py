#!/usr/bin/env python
import webapp2
import logging
from google.appengine.ext import ndb
import re

class Statement(ndb.Model):
    #name of the account
    statement_name = ndb.StringProperty(required = True)
    # date
    date = ndb.StringProperty(required = True)
    # id of the merchant store
    merchant_id = ndb.StringProperty(required = True)
    # price of item
    price = ndb.FloatProperty(required = True)
    # category of of the product
    category = ndb.StringProperty(required = True)

class SaveStatementHandler(webapp2.RequestHandler):
    def post(self):
        statement_name = self.request.get("statement_name")
        date = self.request.get("date")
        merchant_id = self.request.get("merchant_id")
        price_amount = self.request.get("price_amount")
        category = self.request.get("category")

        new_statement = Statement(
            statement_name = statement_name,
            date = date,
            merchant_id = merchant_id,
            price = price_amount,
            category = category
        )
        new_statement.put()

app = webapp2.WSGIApplication([
    ("save-statement", SaveStatementHandler)
], debug = True)
