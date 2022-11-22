from fastapi import FastAPI
import urllib
import requests

app = FastAPI(docs_url='/')

@app.get("/url_shorten")
def shorten_url(link, alias):
    url = urllib.parse.quote(link)
    name = alias
    r = requests.get(f'http://cutt.ly/api/api.php?key={INSERT API HERE}&short={url}&name={name}')
    data = r.json()
    output = data['url']['shortLink']
    return output