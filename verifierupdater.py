import requests, json, time
src = "https://www.speedrun.com/api/v1/"

with open("vdatabase.json", "r") as f:
    fjson = json.loads(f.readlines()[0])
#with open("outputs/verifieroutput.txt", "w") as v:
#    v.truncate(0)
no = 0
usersid = ""
t = time.time()
fjsonk = list(fjson.keys())[:] #list(fjson.keys()).index("86n5knqx")
while True:
    if usersid != "":
        fjsonk = list(fjson.keys())[list(fjson.keys()).index(usersid):]
        print(usersid)
    try:
        for user in fjsonk:
            usersid = user
            print(fjson[user][0], len(list(fjson.keys()))-list(fjson.keys()).index(user))
            if fjson[user][0] in ["dha", "1", "Reni", "jensj56"]:
                continue
            while True:
                no += 1
                try:
                    if time.time() - t < 0.8:
                        time.sleep(0.8 - (time.time() - t))
                    o1600 = requests.get(src + f"runs?examiner={user}&max=1&offset=1600").json()
                    t = time.time()
                    if "status" in list(o1600.keys()):
                        if o1600["status"] == 404:
                            o1600 = []
                            break
                        else:
                            print("We're getting rate limited!", o1600["status"])
                            time.sleep(10)
                            continue   
                    o1600 = o1600["data"]
                    break
                except Exception:
                    if "status" in list(o1600.keys()):
                        if o1600["status"] == 404:
                            o1600 = []
                            break
                        else:
                            print("We're getting rate limited!", o1600["status"], "test")
                            time.sleep(10)
                            continue
            if len(o1600) == 0:
                continue
            allruns = []
            lastrun = {"id": "whadohdwao///"}
            breakeverything = False
            deleted = False
            for dir in ["asc", "desc"]:
                offset = 0
                while offset < 10000:
                    while True:
                        try:
                            if time.time() - t < 0.8:
                                time.sleep(0.8 - (time.time() - t))
                            runs = requests.get(src + f"runs?examiner={user}&direction={dir}&max=200&offset={offset}&orderby=date").json()
                            t = time.time()
                            if "status" in list(runs.keys()):
                                if runs["status"] == 404:
                                    deleted = True
                                    break
                                else:
                                    print("We're getting rate limited!")
                                    time.sleep(10)
                                    continue
                            break
                        except Exception:
                            print("We're getting rate limited!")
                            time.sleep(10)
                            continue
                    if deleted:
                        break
                    runs = runs["data"]
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
                print(len(allruns)) 
            with open("outputs/verifieroutput.txt", "a") as f:
                if deleted:
                    continue
                else:
                    f.writelines(f"{user}, {len(allruns)}\n")
        break
    except Exception:
        continue


