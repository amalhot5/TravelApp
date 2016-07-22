## Trying to get RESTful calls working

import requests
import time
import random
import uuid
from yelpapi import YelpAPI

#def randomword(length):
 #  return ''.join(random.choice(string) for i in range(length))

def main():
    consumer_key = "z5lwUGdh0deaEbvRhUwCKw"
    consumer_secret = "Tq7QBqhKIKyNBlOEGYzJK0UrLHc"
    token = "QwkD6OQ_h3zslXmnTyoitk5vZqhSt8pv"
    token_secret = "95Oyv0QdB_v6ghyi87oe8AtPkBo"
    yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)
    args = {"term": "food", "location": "San Fransciso"}
    response = yelp_api.search_query(term = "food", location="Menlo Park")
    params = {"oauth_consumer_key": consumer_key,
              "oauth_token": token,
              "oauth_signature_method": "HMAC-SHA1",
              "oauth_signature": token_secret,
              "oauth_timestamp": int(time.time()),
              "oauth_nonce": uuid.uuid4()
              }
    #url = "https://api.yelp.com/v2/search?term=food&location=San+Francisco"
    #response = requests.get(url, params=params)
    rand = random.randint(0,len(response['businesses']))
    while rand < 4:
        if response['businesses'][rand]['rating'] >= 4:
            break
        else:
            rand = random.randint(0,len(response['businesses']))
    rec_rest = {'restaurant': response['businesses'][rand]['name'],
                'rating': response['businesses'][rand]['rating']}
    for i in range(len(response['businesses'])):
        if response['businesses'][i]['rating'] >= 4:
            print({'restaurant': response['businesses'][i]['name'],
                'rating': response['businesses'][i]['rating']})
        else:
            pass
    print('\n',rec_rest,sep='')

if __name__ == "__main__":
    main()
