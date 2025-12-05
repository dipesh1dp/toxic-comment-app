# Training Report
The [bert-base-uncased](https://huggingface.co/bert-base-uncased) and [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) were fine-tuned on the jigsaw-toxic-comment-classification-challenge dataset using Huggingface Trainer. \
Bert Training was tracked with [Weights & Biases](https://wandb.ai/) to ensure transparency, reproducibility, and in-depth performance analysis.

👉 [Click here to view the full wandb run report](https://api.wandb.ai/links/dipesh1dp-purwanchal-campu/c682p62i)



👉 [Click here to view the Bert model at HuggingFace](https://huggingface.co/dipeshpandit/bert-toxic) \
👉 [Click here to view the Distilbert model (chosen model) at HuggingFace](https://huggingface.co/dipeshpandit/distilbert-toxic-comment)



## Training procedure
**Training Hardware**: \
Bert Model trained on Kaggle using `NVIDIA TESLA P100` GPU \
Distilbert Model trained on Modal using `NVIDIA H100` GPU

**Training and evaluation data**:
[jigsaw-toxic-comment-classification-challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data)
### Training hyperparameters

| **Hyperparameter**              | **BERT Model**                                   | **DistilBERT Model**                             |
|---------------------------------|--------------------------------------------------|--------------------------------------------------|
| **Learning Rate**               | `2e-05`                                          | `3.2719182895564304e-05` (Tuned)                 |  
| **Train Batch Size**            | `16`                                             | `64` (Tuned)                                     |
| **Eval Batch Size**             | `32`                                             | `32`                                             |
| **Seed**                        | `42`                                             | `42`                                             |
| **Optimizer**                   | `ADAMW`                                          | `ADAMW`                                          |
| **Weight Decay**                | `0.01`                                           |  `0.023377366840031614` (Tuned)                  |
| **LR Scheduler Type**           | `linear`                                         | `linear`                                         |
| **Number of Epochs**            | `5`                                              | `5`                                              |
| **Mixed Precision Training**    | `Native AMP`                                     | `Native AMP`                                     |


## Training results
### BERT Model
| Training Loss | Epoch | Step  | Validation Loss | Micro F1 | Macro F1 | Precision | Recall | Hamming Loss | Roc Auc Macro | Roc Auc Micro |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:---------:|:------:|:------------:|:-------------:|:-------------:|
| 0.0411        | 1.0   | 8976  | 0.0386          | 0.7857   | 0.6324   | 0.6794    | 0.6379 | 0.0159       | 0.9885        | 0.9919        |
| 0.0333        | 2.0   | 17952 | 0.0392          | 0.7951   | 0.6788   | 0.6934    | 0.6749 | 0.0155       | 0.9883        | 0.9917        |
| 0.0248        | 3.0   | 26928 | 0.0443          | 0.7855   | 0.6910   | 0.6312    | 0.7756 | 0.0170       | 0.9891        | 0.9912        |
| 0.016         | 4.0   | 35904 | 0.0521          | 0.7845   | 0.6912   | 0.6584    | 0.7295 | 0.0163       | 0.9875        | 0.9892        |
| 0.0101        | 5.0   | 44880 | 0.0585          | 0.7818   | 0.6879   | 0.6583    | 0.7228 | 0.0164       | 0.9860        | 0.9879        |

### DistilBERT Model
| Training Loss | Epoch | Step  | Validation Loss | Macro F1 | Micro F1 | Precision | Recall | Hamming Loss | Roc Auc Macro | Roc Auc Micro |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:---------:|:------:|:------------:|:-------------:|:-------------:|
| 0.0402        | 1.0   | 2244  | 0.0387          | 0.6473   | 0.7850   | 0.6806    | 0.6427 | 0.0160       | 0.9901        | 0.9920        |
| 0.0336        | 2.0   | 4488  | 0.0385          | 0.6798   | 0.7912   | 0.6727    | 0.6974 | 0.0161       | 0.9898        | 0.9924        |
| 0.0259        | 3.0   | 6732  | 0.0414          | 0.6896   | 0.7872   | 0.6520    | 0.7360 | 0.0165       | 0.9900        | 0.9918        |
| 0.0199        | 4.0   | 8976  | 0.0463          | 0.6761   | 0.7852   | 0.6525    | 0.7041 | 0.0165       | 0.9887        | 0.9905        |
| 0.0151        | 5.0   | 11220 | 0.0510          | 0.6969   | 0.7858   | 0.6672    | 0.7298 | 0.0163       | 0.9885        | 0.9900        |



## Model Evaluation
### Per Label Optimal Threshold (BERT)
| Label ID | Label Name     | Threshold (BERT) | Val F1 Score (BERT) | Threshold (DistilBERT) | Val F1 Score (DistilBERT) |
| -------- | -------------- | -----------------| ------------------- | -----------------------| ------------------------- |
| 0        | toxic          | `0.69`           |   `0.8264`          | `0.57`                 |   `0.8312`                |
| 1        | severe\_toxic  | `0.44`           |   `0.5238`          | `0.30`                 |   `0.5564`                |
| 2        | obscene        | `0.60`           |   `0.8321`          | `0.49`                 |   `0.8383`                |
| 3        | threat         | `0.47`           |   `0.6316`          | `0.39`                 |   `0.6275`                |
| 4        | insult         | `0.32`           |   `0.7713`          | `0.36`                 |   `0.7636`                |
| 5        | identity\_hate | `0.55`           |   `0.6280`          | `0.37`                 |   `0.6179`                |

### Per Label Threshold (DistilBERT)



## Model Performance on Test Set (BERT vs DistilBERT)
| Metric                | Value (BERT Model) | Value (DistilBERT Model) |
| --------------------- | ------------------ | ------------------ |
| **F1 Score (Micro)**  |      `0.6740`      |      `0.6668`      | 
| **F1 Score (Macro)**  |      `0.6089`      |      `0.6083`      | 
| **Precision (Micro)** |      `0.5857`      |      `0.5642`      | 
| **Recall (Micro)**    |      `0.7938`      |      `0.8152`      | 
| **Precision (Macro)** |      `0.5426`      |      `0.5264`      | 
| **Recall (Macro)**    |      `0.7092`      |      `0.7475`      |

