from PIL import Image, ImageFilter


# img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.convert('L') #for black and white format
# # resize = filtered_img.resize((300,300))#resize method accepts tupples only
# # resize.save("grey.png",'png')
# box=(100,100,400,400)
# region= filtered_img.crop(box)
# region.save("grey.png",'png')

img = Image.open('./astro.jpg')
# helps in maintaining aspect ratio without distorting image
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)