# "0.1": "/tickingarea add -297 155 -272 -248 57 -232 loader"

import json

timeline = {}

step_time = float(input("Seconds between steps: "))


#timeline["0.0"] = "/tickingarea add {} {} {} {} {} {} loader".format(x1, y1, z1, x2, y2, z2)

CHUNK = 16
time = 0

for x in range(0, 96, 16):
    for z in range(0, 96, 16):
        timeline[str(time)] = ["/say Adding loader...", "/tickingarea add {} {} {} {} {} {} loader".format(x, 0, z, x + CHUNK, 0, z + CHUNK)]
        for y in range(0, 64, 16):
            time += step_time
            timeline[str(time)] = ["/say Removing click...", "/fill {} {} {} {} {} {} air".format(x, y, z, x + CHUNK, y + CHUNK, z + CHUNK)]
            time += step_time
            time += step_time
        timeline[str(time)] = "/tickingarea remove loader"




out = json.dumps(timeline, indent=4)
print(out)
