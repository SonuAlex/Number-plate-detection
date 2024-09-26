import os

image_dir = 'images'

image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f)) and f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]

for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]
    txt_file = image_name + '.txt'

    if not os.path.exists(os.path.join(image_dir, txt_file)):
        os.remove(os.path.join(image_dir, image_file))
        print(f'{image_file} deleted')