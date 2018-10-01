def reverse_rec(a_string):
    if a_string == "":
        return ""
    else:
        return a_string[0] + reverse_rec(a_string[1:])

def main():
    a_string = input("Enter a string: ")
    gnirts_a = reverse_rec(a_string)
    print(gnirts_a)

if __name__ == "__main__":
    main()
