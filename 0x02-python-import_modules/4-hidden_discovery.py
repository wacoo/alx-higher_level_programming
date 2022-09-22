#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    ls = dir(hidden_4)

    for ll in ls:
        if ll[:2] != "__":
            print(ll)
