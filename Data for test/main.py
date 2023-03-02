# Import necessary libraries
from PIL import Image
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout


#Rename images
folder_path = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Train/Sofa'

prefix = 'Sofa_'
count = 1
for filename in os.listdir(folder_path):
  if filename.endswith('.jpg'):
        #old_name = os.path.join(folder_path, filename)
        new_name = prefix + str(count) + '.jpg'
        count += 1
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))  

folder_path = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Train/Bed'

prefix = 'Bed_'
count = 1
for filename in os.listdir(folder_path):
  if filename.endswith('.jpg'):
        #old_name = os.path.join(folder_path, filename)
        new_name = prefix + str(count) + '.jpg'
        count += 1
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

folder_path = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Train/Chair'

prefix = 'Chair_'
count = 1
for filename in os.listdir(folder_path):
  if filename.endswith('.jpg'):
        #old_name = os.path.join(folder_path, filename)
        new_name = prefix + str(count) + '.jpg'
        count += 1
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        
        
        #resize images
        
  def resize_images(input_dir, output_dir, size):
    """
    Resizes all images in input_dir to size and saves them in output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop over all files in the input directory
    for filename in os.listdir(input_dir):
        # Only process image files
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image
            image = Image.open(os.path.join(input_dir, filename))
            # Resize the image
            resized_image = image.resize(size)
            # Save the resized image to the output directory
            resized_image.save(os.path.join(output_dir, filename))

input_dir = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Train'
output_dir = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Train_r'
size = (256, 256)  # target size of the images

resize_images(input_dir, output_dir, size)

input_dir = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Test'
output_dir = 'C:/Users/imman/OneDrive/Documents/Image Classification Project/Data for test/Test_r'
size = (256, 256)  # target size of the images

resize_images(input_dir, output_dir, size)

