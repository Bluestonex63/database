import json

str = ""
username = ""
with open("outputs/pbsoutput.txt", "r") as r:
    with open("database.json", "r") as d:
        data = json.loads(d.readlines()[0])
        for i in "".join(r.readlines()).split("\n")[:-1]:
            for id in list(data.keys()):
                if data[id][0] ==  i.split(", ")[0]:
                    username = id
            if username == "":
                username = "CHANGEDNAME"
                with open("deletedusers.txt", "a") as f:
                    f.writelines(i.split(", ")[0])
            print(f'{username}, {i.split(", ")[1]}, {i.split(", ")[2]}, {i.split(", ")[3]}, {i.split(", ")[4]}, {i.split(", ")[5]}, {i.split(", ")[6]}, {i.split(", ")[7]}, {i.split(", ")[8]}, {i.split(", ")[9]}')
            str += f'{username}, {i.split(", ")[1]}, {i.split(", ")[2]}, {i.split(", ")[3]}, {i.split(", ")[4]}, {i.split(", ")[5]}, {i.split(", ")[6]}, {i.split(", ")[7]}, {i.split(", ")[8]}, {i.split(", ")[9]}\n'
with open("outputs/pbsoutput.txt", "w") as r:
    r.truncate(0)
    r.writelines(str)
        