#!/usr/bin/env python

import webapp2
import logging
from google.appengine.ext import ndb
import re

class UserInformation(ndb.Model):
    # Account/User name
    # account = ndb.StringProperty(required = True)
    # Category that will have a money limit set
    category = ndb.StringProperty(required = True)
    # Numeric limit set for the category
    limit = ndb.IntegerProperty(required = True)

class SaveInformationHandler(webapp2.RequestHandler):
    def post(self):
        # account_name = self.request.get("account_name")
        category_name = self.request.get("category_name")
        limit_amount = self.request.get("limit_amount")

        logging.info("IN THE SAVE HANDLER")
        #Add limit confirmation here? Ask Youyou

        new_userinfo =  UserInformation(
            # account = account_name,
            category = category_name,
            limit = limit_amount
        )
        new_userinfo.put()

app = webapp2.WSGIApplication([
    ("/save-userinfo", SaveInformationHandler)
], debug = True)
