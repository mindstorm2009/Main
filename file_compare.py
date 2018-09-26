def char_by_char(name1, name2):
    print("Character by Character:")
    f1 = open(name1)
    f2 = open(name2)
    linecount = 0
    linenumber = 0
    charcount = 0
    totallinecount1 = 0
    totallinecount2 = 0
    totalcharcount1 = 0
    totalcharcount2 = 0
    print("Unmatched Character:", end=" ")
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        line1 = line1.strip()
        line2 = line2.strip()
        linenumber += 1
        if line1 != "":
            totallinecount1 += 1
            totalcharcount1 += len(line1)
        if line2 != "":
            totallinecount2 += 1
            totalcharcount2 += len(line2)
        if len(line1) == len(line2):
            for ch2 in range(0, len(line2)):
                if line1[ch2] != line2[ch2]:
                    print(linenumber, ":", ch2, sep="", end=", ")
                    charcount += 1
        else:
            linecount += 1
        if totallinecount1 > totallinecount2 or totallinecount1 < totallinecount2:
            print(linenumber, end=", ")
            break
    print("")
    print("There are", totalcharcount1, "characters in", name1)
    print("There are", totalcharcount2, "characters in", name2)
    print("There are", charcount, "unmatched characters in the files")
    print("There were", linecount, "lines of different length")
    f1.close()
    f2.close()


def main():
    char_by_char("t1.txt", "t2.txt")


if __name__ == '__main__':
    main()
