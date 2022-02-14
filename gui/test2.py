from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image as kiImage
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

canvas_img = Image.new('RGB', (240, 120), color=(255, 255, 255))
# (do stuff to canvas_img)

data = BytesIO()
canvas_img.save(data, format='png')
data.seek(0) # yes you actually need this
im = CoreImage(BytesIO(data.read()), ext='png')
self.beeld = kiImage() # only use this line in first code instance
self.beeld.texture = im.texture
