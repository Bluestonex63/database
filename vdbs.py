import json
newdatabase = {}
with open("vdatabase.json", "r") as f:
    f = f.readlines()[0]
    f = json.loads(f)
with open("outputs/verifieroutput.txt", "r") as o:
    o = "".join(o.readlines())
    for i in list(f.keys()):
        if i in o:
            newdatabase.update({i: [f[i][0], f[i][1]]})
with open("vdatabase.json", "w") as data:
    data.writelines(json.dumps(newdatabase))