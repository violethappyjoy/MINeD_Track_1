import os
from PIL import Image
from tqdm import tqdm

# Function to convert images to RGBA, resize to 256x256, and save as PNG
def process_image(input_path, output_path):
    try:
        # Open the image
        image = Image.open(input_path)

        # Convert to RGBA if not already in RGBA format
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        # Resize to 256x256
        image = image.resize((256, 256))

        # Save as PNG
        image.save(output_path, 'PNG')
    except Exception as e:
        print(f"Error processing image {input_path}: {e}")

# Root directory containing sub-folders
root_folder = "class_dirs"
output_folder = "class_dirs_clone"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each sub-folder
for class_name in os.listdir(root_folder):
    class_path = os.path.join(root_folder, class_name)
    output_class_path = os.path.join(output_folder, class_name)

    # Skip if not a directory
    if not os.path.isdir(class_path):
        continue

    # Create output class folder if it doesn't exist
    os.makedirs(output_class_path, exist_ok=True)

    # Iterate through images in the sub-folder
    for filename in tqdm(os.listdir(class_path)):
        input_image_path = os.path.join(class_path, filename)
        output_image_path = os.path.join(output_class_path, filename.split('.')[0] + '.png')

        # Process and save the image
        process_image(input_image_path, output_image_path)
        tqdm.write(f"Processed: {input_image_path}")

print("All images processed and saved.")
