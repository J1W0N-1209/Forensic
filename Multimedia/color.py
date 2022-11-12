from PIL import Image

img = Image.open("E:\Forensic\Multimedia/color.png")
data = img.load()
red = (255, 0, 0)

text = ""

binary_lines = []
width, height = img.size

for x in range(height):
    binary_line = []
    for y in range(width):
        pixel = data[y,x]
        if pixel == red:
            binary_line.append('1')
        else:
            binary_line.append('0')
    binary_lines.append(binary_line)

for x in binary_lines:
    text += ''.join([chr(int(''.join(x),2))])

print(text)