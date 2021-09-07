import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import urllib.request
import random
import string
import os



model = load_model('./rps.h5')

def get_crop_predict(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x, batch_size=10)
    class_arr = prediction[0]
    class_value = max(class_arr)
    class_list = list(class_arr)
    class_index = class_list.index(class_value)
    
    return (str(class_index),str(class_value))

def download_get_crop_predict(image_url):
    save_name = random_string_generator(25) + '.jpg' 
    currrent_dir = os.getcwd()
    working_dir = currrent_dir + '/images'
    os.chdir(working_dir)
    urllib.request.urlretrieve(image_url, save_name)  
    img = image.load_img(save_name, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction = model.predict(x, batch_size=10)
    class_arr = prediction[0]
    class_value = max(class_arr)
    class_list = list(class_arr)
    class_index = class_list.index(class_value)
    crop_name = ''
    if class_index == 0:
        crop_name = 'Onion'
    elif class_index == 1:
        crop_name = 'Carrot'
    elif class_index == 2:
        crop_name == 'Maize, Cabbage'

    os.chdir('../')
    return (str(class_index),str(class_value), crop_name)

def random_string_generator(str_size):
    chars = string.ascii_letters #+ string.punctuation
    return ''.join(random.choice(chars) for x in range(str_size))
           