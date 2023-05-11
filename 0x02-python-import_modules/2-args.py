#!/usr/bin/python3
if __name__ == "__main__":
    import sys as syst

    argc = len(syst.argv)
    if argc == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc-1))
        for arg in range(1, argc):
            print("{}: {}".format(arg, syst.argv[arg]))
