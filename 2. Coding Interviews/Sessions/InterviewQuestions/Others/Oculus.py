"""
Print 100 random events of the form:
date time: service (random), load (random 0 - 100), client (random)

services = [
    "control",
    "reader",
    "handler",
    "messager",
    "analyst"
]

clients = [
    "terminal 1",
    "terminal 2",
    "terminal 3",
    ....
    "terminal 20",
    "operator 1",
    ...
    "operator 5"
]
"""

# /var/log.log
"""
04-11-2021-21:00:02: control,11, terminal 1
04-11-2021-21:00:03: alanyst,98, terminal 3
.
.
.
"""
services = [
    "control",
    "reader",
    "handler",
    "messager",
    "analyst"
]

import random
from datetime import datetime


def printRandom100Events():
    clients = ["terminal " + str(i) for i in range(1, 21)]

    for i in range(1, 6):
        clients.append("operator " + str(i))

    clients = ["terminal " + str(i) for i in range(1, 21)]
    outputs = []
    for i in range(100):
        now = datetime.now()
        line = ""
        line += now.strftime("%d/%m/%Y %H:%M:%S") + ": service "

        line += random.choice(services) + ", load "
        line += str(random.randrange(0, 101)) + ", client "
        line += random.choice(clients)
        outputs.append(line)
    return "\n".join(outputs)


output = printRandom100Events()
print(output)
print("#" * 5)

"""
parse that list for events with load > 75
"""

def parseLoad75(output):
    #    output = printRandom100Events()
    lines = output.split("\n")
    for line in lines:
        # date time: service (random), load (random 0 - 100), client (random)
        strs = line.split(",")
        # strs[1] = load 5,  load 77
        if int(strs[1][6:]) > 75:
            print(line)


parseLoad75(output)
