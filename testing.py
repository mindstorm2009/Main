def create_list(filename):
    file = open(filename)
    L = []
    for line in file:
        a,b = line.split(" ")
        b.strip()
        L+= [int(b)]
    file.close()

create_list("test500Keven.txt")
