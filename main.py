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
import appengine_config
import webapp2
import logging
import os
import jinja2
import requests
import urllib
from google.appengine.api import urlfetch
from parserXML import parseXML
from emailsend import mailing

import statement_datastore as sds
import userinfo_datastore as ui_ds

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)
categoryIcons = {"dining_out": "cutlery", "rainy_day":"cloud",
                "groceries":"shopping-cart", "travel":"suitcase",
                "entertainment":"film", "electronics":"gamepad"}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template("templates/budgeting.html")
        self.response.write(main_template.render())

class MasterCardHandler(webapp2.RequestHandler):
    def get(self):
        arguments = self.request.GET.items()
        url = arguments[0][1] + "/merchantid/v1/merchantid"
        date = arguments[1][1]
        merchant_id = arguments[2][1]
        price = arguments[3][1]
        statement_name = arguments[4][1]
        field = {
            "Format": "XML",
            "MerchantId": merchant_id
        }
        #field = "/merchantid/v1/merchantid?Format=XML&MerchantId=" + merchant_id
        form_data = urllib.urlencode(field)
        result = urlfetch.fetch(
            url = url + "?" + form_data,
            deadline=10
        )
        try:
            if(result.status_code == 200):
                category = parseXML(result.content)
                new_userinfo = sds.Statement(
                    statement_name = statement_name,
                    date = date,
                    merchant_id = merchant_id,
                    price = float(price),
                    category = category
                )
                new_userinfo.put()
            else:
                logging.info("Error: " + str(result.status_code))
        except urlfetch.InvalidURLError:
            logging.info("INVALID URL")
        except urlfetch.DownloadError:
            logging.info("Server cannot be contacted")

        self.redirect("/analysis")

class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template("templates/settings.html")
        self.response.write(main_template.render())

class AnalysisHandler(webapp2.RequestHandler):
    def get(self):
        template_header = JINJA_ENVIRONMENT.get_template('templates/header.html')
        template_footer = JINJA_ENVIRONMENT.get_template('templates/footer.html')

        self.response.write(template_header.render())

        template_values = {}
        template_values["entries"] = []
        price_list = {}
        entries = sds.Statement.query().fetch()
        for entry in entries:
            if price_list.has_key(entry.category):
                price_list[entry.category] = price_list[entry.category] + entry.price
            else:
                price_list[entry.category] = entry.price
        for key, value in price_list.iteritems():
            budget = ui_ds.UserInformation.query(ui_ds.UserInformation.category == key).fetch()[0].limit
            logging.info(budget)
            percent = value/budget*100
            new_entry = {
                "category_name": categoryIcons[key],
                "percent_spent": percent,
                "total_amount": value,
                "budget": budget
            }
            new_entry["entry_id"] = entry.key.urlsafe()
            template_values["entries"].append(new_entry)
        template = JINJA_ENVIRONMENT.get_template('templates/progressBarTemplate.html')
        self.response.write(template.render(template_values))
        # Close the page
        self.response.write(template_footer.render())

        #mailing()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/mc-handler", MasterCardHandler),
    ("/settings", SettingsHandler),
    ("/analysis", AnalysisHandler)
], debug=True)
#parser
