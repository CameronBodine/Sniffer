# Sniffer 🐕 
<img src="https://user-images.githubusercontent.com/61564689/156816270-3e0374b9-bd93-4e46-b195-2f88d10c0b54.gif" align="right"
     alt="Sniffer Logo" width="550" height="400">
   
<img src="https://user-images.githubusercontent.com/61564689/156816405-f7f260e3-b020-43fd-8462-023dabcf0b7a.png" align="left"
     alt="Sniffer Logo" width="420" height="150">

- A python application for sorting through geospatial imagery.
- Only sorts jpgs in the `images` directory
- Saves the sorted jpgs in a directory called `sorted_images` within the program's directory

## Running the Program

- There are two ways to run the program, from the command line or from within a jupyter notebook.

#### Jupyter Notebook Method

1. `conda activate Sniffer`
2. `cd <location where you saved Sniffer>`
3. `jupyter notebook`

#### Command Prompt Method

1. `conda activate Sniffer`
2. `cd <location where you saved Sniffer>`
3. `panel serve Sniffer.ipynb`
4. Copy the local host text into your browser of choice `http://localhost:5006/Sniffer`

## Installation Guide

1. `conda env create --file install/Sniffer.yaml`
2. `conda activate Sniffer`
