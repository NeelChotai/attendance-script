import socket
from contextlib import closing

num = input("1) 069\n2) 070\n3) 168\n4) 169 \n5) 270\nPlease select a number > ")

def scan(room, min, max):
    for pc in range(min, max):
        if pc < 10:
            pc = str(0) + str(pc)
        host = "cse" + room + "pc-" + pc + ".cs.york.ac.uk/"
        if s.connect_ex((host, 22)) == 0:
            print(host)
            return

with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    s.settimeout(2)
    if num == "1":
        scan("069", 1, 56)
    elif num == "2":
        scan("070", 57, 84)
    elif num == 3:
        scan("168", 1, 37)
    elif num == 4:
        scan("169", 38, 85)
    elif num == 5:
        scan("270", 1, 80)

