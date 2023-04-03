import json

with open("outputs/gamesoutput.json") as g:
    games = json.loads(g.readlines()[0])

for i in games:
    with open(f"outputs/{i}finallb.txt", "a") as flb:
        flb.truncate(0)
        no, nr, ibefore = 1, 1, 1
        for game in list(dict(sorted(games[i].items(), key=lambda item: item[1], reverse=True)).keys()):
            if ibefore != 1:
                if not ibefore == games[i][game]:
                    no = nr
            flb.writelines(str(f'{no}.**{str(game.encode("utf-8"))[2:-1]}** - {games[i][game]}\n'))
            nr+=1
            ibefore = games[i][game]
