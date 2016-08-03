from base64 import b64decode, b64encode
from io import BytesIO
from numpy import array, rollaxis, where, zeros
from PIL import Image

from library.image import apply_mask, from_png, lower, to_hsv, to_rgb, upper

with open("lena.png", 'rb') as f:
    data = b64encode(f.read())

img = Image.open(BytesIO(b64decode(data)))
hsv = img.convert('HSV')

# filter
a = array(hsv)
mask1d = (a < (255, 128, 255)).all(axis=2)
mask3d = rollaxis(array([mask1d] * 3), 0, 3)

black_a = rollaxis(array([a[:, :, 0], zeros(a.shape[:2]), zeros(a.shape[:2])],
                         dtype=a.dtype), 0, 3)
res = where(mask3d, black_a, a)
# res = where(mask3d, a, zeros(a.shape, dtype=a.dtype) + 255)
#
# false_rgb = Image.fromarray(res, 'RGB')
#
# # create false rgb image with hsv data
# # false_rgb = Image.frombytes('RGB', hsv.size, hsv.tobytes())
#
# # # save it in a string
# # txt = BytesIO()
# # false_rgb.save(txt, 'PNG')
# #
# # # encode it back
# # res = b64encode(txt.getvalue())
#
# false_rgb.save("toto.png")


hsv = to_hsv(data)
with open("hsv.png", 'wb') as f:
    f.write(b64decode(hsv))

low = lower(hsv, (255, 127, 255))
with open("low.png", 'wb') as f:
    f.write(b64decode(low))

up = upper(low, (0, 127, 0))
with open("up.png", 'wb') as f:
    f.write(b64decode(up))

rgb = to_rgb(up)
with open("rgb.png", 'wb') as f:
    f.write(b64decode(rgb))

mask = apply_mask(data, rgb)
with open("mask.png", 'wb') as f:
    f.write(b64decode(mask))
