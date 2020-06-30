import socket
from subprocess import call
from sys import exit

username = input("University of York username > ")
room = input("1) 069\n2) 070\n3) 168\n4) 169 \n5) 270\nPlease select a number > ")


def scan(room, lower_bound, upper_bound):
    for pc in range(lower_bound, upper_bound):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        host = "".join(["cse", room, "pc-", str(pc).zfill(2), ".cs.york.ac.uk"])
        if s.connect_ex((host, 22)) == 0:
            s.close()
            call(["ssh", "-X", "".join([username, "@", host])])
            exit(0)
        s.close()


if room == "1":
    scan("069", 1, 56)
elif room == "2":
    scan("070", 57, 84)
elif room == "3":
    scan("168", 1, 37)
elif room == "4":
    scan("169", 38, 85)
elif room == "5":
    scan("270", 1, 80)
