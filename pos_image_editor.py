import os
from PIL import Image
from glob import glob

x = 780
y = 645

file_paths = glob(os.path.join(os.getcwd(), '*.png'))

processed_images = []
for file_path in file_paths:
    img = Image.open(file_path)
    new_img = Image.new("RGBA", (x, y), (255, 255, 255, 0))
    # new_img = Image.new("RGBA", (x, y), (255, 255, 255, 255))

    img_width, img_height = img.size
    new_x = round((x - img_width) / 2)
    new_y = round((y - img_height) / 2)

    new_img.paste(img, (new_x, new_y))
    processed_images.append(new_img)

for new_img, output_path in zip(processed_images, file_paths):
    new_img.save(output_path)
