# Udacity-AWS-ML-project-2
This is my submission to the AWS Machine Learning nanodegree  - project 2

## Project structure
Main Python notebook for the project is named [`starter.ipynb`](./starter.ipynb)

AWS lambda functions are in three python files: 
* [`serializeImageData.py`](./lambda1-serializeImgaeData.py),
* [`classifyimageData.py`](./lambda2-ImageClassify.py),
* [`filterLowConfidence.py`](./lambda3-filterLowConfidence.py)

Step function code file: [`stateMachine.json`](./step-function.json). Graph:

![stateMachine](./step-function-working.png)
![stateExecution](./state-execution.png)
![stateExecution](./state-success.png)
![stateExecution](./state-failure.png)
