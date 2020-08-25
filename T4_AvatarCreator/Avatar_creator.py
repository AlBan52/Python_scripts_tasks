from PIL import Image

image = Image.open("monro.jpg")

if image.mode != "RGB":
    image = image.convert("RGB")
red, green, blue = image.split()

offset_pix = 50
coordinates_left_offset = (offset_pix, 0, image.width, image.height)
coordinates_bothsides_offset = (offset_pix*0.5, 0, image.width-offset_pix*0.5, image.height)
coordinates_right_offset = (0, 0, image.width-offset_pix, image.height)

cropped_left_red = red.crop(coordinates_left_offset)
cropped_both_red = red.crop(coordinates_bothsides_offset)
cropped_right_red = red.crop(coordinates_right_offset)
offset_red = Image.blend(cropped_right_red, cropped_both_red, 0.28)

cropped_right_blue = blue.crop(coordinates_right_offset)
cropped_left_blue = blue.crop(coordinates_left_offset)
cropped_both_blue = blue.crop(coordinates_bothsides_offset)
offset_blue = Image.blend(cropped_left_blue, cropped_both_blue, 0.72)

cropped_both_green = green.crop(coordinates_bothsides_offset)

new_image = Image.merge("RGB", (offset_red, offset_blue, cropped_both_green))
new_image.save('new_image.jpg')
new_image.thumbnail((80, 64))
new_image.save('avatar.jpg')