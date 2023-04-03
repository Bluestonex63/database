import requests, json, time
src = "https://www.speedrun.com/api/v1/"
for user in [["dha", "kj9p77x4"], ["reni", "8l0rl9v8"], ["1", "zx7gd1yx"], ["jensj56", "pj0o1g4j"]]:
	allruns = []
	with open(f"platforms{user[0]}.json", "r") as f:
		fj = ""
		for i in f.readlines():
			fj += i.replace("\n", "").replace("\t", "")
		fjson = json.loads(fj)
		platformlist = []
		platformname = []
		for plat in list(fjson.keys()):
			platformlist.append(plat)
			platformname.append(fjson[plat])
	for status in ["verified", "rejected"]:
		for emu in ["1", "0"]:
			for platform in platformlist:
				lastrun = {"id": "whadohdwao///"}
				breakeverything = False
				for dir in ["asc", "desc"]:
					offset = 0
					while offset < 10000:
						print(emu, fjson[platform], dir, status, user[0], offset, len(allruns))
						while True:
							try:
								runs = requests.get(src + f"runs?examiner={user[1]}&emulated={emu}&platform={platform}&direction={dir}&max=200&offset={offset}&orderby=date&status={status}").json()["data"]
								break
							except Exception:
								time.sleep(10)
								continue
						for run in runs:
							if len(run["players"]) > 0:
								if run["players"][0]["rel"] == "guest":
									if run["players"][0]["name"].lower() == "n/a" or run["players"][0]["name"].lower() == "n\a":
										continue
							else:
								continue
							if run["id"] == lastrun["id"]:
								breakeverything = True
								break
							allruns.append(run)
						if len(runs) < 200 or breakeverything:
							break
						offset += 200
					if offset != 10000:
						break
					lastrun = allruns[-1]
	with open("outputs/verifieroutput.txt", "a") as v:
		v.writelines(f"{user[1]}, {len(allruns)}\n")