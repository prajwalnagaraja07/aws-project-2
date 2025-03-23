# Udacity-AWS-ML-project-2
This is my submission to the AWS Machine Learning nanodegree  - project 2

## Project structure
Main Python notebook for the project is named [`starter.ipynb`](./starter.ipynb)

AWS lambda functions are in three python files: 
* [`serializeImageData.py`](./lambda1-serializeImageData.py),
* [`classifyimageData.py`](./lambda2-ImageClassify.py),
* [`filterLowConfidence.py`](./lambda3-filterLowConfidence.py)

Step function code file: [`stateMachine.json`](./step-function.json). Graph:

![stateMachine](./step-function-working.png)

