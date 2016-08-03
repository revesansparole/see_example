from base64 import b64decode, b64encode
from io import BytesIO
from numpy import array, rollaxis, where, zeros
from PIL import Image


def from_png(data):
    """Load an image from PNG data

    Args:
        data (str): PNG encoded string

    Returns:
        (Image.Image)
    """
    img = Image.open(BytesIO(b64decode(data)))
    return img.convert('RGB')


def to_png(img):
    """Encode an image into a PNG stream

    Args:
        img (Image.Image):

    Returns:
        (str)
    """
    txt = BytesIO()
    img.save(txt, 'PNG')

    # encode it back
    return b64encode(txt.getvalue())


def load_image(pth):
    """Load an image from file

    Args:
        pth (str): path to image file

    Returns:
        (Image.Image)
    """
    img = Image.open(pth)
    return img


def store_image(img, pth):
    """Write an image on disk

    Args:
        img (Image.Image):
        pth (str): path to image file

    Returns:
        (str): the path used
    """
    img.save(pth)
    return pth


def to_hsv(img):
    """Convert a RGB image into HSV

    Args:
        img (Image): RGB triplets

    Returns:
        (Image): HSV triplets
    """
    hsv = from_png(img).convert('HSV')

    # create false rgb image with hsv data
    false_rgb = Image.frombytes('RGB', hsv.size, hsv.tobytes())

    return to_png(false_rgb)


def to_rgb(img):
    """Convert a HSV image into RGB

    Args:
        img (Image): HSV triplets

    Returns:
        (Image): RGB triplets
    """
    false_rgb = from_png(img)
    hsv = Image.frombytes('HSV', false_rgb.size, false_rgb.tobytes())

    img = hsv.convert('RGB')
    return to_png(img)


def lower(img, threshold):
    """Force black on pixels lower than threshold

    Args:
        img (Image):
        threshold (tuple of int): one value for each channel of image

    Returns:
        (Image)
    """
    hsv = from_png(img)
    # filter
    a = array(hsv)
    mask1d = (a < threshold).all(axis=2)
    mask3d = rollaxis(array([mask1d] * 3), 0, 3)

    black_a = rollaxis(array([a[:, :, 0],
                              zeros(a.shape[:2]),
                              zeros(a.shape[:2])],
                             dtype=a.dtype), 0, 3)
    res = where(mask3d, black_a, a)

    false_rgb = Image.fromarray(res, 'RGB')
    return to_png(false_rgb)


def upper(img, threshold):
    """Force white on pixels higher than threshold

    Args:
        img (Image):
        threshold (tuple of int): one value for each channel of image

    Returns:
        (Image)
    """
    hsv = from_png(img)
    # filter
    a = array(hsv)
    mask1d = (a >= threshold).all(axis=2)
    mask3d = rollaxis(array([mask1d] * 3), 0, 3)

    white_a = rollaxis(array([a[:, :, 0],
                              zeros(a.shape[:2]),
                              zeros(a.shape[:2]) + 255],
                             dtype=a.dtype), 0, 3)
    res = where(mask3d, white_a, a)

    false_rgb = Image.fromarray(res, 'RGB')
    return to_png(false_rgb)


def apply_mask(img, mask):
    """Apply mask on image

    Args:
        img (Image): RGB image
        mask (Image): binary image

    Returns:
        (Image)
    """
    img = array(from_png(img))
    mask = array(from_png(mask))

    res = where(mask, img, zeros(img.shape, dtype=img.dtype))

    return to_png(Image.fromarray(res, 'RGB'))


def average(img, scaling):
    """Compute weighted average of all pixels

    Args:
        img (Image):
        scaling (tuple of int): weight of each channel of image

    Returns:
        (float)
    """
    return 0.


