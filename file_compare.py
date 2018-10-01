"""
    File: file_compare.py
    Assignment: homework
    Language: python3
    Author: Nicholas Curl
    Purpose: Compare the characters of two files
"""


# Definitions and functions to compare two files


def char_by_char(name1, name2):
    """Function that compares the lines in two files"""
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
        # Reads the lines of each file
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
        # Checks to see if the length of lines are the same
        if len(line1) == len(line2):
            for ch2 in range(0, len(line2)):
                if line1[ch2] != line2[ch2]:
                    print(linenumber, ":", ch2, sep="", end=", ")
                    charcount += 1
        else:
            linecount += 1
        # Checks if there are more lines in any of the files than the other
        if totallinecount1 > totallinecount2 or totallinecount1 < totallinecount2:
            print(linenumber, end=", ")
            break
        # Checks if there are no more lines
        if totallinecount1 == totallinecount2 and line1 == "" or line2 == "":
            break
    print("")
    print("There are", totalcharcount1, "characters in", name1)
    print("There are", totalcharcount2, "characters in", name2)
    print("There are", charcount, "unmatched characters in the files")
    print("There were", linecount, "lines of different length")
    f1.close()
    f2.close()


def main():
    """Main function to run the char_by_char function"""
    file1 = input("File 1:")
    file2 = input("File 2:")
    char_by_char(file1, file2)


# Checks if being run as a file
if __name__ == '__main__':
    main()
