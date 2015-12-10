import json
from utils import get_token, get_cats
import requests as r


with open('credentials.json') as credentials_file:
    creds = json.load(credentials_file)

detector_url = 'http://catdetector.biz/?imageurl='

access_token = get_token(creds)
cats = get_cats(access_token, 10)

for cat in cats:
    resp = r.get(detector_url + cat['image_url'] + '&json')

    if resp.status_code == 200:
        probability_of_cat = resp.json()['probability']

        if probability_of_cat > 70:
            comment = 'This is cat! I am %.2f%% sure of it.' % probability_of_cat
        elif 70 >= probability_of_cat > 50:
            comment = 'This might be cat... there is a %.2f%% chance' % probability_of_cat
        elif probability_of_cat <= 50:
            comment = 'This is not a cat! How dare you disparage the #cat hashtag! I am %.2f%% sure this is not a cat' % (100 - probability_of_cat)

        comment_url = 'https://api.instagram.com/v1/media/%s/comments' % cat['id']

        print comment
        post_data = {'text': comment, 'access_token': access_token}
        post_resp = r.post(url=comment_url, data=post_data)
        if post_resp.status_code != 200:
            print "Unable to post..."
