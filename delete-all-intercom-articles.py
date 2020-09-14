import requests
import json

for j in range(5):
    url_to_fetch='https://api.intercom.io/articles'
    headers = {
        'Authorization': 'Bearer <Your Intercom Token>',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    response = requests.get(url_to_fetch, headers=headers)
    dict=json.loads(response.text)

    for i in dict["data"]:
            id=i["id"]
            string="https://api.intercom.io/articles/" + str(id)
            url_to_delete=string
            delete_response = requests.delete(url_to_delete, headers=headers)
    print(delete_response)





