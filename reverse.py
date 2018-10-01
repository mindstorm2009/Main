def reverse_rec(a_string):
    if a_string == "":
        return ""
    else:
        gnirts = reverse_rec(a_string[1:]) + a_string[0]
        return gnirts


def main():
    a_string = input("Enter a string: ")
    gnirts_a = reverse_rec(a_string)
    print(gnirts_a)


if __name__ == "__main__":
    main()
