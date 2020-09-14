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

    # creating and saving the XML file
    with open('feed.xml', 'wb') as f:
        f.write(resp.content)

def parseRSS():
        # create element tree object
        feed = ET.parse('feed.xml')

        # get root element
        root = feed.getroot()

        #Iterating through all items
        for childitem in root.findall('./channel/item'):

                #creating an empty dictionary
                articles={}

                # iterate child elements of childitem
                for child in childitem:

                    #storing necessary tags in dictionary
                    if(child.tag == 'title'):
                        articles[child.tag]=child.text
                    if (child.tag == '{http://purl.org/rss/1.0/modules/content/}encoded'):
                        articles['body'] = child.text
                    if(child.tag == 'link'):
                        articles[child.tag] = child.text

                    articles['author_id'] = <Your Author id>
                    articles['state'] = "draft"

                #Converting dictionary into JSON object
                articles_in_json=json.dumps(articles)

                #Sending JSON object to the server
                res = requests.post(url, data=articles_in_json, headers=headers)
        
        //Should print <200>
        print(res.status_code)

# load RSS from web to update existing xml file
loadRSS()
parseRSS()



