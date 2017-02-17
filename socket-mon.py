
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM
import collections
import psutil

AD = "-"
AF_INET6 = getattr(socket, 'AF_INET6', object())

def main():
    templ = "%-10s %-60s %-60s %-13s"
    x = []
    y = {}
    sort_proc = {}

    print(templ % (
        "PID", "Local address", "Remote address", "Status"))

    for c in psutil.net_connections(kind='inet'):
        if (c.status == "NONE"):
            pass
        else:
            laddr = "%s@%s" % (c.laddr)
            raddr = ""
            if c.raddr:
                raddr = "%s@%s" % (c.raddr)

            x.extend([c.pid])
    y = collections.Counter(x)
    sort_proc =sorted(y.items(), key=lambda x: (-x[1], x[0]))

    #print sort_proc
    l = []

    for key in sort_proc:
        temp = key[0]
        l.append(temp)
    #print l

    for z in l:
        for c in psutil.net_connections(kind='inet'):
            if z == c.pid:
                    if (c.status == "NONE"):
                        pass
                    else:
                        laddr = "%s@%s" % (c.laddr)
                        raddr = ""
                    if c.raddr:
                        raddr = "%s@%s" % (c.raddr)

                    print(templ % (c.pid or AD,laddr,raddr,c.status))


if __name__ == '__main__':
    main()
