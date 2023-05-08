# NET_DET_YOLOV63


=============================================================

### Setup Virtual environment

=============================================================

1. Installing miniconda3 : 
    1. Download the Miniconda installer to your Home directory.
`wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh`
    2. Install Miniconda quietly, accepting defaults, to your Home directory.
`bash ~/miniconda.sh -b -p`
    3. Remove the Miniconda installer from your Home directory.
`rm ~/miniconda.sh`
----------------------------------------------

2. Activating environment :
    1. activate conda for this session
`source $HOME/miniconda3/bin/activate`

    2. Creating environment : #Skip if env already created
`conda create --name yolo_defect --file reauirements.txt python=3.8`

    3. Activating the environment : 
`conda activate yolo_defect`

----------------------------------------------

3. Usefull Commands :
- for deactivating :
`conda deactivate`

- to list created environments :
`conda env list`

=============================================================

### COnverting from xml format to YOLO format : 

=============================================================

NOTE : Some changes to file direcories, class names MIGHT need to be added

1. run convert_voc_to_yolo.py file :
`python3 convert_voc_to_yolo.py`

2. Create .yaml file
example : 
```
train: "/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/images/train"
val: "/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/images/validation"

nc: 6
names: ['pitted_surface', 'rolled-in_scale',"scratches","crazing","inclusion","patches"]
```

=============================================================

### Setting Up YOLOv6 v3 : 

=============================================================

1. Install YOLOv6 v3.0
```
git clone --branch v3 https://github.com/meituan/YOLOv6 
cd YOLOv6
pip install -r requirements.txt
```

2. Move images, lablels directories and .yaml file under YOLOv6/data 


3. Modify YOLOv6/run_neu_det.sh as necessesary for train/eval/infer 

=============================================================

### Using YOLOv6 v3 : 

=============================================================


1. `cd YOLOv6/` 

Add executable permissions to Shell script :
`sudo chmod +x ./run_neu_det.sh` 

2. For training / Evaluation / inference :
`run ./run_neu_det.sh`

2. For Evaluation / Inference:
`run ./run_neu_det.sh 1`

2. For Inference :
`run ./run_neu_det.sh 2`

NOTE : for inference move own Test Data under YOLOv6/test




