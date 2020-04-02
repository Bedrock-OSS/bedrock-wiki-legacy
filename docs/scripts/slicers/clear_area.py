# "0.1": "/tickingarea add -297 155 -272 -248 57 -232 loader"

import json

timeline = {}

step_size = int(input("Step size: "))
step_time = float(input("Seconds between steps: "))
x1, y1, z1 = input("Start position [x, y, z]: ").split(" ")
x2, y2, z2 = input("End position [x, y, z]: ").split(" ")
start = int(min(int(y1), int(y2)))
end = int(max(int(y1), int(y2)))

step = start

offset = 0
step = start
time = 1.0

timeline["0.0"] = "/tickingarea add {} {} {} {} {} {} loader".format(x1, y1, z1, x2, y2, z2)
while(step < end):
    timeline["%.1f"%time] = ["/clone {} {} {} {} {} {} ~ ~{} ~".format(x1, step, z1, x2, step + step_size - 1, z2, offset)]
    time += step_time
    step += step_size
    offset += step_size

timeline[str(time)] = "/tickingarea remove loader"

out = json.dumps(timeline, indent=4)
print(out)
