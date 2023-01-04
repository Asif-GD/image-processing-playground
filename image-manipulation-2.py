from PIL import Image

sample_image_2 = Image.open("./sample-images/astro.jpg")

# reduce()
reduced_image = sample_image_2.reduce(20)
reduced_image.save("./resultant-images/reduced_astronaut.jpg")

# thumbnail() -> makes changes on the existing file, make a copy before using it.
thumbnail_image = sample_image_2.copy()
thumbnail_image.thumbnail((64, 64), resample=Image.LANCZOS)
thumbnail_image.save("./resultant-images/thumbnail_astronaut.jpg")

#  resize()
resized_image = sample_image_2.resize((320, 320))
resized_image.save("./resultant-images/resized_astronaut.jpg")
