import colorgram

colors = colorgram.extract('H.jpeg', 10)
for c in colors:
    print(c.rgb)
