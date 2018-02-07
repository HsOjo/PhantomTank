from PIL.Image import Image, new as image_new

from PIL.ImageOps import invert as image_color_invert


def build_phantom_tank(img_inner: Image, img_outer: Image):
    max_w = img_inner.width if img_inner.width > img_outer.width else img_outer.width
    max_h = img_inner.height if img_inner.height > img_outer.height else img_outer.height

    img_inner_l = img_inner.convert('L')
    img_outer_l = image_color_invert(img_outer.convert('L'))

    img_temp = image_new('RGBA', (max_w, max_h), (0, 0, 0, 0))

    for y in range(max_h):
        for x in range(max_w):
            if x % 2 == 0 and y % 2 == 0:
                a = 255
                if x < img_inner_l.width and y < img_inner_l.height:
                    a = img_inner_l.getpixel((x, y))

                img_temp.putpixel((x, y), (255, 255, 255, a))
            else:
                a = 255
                if x < img_outer_l.width and y < img_outer_l.height:
                    a = img_outer_l.getpixel((x, y))

                img_temp.putpixel((x, y), (0, 0, 0, a))

    return img_temp
