def char_by_char(name1, name2):
    print("Character by Character:")
    f1 = open(name1)
    f2 = open(name2)
    linecount = 0
    linenumber = 1
    charnumber = 0
    totallinecount1 = 0
    totallinecount2 = 0
    totalcharcount1 = 0
    totalcharcount2 = 0
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        linenumber += 1
        if line1 != "":
            totallinecount1 += 1
            totalcharcount1 += len(line1)
        if line2 != "":
            totallinecount2 += 1
            totallinecount2 += len(line2)
        if len(line1) == len(line2):
            print("place holder")
        else:
            linecount += 1
        if line1 == "" or line2 == "":
            break
    print(linenumber)
    print(totallinecount1, totallinecount2)
    print(totalcharcount1, totalcharcount2)
    print("There were", linecount, "lines of different length")


def main():
    char_by_char("t1.txt", "t2.txt")


if __name__ == '__main__':
    main()
