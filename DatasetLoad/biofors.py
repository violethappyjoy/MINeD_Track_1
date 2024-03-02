import os
import json
import shutil
from tqdm import tqdm

classification_dir = "/Users/happyjoy/Joy/SEM6/Extra/MINeD/DatasetLoad/classifjson"
dataset_dir = r"/Users/happyjoy/Joy/SEM6/Extra/MINeD/DatasetLoad/biofors_images"
output_base_dir = r"/Users/happyjoy/Joy/SEM6/Extra/MINeD/DatasetLoad/class_dirs"
image_label_map = {}

for class_name in image_label_map.values():
    class_dir = os.path.join(output_base_dir, class_name)
    os.makedirs(class_dir, exist_ok=True)
    
for jsonFile in tqdm(os.listdir(classification_dir)):
    if jsonFile.endswith('.json'):
        json_filepath = os.path.join(classification_dir,jsonFile)
        with open(json_filepath) as f:
            data = json.load(f)
            
            for key, value in data.items():
                label = key
                for category, images in value.items():
                    for img_pair in images:
                        if isinstance(img_pair, str):  # Check if img_pair is a string
                            img_names = img_pair.split()
                            for img_name in img_names:
                                if img_name.endswith('.png'):  # Check if the file ends with .png
                                    img_path = os.path.join(dataset_dir, key, img_name)
                                    if os.path.exists(img_path):  # Check if file exists before copying
                                        output_dir = os.path.join(output_base_dir, category)
                                        os.makedirs(output_dir, exist_ok=True)  # Ensure destination directory exists
                                        shutil.copy(img_path, output_dir)
                                    else:
                                        print(f"File not found: {img_path}")
                                else:
                                    print(f"Skipping non-PNG file: {img_name}")

print("Images copied successfully.")