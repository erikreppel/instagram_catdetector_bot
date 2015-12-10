from instagram.client import InstagramAPI
import webbrowser
import requests as r
import json


def get_token(creds, scope=['basic', 'comments', 'public_content']):
    # Fix Python 2.x.
    try:
        import __builtin__
        input = getattr(__builtin__, 'raw_input')
    except (ImportError, AttributeError):
        pass

    client_id = creds['client_id']
    client_secret = creds['client_secret']
    redirect_uri = creds['redirect_uri']

    print 'Connecting to InstagramAPI'

    api = InstagramAPI(client_id=client_id,
                       client_secret=client_secret,
                       redirect_uri=redirect_uri)

    print 'Obtaining auth url'
    redirect_uri = api.get_authorize_login_url(scope=scope)
    webbrowser.open_new_tab(redirect_uri)

    code = (str(input(
                "Login in, then paste in code in query string after redirect: "
                ).strip()))
    access_token = api.exchange_code_for_access_token(code)
    return access_token[0]


def get_cats(token, count):
    try:
        with open('visited_cats.json') as f:
            visited_cats = json.load(f)
    except:
        visited_cats = []

    base_url = 'https://api.instagram.com/v1/tags/cat/media/recent?'
    url = base_url + 'access_token=%s&count=%s' % (token, count)
    resp = r.get(url)
    if resp.status_code == 200:
        matched_posts = resp.json()['data']
        cats = []
        for post in matched_posts:
            cat = {
                    'id': post['id'],
                    'image_url': post['images']['standard_resolution']['url']
                    }
            if cat not in visited_cats:
                visited_cats.append(cat)
                cats.append(cat)

        print 'Found %s cats!' % len(cats)
        f = open('visited_cats.json', 'wb')
        f.write(json.dumps(visited_cats))
        f.close()
        if len(cats) > 0:
            return cats
    else:
        return None
