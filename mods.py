import requests, json, time
src = "https://www.speedrun.com/api/v1/"

database = {}
t = time.time()
for offset in range(100000000000):
    for i in range(5):
        try:
            games = requests.get(src + f"games?offset={offset*200}&max=200&embed=moderators").json()["data"]
            break
        except Exception:
            time.sleep(5)
            continue
    if time.time() - t < 0.7:
        try:
            time.sleep(0.7 - (time.time() - t))
            t = time.time()
        except Exception:
            t = time.time()
    for game in games:
        for mod in game["moderators"]["data"]:
            try:
                id = mod["id"]
            except Exception:
                continue
            if id in list(database.keys()):
                database[id][2] += 1
                continue
            if mod["location"] == None:
                flag = ":united_nations:"
            else:
                flag = f':flag_{mod["location"]["country"]["code"][:2]}:' 
            print({id: [mod["names"]["international"], flag, 1]}, offset*200)
            database.update({id: [mod["names"]["international"], flag, 1]})
    if len(games) < 200:
        break

with open("vdatabase.json", "a") as vd:
    vd.truncate(0)
    vd.writelines(json.dumps(database))