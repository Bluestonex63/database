import requests, time, json
src = "https://www.speedrun.com/api/v1/"

with open("database.json", "r") as f:
    fjson = json.loads(f.readlines()[0])
with open("deletedusers.txt", "a") as d:
    d.truncate(0)
newdatabase = {}
no = 0
t = time.time()
for i in list(fjson.keys()):
    deleted = False
    while True:
        if (no % 50 == 0 and no != 0) and time.time() - t < 40:
            time.sleep(40 - (time.time() - t))
            t = time.time()
        flag = requests.get(src + f"users/{i}").json()
        no += 1
        try:
            flag = flag["data"]
            username = flag["names"]["international"]
            if flag["location"] == None:
                flag = ":united_nations:"
            else:
                flag = f':flag_{flag["location"]["country"]["code"][:2]}:' 
        except KeyError:
            if flag["status"] == 404:
                deleted = True
                break
#                flag = fjson[i][1]
#                username = fjson[i][0]
#                with open("deletedusers.txt", "a") as d:
#                    with open("outputs/verifieroutput.txt", "r") as v:
#                        verifierdict = {}
#                        for ver in "".join(v.readlines()).split("\n"):
#                            verifierdict.update({ver.split(", ")[0]: ver.split(", ")[1]})
#                    with open("outputs/runsoutput.txt", "r") as r:
#                        runsdict = {}
#                        for ru in "".join(r.readlines()).split("\n"):
#                            runsdict.update({ru.split(", ")[0]: [ru.split(", ")[1], ru.split(", ")[2], ru.split(", ")[3]]})
#                    with open("outputs/pbsoutput.txt", "r") as r:
#                        pbsdict = {}
#                        for pb in "".join(r.readlines()).split("\n"):
#                            pbsdict.update({pb.split(", ")[0]: [pb.split(", ")[1], pb.split(", ")[2], pb.split(", ")[3]]})
#                    d.writelines(f"{username}, {verifierdict[i]}, {runsdict[i][0]}, {runsdict[i][1]}, {runsdict[i][2]}, {}")
            else:
                time.sleep(10)
                continue
        break
    if not deleted:
        if i == "j26g4pnx":
            flag = ":flag_ru:"
        newdatabase.update({i: [username, flag]})
    print(username, flag, len(list(fjson.keys()))-len(list(newdatabase.keys())))
with open("database.json", "w") as w:
    w.writelines(json.dumps(newdatabase))
