import json, requests

riotKey = ""

with open('config.json', 'r') as f:
	config = json.load(f)
	riotKey = config["riotApi"]
	name = config["testUser"]
	

getSummonerId = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s" % (name, riotKey))
if getSummonerId.status_code != 200:
	print("Script aborted with error code : %s " %getSummonerId.status_code)
	exit()
else:
	print(getSummonerId.status_code)
	summonerId = getSummonerId.json()["id"]
	print(summonerId)

getChampMastery = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/%s?api_key=%s" % (summonerId, riotKey))
if getChampMastery.status_code != 200:
	print("Script aborted with error code : %s " %getChampMastery.status_code)
	exit()
else:
	print(getChampMastery.status_code)
	print(getChampMastery.json())
	summonerMastery = getChampMastery.json()
