import xml.etree.ElementTree as ET
import json
import requests

url = "https://api.intercom.io/articles"
headers = {
    'Authorization': 'Bearer <Your Intercom Token>',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
def loadRSS():
    # url of RSS feed
    url = '<Your RSS FEED>'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # saving the XML file
    with open('recurfeed.xml', 'wb') as f:
        f.write(resp.content)

def parseRSS():
        # create element tree object
        feed = ET.parse('recurfeed.xml')

        # get root element
        root = feed.getroot()

        #Iterating through all items
        for childitem in root.findall('./channel/item'):

                #creating an empty dictionary
                dict={}

                # iterate child elements of childitem
                for child in childitem:

                    #storing necessary tags in dictionary
                    if(child.tag == 'title'):
                        dict[child.tag]=child.text
                    if (child.tag == '{http://purl.org/rss/1.0/modules/content/}encoded'):
                        dict['body'] = child.text
                    if(child.tag == 'link'):
                        dict[child.tag] = child.text

                    dict['author_id'] = 4334234
                    dict['state'] = "draft"

                #Converting dictionary into JSON object
                json_dict=json.dumps(dict)

                #Sending JSON object to the server
                res = requests.post(url, data=json_dict, headers=headers)

        print(res.status_code)

# load RSS from web to update existing xml file
loadRSS()
parseRSS()



