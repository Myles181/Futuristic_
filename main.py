import json


data = []
with open('Tweets.json', 'r') as f:
    content = json.loads(f.read())
    for con in range(len(content)):
        if con == 0:
            for k, v in content[con].items():
                if k == "user":
                    data.append(v['name'])
                    data.append(v['followers_count'])
print(data)

