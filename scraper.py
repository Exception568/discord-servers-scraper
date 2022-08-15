import requets
import json
r = requests.get('https://www.reddit.com/domain/discord.gg/new.json', headers={'User-Agent': 'servers scraper'})
json_data = r.json()
servers = {}
for url in json_data['data']['children']:
    servers[url['data']['url']] = {'link': url['data']['url']}
with open('discord.json', 'w') as datafile:
    json.dump(servers, datafile)
