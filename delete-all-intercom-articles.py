import requests
import json

// intercom supports deletion of upto 30 articles a time so a loop will help to not the run the code multiple times
for articles in range(5):
    url_to_fetch='https://api.intercom.io/articles'
    headers = {
        'Authorization': 'Bearer <Your Intercom Token>',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.get(url_to_fetch, headers=headers)
    articles_in_a_dictionary=json.loads(response.text)

    for i in articles_in_a_dictionary["data"]:
            id=i["id"]
            url_to_delete="https://api.intercom.io/articles/" + str(id)
            delete_response = requests.delete(url_to_delete, headers=headers)
    print(delete_response)





