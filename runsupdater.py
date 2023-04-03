import requests, json, time
src = "https://www.speedrun.com/api/v1/"

with open("database.json", "r") as f:
    fjson = json.loads(f.readlines()[0])
no, no2 = 0, 0
t = time.time()
for id in fjson:
    allruns = []
    runsIL = 0
    runsFG = 0
    no2 += 1
    lastrun = {"id": "whadohdwao///"}
    breakeverything = False
    deleted = False
    for dir in ["asc", "desc"]:
        offset = 0
        while offset < 10000:
            if time.time() - t < 0.8:
                time.sleep(0.8 - (time.time() - t))
                t = time.time()
            runs = requests.get(src + f"runs?user={id}&direction={dir}&max=200&offset={offset}&orderby=date&status=verified").json()
            no += 1
            if "status" in list(runs.keys()):
                if runs["status"] == 404:
                    deleted = True
                    break
                else:
                    print("We're getting rate limited!")
                    time.sleep(10)
                    continue
            runs = runs["data"]
            for run in runs:
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
    for run in allruns:
        if run["level"] == None:
            runsFG += 1
        else:
            runsIL += 1
    print(fjson[id][0], len(list(fjson.keys()))-no2, len(allruns), runsFG, runsIL, runsFG + runsIL == len(allruns))
    with open("outputs/runsoutput.txt", "a") as output:
        if deleted:
            continue
        else:
            output.writelines(f"{id}, {len(allruns)}, {runsFG}, {runsIL}\n")
