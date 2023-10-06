#!/bin/bash
#SBATCH --account=def-selouani
#SBATCH --gres=gpu:1       # Request GPU "generic resources"
#SBATCH --mem=32G       # Memory proportional to GPUs: 32000 Cedar, 64000 Graham.
#SBATCH --time=0-6:00
#SBATCH --output=output/%N-%j.out

module load python/3.8 scipy-stack gcc/9.3.0 cuda/11.4 opencv

source ENV/bin/activate


data_yaml="datasets/metatrain/neu_det.yaml"
batch_size=32
img_size=320
name=train_6l6-$batch_size-$img_size


python3 tools/eval.py --batch $batch_size \
                    --img $img_size \
                    --data $data_yaml \
                    --weights results/$name/weights/best_ckpt.pt \
                    --task val \
                    --save_dir results \
                    --name eval_$name \
                    --plot_curve True \
                    --plot_confusion_matrix \
                    --verbose

