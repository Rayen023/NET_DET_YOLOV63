# NET_DET_YOLOV63

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

### Converting from xml format to YOLO format : 

=============================================================

NOTE : Some changes to file direcories, class names MIGHT need to be added

1. run convert_voc_to_yolo.py file :
`python convert_voc_to_yolo.py`

2. Create .yaml file
example : 
```
train: "/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/images/train"
val: "/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/images/validation"

nc: 6
names: ['pitted_surface', 'rolled-in_scale',"scratches","crazing","inclusion","patches"]
```

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




