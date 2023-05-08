
import os
import cv2
import matplotlib.pyplot as plt

def plot_image_with_labels(img_path, label_path):
    # Load image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Load labels
    with open(label_path, 'r') as f:
        labels = f.read().splitlines()
    
    classes = ['pitted_surface', 'rolled-in_scale',"scratches","crazing","inclusion","patches"]
        

    # Convert labels to bounding box coordinates
    for label in labels:
        class_id, x_center, y_center, width, height = map(float, label.split())
        x_min = int((x_center - width/2) * img.shape[1])
        y_min = int((y_center - height/2) * img.shape[0])
        x_max = int((x_center + width/2) * img.shape[1])
        y_max = int((y_center + height/2) * img.shape[0])
        
        class_id =  classes[int(class_id)]

        # Draw bounding box and label
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 1)
        cv2.putText(img, f'{class_id}', (x_min, y_min-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Show image
    plt.imshow(img)
    plt.show()

# Main
img_path = '/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/images/train/inclusion_22.jpg'
label_path = '/home/rayen/projects/NET_DET_YOLOV63/YOLOv6/data/labels/train/inclusion_22.txt'
plot_image_with_labels(img_path, label_path)
