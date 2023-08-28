import json
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    hours_str = str(hours)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    time_str = f"{hours_str}h {minutes_str}m {seconds_str}s"
    return time_str
with open("outputs/runsoutput.txt", "r") as o:
    output = "".join(o.readlines())
    rlb, rILlb, rFGlb, ttlb = {}, {}, {}, {}
    for i in output.split("\n")[:-1]:
        rlb.update({i.split(", ")[0]: int(i.split(", ")[1])})
        rFGlb.update({i.split(", ")[0]: int(i.split(", ")[2])})
        rILlb.update({i.split(", ")[0]: int(i.split(", ")[3])})
        ttlb.update({i.split(", ")[0]: round(float(i.split(", ")[4]))})

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
with open("outputs/totaltimefinallb.txt", "a") as flb:
    flb.truncate(0)
    nr, no, ibefore = 1, 1, 1
    with open("database.json", "r") as datab:
        database = json.loads(datab.readlines()[0])
        for i in list(dict(sorted(ttlb.items(), key=lambda item: item[1], reverse=True)).keys()):
            if ibefore != 1:
                if not ttlb[ibefore] == ttlb[i]:
                    no = nr
            convert = format_time(ttlb[i])
            flb.writelines(f'`{no}.`{database[i][1]}`{database[i][0]}' + " "*(40-(len(convert)+1+len(database[i][0])+len(str(no)))) + convert + '`\n')
            nr+=1
            ibefore = i