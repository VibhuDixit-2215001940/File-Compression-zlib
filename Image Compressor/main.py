#COMPRESSIG IMAGE USING PILLOW - pip install Pillow
from PIL import Image

actual_image = "pic.jpg"

pic = Image.open(actual_image)

pic.save("ok.jpg","JPEG",optimise=True,quality=30)
#Here first argument is the name of file which we want to put on new file
#Less the quality will less compression