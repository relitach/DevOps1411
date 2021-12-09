from PIL import Image, ImageDraw

img = Image.new('RGB', (100, 100), 'blue')

d = ImageDraw.Draw(img)
d.text((10, 50), "Ariel King", 'black')

img.save('Ariel_king.png')
