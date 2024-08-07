from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os
from data_extraction import load_data

def visualize_data():
    try:
        url = load_data()
        url_response = requests.get(url)
        url_response.raise_for_status()  # Raise an error for bad responses
        with zipfile.ZipFile(BytesIO(url_response.content)) as z:
            z.extractall('.')
        print("Data extraction successful.")
    except requests.exceptions.RequestException as e:
        print("Error downloading data:", e)
    except zipfile.BadZipFile:
        print("The downloaded file is not a valid zip file.")
    except Exception as e:
        print("An unexpected error occurred:", e)

    lesion_types = [
        'Actinic keratoses',
        'Basal cell carcinoma',
        'Benign keratosis-like lesions',
        'Chickenpox',
        'Cowpox',
        'Dermatofibroma',
        'Healthy',
        'HFMD',
        'Measles',
        'Melanocytic nevi',
        'Melanoma',
        'Monkeypox',
        'Squamous cell carcinoma',
        'Vascular lesions'
    ]

    total_images = {}
    for lesion_type in lesion_types:
        formatted_name = lesion_type.lower().replace(' ', '_').replace('-', '_') + '_images'
        total_images += os.listdir(os.path.join(os.getcwd(), f'lesions_image_data/{lesion_type}'))

    '''
    actinic_keratoses_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Actinic keratoses'))
    basal_cell_carcinoma_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Basal cell carcinoma'))
    benign_keratosis_lesion_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Benign keratosis-like lesions'))
    chickenpox_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Chickenpox'))
    cowpox_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Cowpox'))
    dermatofibroma_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Dermatofibroma'))
    healthy_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Healthy'))
    hfmd_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/HFMD'))
    measles_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Measles'))
    melanocytic_nevi_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Melanocytic nevi'))
    melanoma_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Melanoma'))
    monkeypox_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Monkeypox'))
    squamous_cell_carcinoma_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Squamous cell carcinoma'))
    vascular_lesions_images = os.listdir(os.path.join(os.getcwd(),'lesions_image_data/Vascular lesions'))
    '''

    path = pathlib.Path(os.path.join(os.getcwd(),'lesions_image_data'))

    def open_random_image(path):
        # Get a list of all files in the folder
        all_files = os.listdir(path)
        random_image_file = random.choice(all_files)
        image_path = os.path.join(path, random_image_file)
        image = Image.open(image_path)
        return image

    # Save two random images from each category
    for lesion in lesion_types:
        for i in range(2):
            image = open_random_image(os.path.join(os.getcwd(),f'lesions_image_data/{lesion}'))
            image.save(f'{lesion.replace(" ", "_").lower()}_{i+1}.jpg')

    return path, total_images

visualize_data()
