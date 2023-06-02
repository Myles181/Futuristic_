import json
from Tweets import Model


with open('Tweets.json', 'r') as f:
    data = json.loads(f.read())
    content = Model(__root__=data)

print(content)
