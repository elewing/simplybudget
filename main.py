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

import statement_datastore as sds

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

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

        field = {
            "Format": "XML",
            "MerchantId": merchant_id
        }
        #field = "/merchantid/v1/merchantid?Format=XML&MerchantId=" + merchant_id
        form_data = urllib.urlencode(field)
        logging.info("-------------------" + url + "?" + form_data + "------------")
        result = urlfetch.fetch(
            url = url + "?" + form_data,
            deadline=10
        )
        try:
            if(result.status_code == 200):
                logging.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                category = parseXML(result.content)
                logging.info("CATEGORY: " + category)
            else:
                logging.info("Error: " + str(result.status_code))
        except urlfetch.InvalidURLError:
            logging.info("INVALID URL")
        except urlfetch.DownloadError:
            logging.info("Server cannot be contacted")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/mc-handler", MasterCardHandler)
], debug=True)

#parser
