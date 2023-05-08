#!/bin/bash


configs=configs/yolov6s_finetune.py
data_yaml=data/neu_det.yaml
testDir_root=test/

stage=${1:-0} # start from 0 if not specified in command line

#Finetuning step (training yolov6 with our datasets on top of coco-based weights)
if [ $stage -le 0 ]; then
	 python  tools/train.py   --output-dir results \
	                          --name train \
	                          --batch 256\
	                          --img 224 \
							  --epochs 300 \
	                          --data $data_yaml \
	                          --workers 20 \
                              --conf $configs \

fi 
#Evaluation on validation dataset

echo "-----------------------------Training finished. Starting evaluation...-----------------------------"

if [ $stage -le 1 ]; then
	python3 tools/eval.py --batch 256 \
	                     --img 224 \
	                     --data $data_yaml \
	                     --weights results/train_s_256_224_300/weights/best_ckpt.pt \
	                     --task val \
	                     --save_dir results \
	                     --name test \
						 --plot_curve True \
						 --plot_confusion_matrix \
						 --verbose


fi

echo "----------------------------Evaluation finished. Starting inference...----------------------------"

#Inference on test dataset

if [ $stage -le 2 ]; then
	python tools/infer.py --weights results/train_s_256_224_300/weights/best_ckpt.pt \
	                      --source $testDir_root \
	                      --yaml $data_yaml \
	                      --save-txt \
	                      --project results \
	                      --name infer 
fi

echo "----------------------------Inference finished.----------------------------"