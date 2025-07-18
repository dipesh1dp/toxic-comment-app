# Training Report
THe [bert-base-uncased](https://huggingface.co/bert-base-uncased) was fine-tuned on the jigsaw-toxic-comment-classification-challenge dataset using 
Huggingface Trainer.

Training was tracked with [Weights & Biases](https://wandb.ai/) to ensure transparency, reproducibility, and in-depth performance analysis.

👉 [Click here to view the full wandb run report](https://api.wandb.ai/links/dipesh1dp-purwanchal-campu/c682p62i)


## Training procedure
**Training Hardware**: Trained on Kaggle using `NVIDIA TESLA P100` GPU

**Training and evaluation data**:
[jigsaw-toxic-comment-classification-challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data)
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: `2e-05`
- train_batch_size: `16`
- eval_batch_size: `32`
- seed: `42`
- optimizer: Use `OptimizerNames.ADAMW_TORCH` with `betas=(0.9,0.999)` and `epsilon=1e-08` and `optimizer_args=No additional optimizer arguments`
- lr_scheduler_type: `linear`
- num_epochs: `5`
- mixed_precision_training: `Native AMP`

### Training results
| Training Loss | Epoch | Step  | Validation Loss | Micro F1 | Macro F1 | Precision | Recall | Hamming Loss | Roc Auc Macro | Roc Auc Micro |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:---------:|:------:|:------------:|:-------------:|:-------------:|
| 0.0411        | 1.0   | 8976  | 0.0386          | 0.7857   | 0.6324   | 0.6794    | 0.6379 | 0.0159       | 0.9885        | 0.9919        |
| 0.0333        | 2.0   | 17952 | 0.0392          | 0.7951   | 0.6788   | 0.6934    | 0.6749 | 0.0155       | 0.9883        | 0.9917        |
| 0.0248        | 3.0   | 26928 | 0.0443          | 0.7855   | 0.6910   | 0.6312    | 0.7756 | 0.0170       | 0.9891        | 0.9912        |
| 0.016         | 4.0   | 35904 | 0.0521          | 0.7845   | 0.6912   | 0.6584    | 0.7295 | 0.0163       | 0.9875        | 0.9892        |
| 0.0101        | 5.0   | 44880 | 0.0585          | 0.7818   | 0.6879   | 0.6583    | 0.7228 | 0.0164       | 0.9860        | 0.9879        |

### Model Evaluation
## Per Label Threshold
| Label ID | Label Name     | Optimal Threshold   | F1 Score (Validation)   |
| -------- | -------------- | --------------------| ----------------------- |
| 0        | toxic          | `0.69`              | `0.8264`                |
| 1        | severe\_toxic  | `0.44`              | `0.5238`                |
| 2        | obscene        | `0.60`              | `0.8321`                |
| 3        | threat         | `0.47`              | `0.6316`                |
| 4        | insult         | `0.32`              | `0.7713`                |
| 5        | identity\_hate | `0.55`              | `0.6280`                |

## Model Performance on Test Set
| Metric                | Value    |
| --------------------- | -------- |
| **F1 Score (Micro)**  | `0.6740` | 
| **F1 Score (Macro)**  | `0.6089` | 
| **Precision (Micro)** | `0.5857` | 
| **Recall (Micro)**    | `0.7938` | 
| **Precision (Macro)** | `0.5426` | 
| **Recall (Macro)**    | `0.7092` |



### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1