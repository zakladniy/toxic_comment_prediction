# toxic_comment_prediction


## Description

Simple Web-API based on FastAPI and deployed on Heroku service.

This Web-service provide to predict toxic or not toxic russian comments based on BERT model (model was trained with GPU, but for inference use PyTorch CPU version)

Project with model and API for predict toxic comments includes:
 - pipeline for create dataset
 - notebooks for EDA, model predicts interpretation
 - text preprocessing
 - pipeline for create model

### Dataset
Thanks [Alexander Semiletov](https://www.kaggle.com/alexandersemiletov) 
for [Toxic Russian Comments Dataset](https://www.kaggle.com/code/alexandersemiletov/starter-read-toxic-russian-comments-dataset)

There is no data in this repository. 
I was forced to remove them due to Heroku's size restrictions.
You can download the data from the link above, 
unzip it and put it in the cloned repository at data/raw and run workflow


### Model
Thanks [David Dale](https://huggingface.co/cointegrated) 
for pre-trained [tiny BERT-model](https://huggingface.co/cointegrated/rubert-tiny)

## Try Web API


## How to run application?
Clone repo:
  ```console 
    https://github.com/zakladniy/toxic_comment_prediction.git
  ```

### With poetry
Check poetry in you OS

Install with poetry
  ```console 
    poetry install
  ```

Activate env
  ```console 
    poetry shell
  ```

Run with:
  ```console 
    make run
  ```
### With docker

Create image:
  ```console 
    sudo docker build -t toxic_comment .
  ```
Run container:
  ```console 
    sudo docker run -p 80:80 -d toxic_comment
  ```
Open in browser url:
  ```console 
    http://127.0.0.1/docs
  ```

## Screenshots of application
### Common view
![](https://github.com/zakladniy/toxic_comment_predict/blob/main/screenshots/common_view_new.png)

### Request
![](https://github.com/zakladniy/toxic_comment_predict/blob/main/screenshots/request.png)

### Response
![](https://github.com/zakladniy/toxic_comment_predict/blob/main/screenshots/response.png)


## Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │── workflow           <- Workflow management, for creation reproducible and scalable data analyses
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── pyproject.toml   <- Poetry configuration
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    └── 


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
