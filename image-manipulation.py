from PIL import Image, ImageFilter

sample_image = Image.open("./sample-images/pikachu.jpg")
# print(f"sample_image -> {sample_image}")

filtered_image = sample_image.filter(ImageFilter.BLUR)
filtered_image.save("./resultant-images/pikachu_blur.png", format="png")

filtered_image = sample_image.filter(ImageFilter.SHARPEN)
filtered_image.save("./resultant-images/pikachu_sharpen.png", format="png")

# print(dir(Image))
# print(dir(sample_image))

filtered_image = sample_image.convert('L')
filtered_image.save("./resultant-images/pikachu_grey.png", format="png")
