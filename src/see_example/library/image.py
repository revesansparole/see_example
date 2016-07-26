from PIL import Image


def load_image(pth):
    """Load an image from file

    Args:
        pth (str): path to image file

    Returns:
        (Image)
    """
    img = Image.open(pth)
    return img


def store_image(img, pth):
    """Write an image on disk

    Args:
        img (Image):
        pth (str): path to image file

    Returns:
        (str): the path used
    """
    img.write(pth)
    return pth


def to_hsv(img):
    """Convert a RGB image into HSV

    Args:
        img (Image): RGB triplets

    Returns:
        (Image): HSV triplets
    """
    return img


def to_rgb(img):
    """Convert a HXV image into RGB

    Args:
        img (Image): HSV triplets

    Returns:
        (Image): RGB triplets
    """
    return img


def lower(img, threshold):
    """Force zero on pixels lower than threshold

    Args:
        img (Image):
        threshold (tuple of int): one value for each channel of image

    Returns:
        (Image)
    """
    return img


def upper(img, threshold):
    """Force 255 on pixels higher than threshold

    Args:
        img (Image):
        threshold (tuple of int): one value for each channel of image

    Returns:
        (Image)
    """
    return img


def apply_mask(img, mask):
    """Apply mask on image

    Args:
        img (Image): RGB image
        mask (Image): binary image

    Returns:
        (Image)
    """
    return img


def average(img, scaling):
    """Compute weighted average of all pixels

    Args:
        img (Image):
        scaling (tuple of int): weight of each channel of image

    Returns:
        (float)
    """
    return 0.


