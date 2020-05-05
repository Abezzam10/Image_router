import random
from math import pi

from PIL import Image
from numpy import squeeze
from bokeh.models import HoverTool
from bokeh.embed import components
from bokeh.plotting import figure

ALLOWED_EXTENSIONS = set(['png', 'bmp', 'jpg', 'jpeg', 'gif'])
LETTER_SET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
IMAGE_LABELS = ['Headphones', 'Mouse', 'Camera', 'Smartphone',
                'Glasses', 'Shoes', 'Watch', 'Laptop']

def is_allowed_file(filename):
    """ Checks if a filename's extension is acceptable """
    allowed_ext = filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    return '.' in filename and allowed_ext


def make_thumbnail(filepath):
    """ Converts input image to 128px by 128px thumbnail if not that size """
    img = Image.open(filepath)
    thumb = None
    w, h = img.size

    # if it is exactly 128x128, do nothing
    if w == 128 and h == 128:
        return True

    # if the width and height are equal, scale down
    if w == h:
        thumb = img.resize((128, 128), Image.BICUBIC)
        thumb.save(filepath)
        return True

    # when the image's width is smaller than the height
    if w < h:
        # scale so that the width is 128
        ratio = w / 128.
        w_new, h_new = 128, int(h / ratio)
        thumb = img.resize((w_new, h_new), Image.BICUBIC)

        # crop the excess
        top, bottom = 0, 0
        margin = h_new - 128
        top, bottom = margin // 2, 128 + margin // 2
        box = (0, top, 128, bottom)
        cropped = thumb.crop(box)
        cropped.save(filepath)
        return True

    # when the image's height is smaller than the width
    if h < w:
        # scale so that the height is 128
        ratio = h / 128.
        w_new, h_new = int(w / ratio), 128
        thumb = img.resize((w_new, h_new), Image.BICUBIC)

        # crop the excess
        left, right = 0, 0
        margin = w_new - 128
        left, right = margin // 2, 128 + margin // 2
        box = (left, 0, right, 128)
        cropped = thumb.crop(box)
        cropped.save(filepath)
        return True
    return False


def generate_random_name(filename):
    """ Generate a random name for an uploaded file. """
    ext = filename.split('.')[-1]
    rns = [random.randint(0, len(LETTER_SET) - 1) for _ in range(3)]
    name = ''.join([LETTER_SET[rn] for rn in rns])
    return "{new_fn}.{ext}".format(new_fn=name, ext=ext)


def generate_barplot(predictions):
    """ Generates script and `div` element of bar plot of predictions using
    bokeh
    """
    # TODO: Add hover functionality
    plot = figure(x_range=IMAGE_LABELS, plot_height=300, plot_width=400)
    plot.vbar(x=IMAGE_LABELS, top=squeeze(predictions), width=0.8)
    plot.xaxis.major_label_orientation = pi / 2.

    return components(plot)