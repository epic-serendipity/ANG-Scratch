import os
import shutil
import logging
from tkinter import filedialog
from tkinter import *

# Create and configure logger
logging.basicConfig(filename='GruntANG.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.DEBUG)

# Create Tkinter window
root = Tk()
root.withdraw()

# Ask user to select a folder
folder_selected = filedialog.askdirectory()

# Create Duplicates folder if it doesn't exist
if not os.path.exists(os.path.join(folder_selected, 'Duplicates')):
    os.mkdir(os.path.join(folder_selected, 'Duplicates'))

# Loop through each file in the selected folder
for filename in os.listdir(folder_selected):
    # Check if the file starts with "126"
    if filename.startswith('126'):
        # Split the filename into its components
        file_info = filename.split('_')
        # Get the unit and last name
        unit = (file_info[0].replace (file_info[0][:3], "")).upper()
        last_name = file_info[-1].split('.')[0].title()
        # Create the destination folder
        destination_folder = os.path.join(folder_selected, unit, last_name)
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # Check if the file already exists in the destination folder
        if os.path.exists(os.path.join(destination_folder, filename)):
            # Move the file to the Duplicates folder
            shutil.move(os.path.join(folder_selected, filename), os.path.join(folder_selected, 'Duplicates'))
            # Log the movement
            logging.info(filename + ' moved to Duplicates')
        else:
            # Move the file to the destination folder
            shutil.move(os.path.join(folder_selected, filename), destination_folder)
            # Log the movement
            logging.info(filename + ' moved to ' + unit + '/' + last_name)