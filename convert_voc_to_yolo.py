import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join
import shutil

# Directories
dirs = ['train', 'validation']
classes = ['pitted_surface', 'rolled-in_scale',"scratches","crazing","inclusion","patches"]


def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)
    return image_list

# Convert VOC to YOLO
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# Convert annotations
def convert_annotation(full_dir_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(full_dir_path + '/annotations/' + basename_no_ext + '.xml')
    out_file = open(output_path + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# Move images from subclasses folder (VOC Folder structure) to images folder (YOLO Folder structure) 
def move_files(source_folder, destination_folder):
    try :
        for _,_, files in os.walk(source_folder):
            if files :
                for file in files :
                    if not os.path.isfile(destination_folder +"/images/" + file) :
                        #print(source_folder + "/" + file)
                        os.rename(source_folder + "/" + file ,destination_folder +"/images/" + file)
        print("Files Moved")
    except Exception as e:
        print(e)
        
def move_subfiles(source_dir, target_dir) :
    file_names = os.listdir(source_dir)
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    for file_name in file_names :
        shutil.move(os.path.join(source_dir, file_name), target_dir)


# Main

cwd = getcwd()
dataset = cwd + "/datasets/NEU-DET" # /home/rayen/projects/NET_DET_YOLOV63/datasets/NEU-DET


for dir_path in dirs:
    full_dir_path = dataset + '/' + dir_path # /home/rayen/projects/NET_DET_YOLOV63/datasets/NEU-DET/train
    output_path = full_dir_path +'/labels/' # /home/rayen/projects/NET_DET_YOLOV63/datasets/NEU-DET/train/labels/

    # Move files to images folder #TODO Manually delete the empty folders and fix cravings240.jpg non existing xml file
    for sub_class in classes :
        source_folder_path = full_dir_path + "/images/" + sub_class 
        
        move_files(source_folder_path,full_dir_path)
        try :
            os.rmdir(source_folder_path)
        except :
            continue
                
    # Create labels folder
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    # Get images paths
    image_paths = getImagesInDir(full_dir_path + "/images")
    

    # Write images paths to list file
    for image_path in image_paths:
        # Convert annotations
        convert_annotation(full_dir_path, output_path, image_path)
    

    for data in ['images', 'labels', 'annotations']:
        if os.path.exists(dataset + '/' + dir_path +  '/' +  data):
            move_subfiles(dataset + '/' + dir_path +  '/' +  data , dataset + '/'+ data + '/' + dir_path)

    
    # Move annotations to labels folder
    print("Finished processing: " + dir_path)


# Remove empty folders  
for dir_path in dirs:
    if os.path.exists(dataset + '/' + dir_path):
        shutil.rmtree(dataset + '/' + dir_path)