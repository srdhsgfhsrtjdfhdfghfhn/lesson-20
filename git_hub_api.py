import pprint

import requests

url = ''
#token = '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'
#result = requests.get(url, auth = ('srdhsgfhsrtjdfhdfghfhn', token))

headers = {
    'Autorization': f'tokenP{token}'
}

#result = requests.get(url, headers = headers)

session = requests.session()
session.auth = ('srdhsgfhsrtjdfhdfghfhn', token)
#result = session.get(url)

url = 'https://api.github.com/search/code?q=eval+in:file+language:python+user:srdhsgfhsrtjdfhdfghfhn'
result = session.get(url)
pprint.pprint(result.json())
