def create_ascii_map():
    map ={}
    for i in range(65,123):
        map[chr(i)] =i
    return map

map =create_ascii_map()
for key in map:
    print(key, map[key], sep=":", end=" ")
print()