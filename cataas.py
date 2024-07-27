import requests

def get_cat() -> str:
	contents = requests.get('https://cataas.com/cat?json=true').json()
	url = contents['_id']
	return 'https://cataas.com/cat/' + url

def get_tag(str) -> str:
    try:
        contents = requests.get('https://cataas.com/cat/'+ str +'?json=true').json()
        url = contents['_id']
        return 'https://cataas.com/cat/' + url
    except:
        pass

def get_gif() -> str:
	contents = requests.get('https://cataas.com/cat/gif?json=true').json()
	url = contents['_id']
	return 'https://cataas.com/cat/' + url
