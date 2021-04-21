from PIL import Image
import pytesseract
from scipy.ndimage.filters import gaussian_filter
import numpy
from PIL import ImageFilter

th1 = 130  # first threshold
th2 = 130  # second threshold
sig = 1.5  # the blurring sigma

# load image object
img_file = input("Enter image name:")
og_img = Image.open(img_file)
og_img.save("original.png")

# convert into black and white image
bw_img = og_img.convert("P")
bw_img.save("black_and_white.png")

# Filtering the image with first threshold
first_threshold = bw_img.point(lambda p: p > th1 and 255)
first_threshold.save("first_threshold.png")

# Blurring the image with gaussian filter
img_array = numpy.array(first_threshold)
blurred_img = gaussian_filter(img_array, sigma=sig)
blurred_img = Image.fromarray(blurred_img)
blurred_img.save("blurred.png")

# Filtering the blurred image with another threshold
final_img = blurred_img.point(lambda p: p > th2 and 255)
final_img = final_img.filter(ImageFilter.EDGE_ENHANCE_MORE)
final_img = final_img.filter(ImageFilter.SHARPEN)
final_img.save("final.png")


captchca_text = pytesseract.image_to_string(Image.open('final.png'))
print(captchca_text)
