#!/bin/bash


configs=configs/yolov6s6_finetune.py
data_yaml=data/neu_det.yaml
testDir_root=test/
name=train_6s6_128_320_300

stage=${1:-0} # start from 0 if not specified in command line

#Finetuning step (training yolov6 with our datasets on top of coco-based weights)
if [ $stage -eq 0 ]; then
	 python  tools/train.py   --output-dir results \
	                          --name $name \
	                          --batch 32 \
	                          --img 576 \
							  --epochs 300 \
	                          --data $data_yaml \
                              --conf $configs \

fi 
#Evaluation on validation dataset

echo "-----------------------------Training finished. Starting evaluation...-----------------------------"

if [ $stage -eq 1 ]; then
	python3 tools/eval.py --batch 32 \
	                     --img 576 \
	                     --data $data_yaml \
	                     --weights results/$name/weights/best_ckpt.pt \
	                     --task val \
	                     --save_dir results \
	                     --name test_$name \
						 --plot_curve True \
						 --plot_confusion_matrix \
						 --verbose


fi

echo "----------------------------Evaluation finished. Starting inference...----------------------------"

#Inference on test dataset

if [ $stage -eq 2 ]; then
	python tools/infer.py --weights results/$name/weights/best_ckpt.pt \
	                      --source $testDir_root \
	                      --yaml $data_yaml \
	                      --save-txt \
	                      --project results \
	                      --name infer 
fi

echo "----------------------------Inference finished.----------------------------"