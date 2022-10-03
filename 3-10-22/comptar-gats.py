from yogi import tokens

# esquema recorregut

gats = 0

for paraula in tokens(str):
    if paraula == "gat" or paraula == "gata":
        gats += 1
print(gats)
