"""
converts an image to pixelate
"""
from PIL import Image, ImageDraw

IMAGE_SCALE = 0.2
PIXEL_SIZE = 5

def convert(image_path):
    """
    TODO
    """
    image = Image.open(image_path)
    image = _convert_to_scale(image, IMAGE_SCALE)\
            .convert('RGB')
    cols, rows = image.size

    size_new_image = (cols*PIXEL_SIZE, rows*PIXEL_SIZE)
    out_image = Image.new("RGB", size_new_image)
    draw = ImageDraw.Draw(out_image)

    for i in range(cols):
        for j in range(rows):
            pixel = tuple(image.getpixel((i, j)))
            hex_value = _rgb_to_hex(*pixel)

            pixel_cord = [(i*PIXEL_SIZE, j*PIXEL_SIZE), ((i*PIXEL_SIZE) + PIXEL_SIZE, (j*PIXEL_SIZE)+PIXEL_SIZE)]
            draw.rectangle(pixel_cord, fill=hex_value)
    return out_image

def _rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def _convert_to_scale(image, scale):
    width, height = image.size
    new_size = (int(width*scale), int(height*scale))
    return image.resize(new_size)

if __name__ == "__main__":
    import sys
    pix_image = convert(sys.argv[1])
    pix_image.save(sys.argv[2])
