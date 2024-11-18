# from PIL import Image

# def reconstruct_secret(share1_path, share2_path):
#     # Load share images
#     share1 = Image.open(share1_path)
#     share2 = Image.open(share2_path)

#     # Get image size
#     width, height = share1.size

#     # Create a blank image for the secret
#     secret_image = Image.new("RGB", (width, height))

#     # Reconstruct the secret image pixel by pixel
#     for x in range(width):
#         for y in range(height):
#             # Get pixel values from shares
#             pixel_share1 = share1.getpixel((x, y))
#             pixel_share2 = share2.getpixel((x, y))

#             # Combine shares to reconstruct the secret pixel using XOR
#             secret_pixel = tuple(p1 ^ p2 for p1, p2 in zip(pixel_share1, pixel_share2))

#             # Set pixel in the secret image
#             secret_image.putpixel((x, y), secret_pixel)

#     return secret_image

# # Example usage
# share1_path = "static/share_images/29bb80d2-6580-4c8b-9f25-ff598f57be07share1.enc"
# share2_path = "static/share_images/53b41a07-6563-475a-b1b7-1dc1be51af73share2.enc"
# decrypted_image = reconstruct_secret(share1_path, share2_path)
# decrypted_image.save("static/share_images/decrypted_image.png")  # Save the decrypted image
# print("Decrypted image saved successfully.")

from cryptography.fernet import Fernet
from PIL import Image
import os

def decrypt_images(share1_path, share2_path, key_image_path):
    # Load share images
    with open(share1_path, 'rb') as file:
        share1 = file.read()
    with open(share2_path, 'rb') as file:
        share2 = file.read()

    # Load key from key image
    with open(key_image_path, 'rb') as key_file:
        key = key_file.read()

    # Combine shares to reconstruct the encrypted image data
    encrypted_image_data = share1 + share2

    # Decrypt the image data using the key
    cipher = Fernet(key)
    decrypted_image_data = cipher.decrypt(encrypted_image_data)

    return decrypted_image_data

# Example usage
# share1_path = "static/share_imagescaa9e97f-9696-4618-ba29-612f627abd8bshare1.enc"
# share2_path = "static/share_images3caa6f5f-df9b-4da0-9c38-b54c07b95070share2.enc"
# key_image_path = "static/share_images/key_image.png"

# decrypted_image_data = decrypt_image(share1_path, share2_path, key_image_path)

# # Save the decrypted image
# with open("static/decrypted_image.jpg", 'wb') as file:
#     file.write(decrypted_image_data)

