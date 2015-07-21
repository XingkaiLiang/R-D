def buildConn(param):
    return ":".join(["%s=%s" % (k,v) for k,v in param.items()])

if __name__ == "__main__":
    myparam = {"server":"myserver",\
               "db":"lxk",\
               "pwd":"clc",\
               }
    print buildConn(myparam)
