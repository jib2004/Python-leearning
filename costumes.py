import sys # to access CLI Arg

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg) #Take the files and give ability to work on the images
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0,
) #saves to disk