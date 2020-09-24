import requests
import json

// intercom supports deletion of upto 30 articles a time so a loop will help to not the run the code multiple times
for articles in range(5):
    
    // intercom url from which you have to fetch articles
    url_to_fetch='https://api.intercom.io/articles'
    
    headers = {
        'Authorization': 'Bearer <Your Intercom Token>',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    //response will store all the retreived articles in JSON format
    response = requests.get(url_to_fetch, headers=headers)
    
    //to convert JSON file into a dictionary
    articles_in_a_dictionary=json.loads(response.text)
   
    for each_article in articles_in_a_dictionary["data"]:
        
            // intercom deletes article based on their id
            id=each_article["id"]
            url_to_delete="https://api.intercom.io/articles/" + str(id)
            
            //deleting article from the url
            delete_response = requests.delete(url_to_delete, headers=headers)
    
    // Should print 200
    print(delete_response)





