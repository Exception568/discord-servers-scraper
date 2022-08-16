import requets
import json
r = requests.get('https://www.reddit.com/domain/discord.gg/new.json', headers={'User-Agent': 'servers scraper'})
json = r.json()
servers = {}
for url in json['data']['children']:
    servers[url['data']['url']] = {'invite': url['data']['url']}
with open('servers.json', 'w') as serversf:
    json.dump(servers, serversf)
