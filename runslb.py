import json
with open("outputs/runsoutput.txt", "r") as o:
    output = "".join(o.readlines())
    rlb, rILlb, rFGlb = {}, {}, {}
    for i in output.split("\n")[:-1]:
        rlb.update({i.split(", ")[0]: int(i.split(", ")[1])})
        rFGlb.update({i.split(", ")[0]: int(i.split(", ")[2])})
        rILlb.update({i.split(", ")[0]: int(i.split(", ")[3])})

with open("outputs/runsfinallb.txt", "a") as flb:
    flb.truncate(0)
    nr, no, ibefore = 1, 1, 1
    with open("database.json", "r") as datab:
        database = json.loads(datab.readlines()[0])
        for i in list(dict(sorted(rlb.items(), key=lambda item: item[1], reverse=True)).keys()):
            if ibefore != 1:
                if not rlb[ibefore] == rlb[i]:
                    no = nr
            flb.writelines(f'`{no}.`{database[i][1]}`{database[i][0]}' + " "*(26-(len(str(rlb[i]))+len(database[i][0])+len(str(no)))) + f'{rlb[i]}`\n')
            nr+=1
            ibefore = i

with open("outputs/runsFGfinallb.txt", "a") as flb:
    flb.truncate(0)
    nr, no, ibefore = 1, 1, 1
    with open("database.json", "r") as datab:
        database = json.loads(datab.readlines()[0])
        for i in list(dict(sorted(rFGlb.items(), key=lambda item: item[1], reverse=True)).keys()):
            if ibefore != 1:
                if not rFGlb[ibefore] == rFGlb[i]:
                    no = nr
            flb.writelines(f'`{no}.`{database[i][1]}`{database[i][0]}' + " "*(26-(len(str(rFGlb[i]))+len(database[i][0])+len(str(no)))) + f'{rFGlb[i]}`\n')
            nr+=1
            ibefore = i

with open("outputs/runsILfinallb.txt", "a") as flb:
    flb.truncate(0)
    nr, no, ibefore = 1, 1, 1
    with open("database.json", "r") as datab:
        database = json.loads(datab.readlines()[0])
        for i in list(dict(sorted(rILlb.items(), key=lambda item: item[1], reverse=True)).keys()):
            if ibefore != 1:
                if not rILlb[ibefore] == rILlb[i]:
                    no = nr
            flb.writelines(f'`{no}.`{database[i][1]}`{database[i][0]}' + " "*(26-(len(str(rILlb[i]))+len(database[i][0])+len(str(no)))) + f'{rILlb[i]}`\n')
            nr+=1
            ibefore = i