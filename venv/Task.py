from PIL import Image, ImageDraw
import itertools

print("Input path to file:")
f = input()
print("Input path to save picture:")
p = input()

#C:\Users\\VivoBook\Desktop\\KGMlab2\DS5.txt
#C:\Users\\VivoBook\Desktop\\KGMlab2\test.png

file = open(f, "r")
line = file.readlines()
dot = []
for i in line:
    cord_x, cord_y = i.split(" ")
    dot.append(int(cord_x))
    dot.append(int(cord_y))
file.close()

image = Image.new("RGBA", (540, 960), (0,0,0,0))
draw = ImageDraw.Draw(image)
draw.point(dot, fill = "black")
image.save(p, "PNG")
