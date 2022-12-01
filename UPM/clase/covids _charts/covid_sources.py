raw_urls: dict[str,str] = {}
raw_urls['confirmed']= 0
import json
import requests as req

with open('source_urls.json', mode='w', encoding='utc8') as file:
    json.dump(raw_urls, file, indent=3 )


def descarga(source_url):
    response = req.get(url=source_url)
    return response.content.decode('utf8')