from circle import *

def parser(map):
    map = "song/" + map + "/" + map + ".msu"
    f = open(map, "r")
    if f.mode == 'r':
        content = f.read()
    lines = content.split('\n')
    circles = []
    start = 0
    for line in lines:
        if line == "[Hit Objects]":
            start += 1
            break
        start += 1
    for i in range(start, len(lines) - 1):
        line = lines[i].split('/')
        circles.append(Circle(line[0], line[1], line[2], line[3]))
    return (circles)
