import json
with open("outputs/modcountfinallb.txt", "a") as filb:
    filb.truncate(0)
    no, no2, bi = 1, 1, ""
    with open("vdatabase.json", "r") as data:
        datab = json.loads(data.readlines()[0])
        m = {}
        for i in datab:
            m.update({i: datab[i][2]})
        for i in list(dict(sorted(m.items(), key=lambda item: item[1], reverse=True)).keys()):
            if bi != datab[i][2]:
                no2 = no
            filb.writelines(str(f'`{no2}.`{datab[i][1]}`{str(datab[i][0].encode("utf-8"))[2:-1]}{" "*(26-(len(str(datab[i][2]))+len(datab[i][0])))}{datab[i][2]}`\n'))
            no+=1
            bi = datab[i][2]