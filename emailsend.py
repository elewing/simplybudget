#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import mail
import logging

def findEmail(carrier, number):
    dict = {'T-Mobile' : '@tmomail.net', 'AT&T' : '@txt.att.net', 'Verizon' : '@vtext.com'}
    emailId = number + dict['carrier']
    return emailId

# class ReceiveHandler(webapp2.RequestHandler):
#     def post(self):
#         # mail server sent the post request
#         # there is no browser involved
#         message = mail.InboundEmailMessage(self.request.body)
#         logging.info("received email")
#         logging.info(message.subject)
#         logging.info("from")
#         logging.info(message.sender)
#         logging.info("original message")
#         logging.info(message.original)
#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
def mailing():
    sender = "hackgreenbean@gmail.com"
    # recipient = findEmail(carrier, number) change this
    recipient = "3013517025@vtext.com"
    subject = "GreenBean Alert"
    body = "You are nearing your limit for the budget. Spend cautiously!"
    mail.send_mail(sender, recipient, subject, body)
    logging.info("DONE!")

# app = webapp2.WSGIApplication([
#     ('/', MainHandler),
#     ("/_ah/mail/.+", ReceiveHandler),
# ], debug=True)
