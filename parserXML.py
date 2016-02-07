from xml.dom.minidom import parse
import xml.dom.minidom
import logging
import re

def parseXML(xml):
    dictionary = ["SPORTING", "ELECTRONIC", "WEAR", "INNS", "FOOD",
              "RESTAURANTS", "EATING", "RENTAL", "STATIONS", "CREDIT",
            "COMPUTER", "ELECTRICAL", "RECORD"]
    #logging.info("IN PARSEXML WEEEEEE")
    #logging.info(xml)
    # Open XML document using minidom parser
    #DOMTree = xml.dom.minidom.parse(xml)
    #logging.info("thisinfo")
    #collection = DOMTree.documentElement
    category = re.search("<MerchantCategory>([^']+)</MerchantCategory>", xml).group(1)
    #logging.info("CATEGORY PARSD:" + category)
    #getting the list of nodes with that tag name
    #category = collection.getElementsbyTagName("MerchantCategory")[0]

    #accessing the string inside
    #string = category.childNodes[0].data

    #split that string
    splitArr = category.split()
    array = splitArr[2:]

    #loop to see if it is in dictionary
    for element in array:
        for key in dictionary:
            if element == key:
                category = key

    return checkCategory(category)

def checkCategory(category):
    entertainment = ["SPORTING", "RECORD", "CREDIT"]
    dining = ["RESTAURANTS", "EATING"]
    electronics = ["ELECTRONIC", "COMPUTER"]
    travel = ["RENTAL", "INNS", "STATIONS"]
    if category in entertainment:
        answer = "entertainment"
    elif category in dining:
        answer = "dining_out"
    elif category in electronics:
        answer = "electronics"
    elif category in travel:
        answer = "travel"
    elif category == "FOOD":
        answer = "groceries"
    elif category == "WEAR":
        answer = "clothing"
    else:
        answer = "rainy_day"
    return answer
