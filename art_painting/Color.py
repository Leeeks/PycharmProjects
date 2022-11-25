import colorgram

my_color_tuple_rgb = []
my_color_tuple_hsl = []
colors = colorgram.extract("painting.jpg", 6)

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b

    new_color = (r, g, b)

    my_color_tuple_rgb.append(new_color)

print(my_color_tuple_rgb)