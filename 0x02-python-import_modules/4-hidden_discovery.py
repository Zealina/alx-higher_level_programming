#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    name = dir(hidden_4)
    j = 0
    for i in range(len(name)):
        if (name[i][j] == '_') and (name[i][j + 1] == '_'):
            continue
        print("{}".format(name[i]))
