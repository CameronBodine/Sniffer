import pytest
import glob
import os
from Sniffer import sniffer


def test_change_filename():
   # Make an instance of the Sniffer Class   
    sniffer_app = sniffer.SnifferClass()
    sorted_dir=os.getcwd()+os.sep+"test_dir"
    old_filename="old_filename.jpg"
    sort_type="good"
    new_filename_loc=sniffer_app.change_filename(old_filename,sort_type,sorted_dir)
    assert new_filename_loc == sorted_dir+os.sep+"old_filename_good.jpg"


def test_replace_ext(get_temp_images_dir):
   # Make an instance of the Sniffer Class 
    print(get_temp_images_dir)
    sniffer_app = sniffer.SnifferClass()  
    old_ext=["JPG","jpeg"]
    new_ext=".jpg"
    sniffer_app.replace_ext(old_ext,new_ext,images_path=get_temp_images_dir)
    for file in os.listdir(get_temp_images_dir):
           print(f"os.path.splitext(file)[1]: {os.path.splitext(file)[1]}")
           if os.path.splitext(file)[1] != ".png":
               assert  os.path.splitext(file)[1] == ".jpg"

def test_sniffer_initial_button_state():
   # yes, no and undo buttons should be disabled when Sniffer starts
   sniffer_app = sniffer.SnifferClass() 
   assert sniffer_app.yes_button.disabled ==True
   assert sniffer_app.no_button.disabled ==True 
   assert sniffer_app.undo_button.disabled ==True 

def test_modify_buttons_state():
   # yes, no and undo buttons should be enabled when False is passed modify_buttons_state
   sniffer_app = sniffer.SnifferClass() 
   sniffer_app.modify_buttons_state(False)
   assert sniffer_app.yes_button.disabled == False
   assert sniffer_app.no_button.disabled == False 
   assert sniffer_app.undo_button.disabled == False 

