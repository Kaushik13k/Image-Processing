# import the Python Image processing Library

from PIL import Image

# Create an Image object from an Image

colorImage = Image.open("abc.jpg")

# Rotate it by 45 degrees

rotated = colorImage.rotate(45)

# Rotate it by 90 degrees

transposed = colorImage.transpose(Image.ROTATE_90)

# Display the Original Image

colorImage.show()

# Display the Image rotated by 45 degrees

rotated.show()

# Display the Image rotated by 90 degrees

transposed.show()