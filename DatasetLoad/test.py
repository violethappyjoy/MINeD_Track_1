import os

# Root directory containing sub-folders
root_folder = "/home/joy/Joy/Sem6/MINeD/DatasetLoad/class_dirs_orignal/"

# Iterate through each sub-folder
for class_name in os.listdir(root_folder):
    class_path = os.path.join(root_folder, class_name)

    # Skip if not a directory
    if not os.path.isdir(class_path):
        continue

    # Count the number of images in the sub-folder
    num_images = sum(1 for _ in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, _)))

    print(f"Number of images in {class_name}: {num_images}")
