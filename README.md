# air-pollution-be

## Introduction
Introducing our React Native Expo app, a dynamic solution that puts the power to combat air pollution in your hands. This innovative application not only helps you understand and monitor air quality but takes it a step further by providing personalized recommendations for action based on real-time pollution levels.

Powered by a robust backend using FastAPI and integrated machine learning and NLP (Natural Language Processing) capabilities, this app stands at the forefront of environmental technology. With the ability to predict the sources of air pollution, it not only informs you about the problem but also offers solutions. Whether it's suggesting lifestyle adjustments, environmental interventions, or regulatory measures, our app ensures you have the information you need to make a positive impact on air quality.

Experience a new era of environmental consciousness and control with our app, making clean air and a healthier planet a reality through data-driven insights and personalized recommendations.

This is Air Polution source prediction application

Create virtual envirment : python -m venv myenv

ACTIVATE VENV: source myenv/Scripts/activate

CONDA env: source C:/Users/Malith/anaconda3/Scripts/activate condamyenv

Create Requirment File: pip freeze > requirements.txt

requirement.text install: pip install -r requirements.txt

RUN SERVER: uvicorn index:app --reload

Test Api: http://localhost:8000/docs

kadawatha location : 8.311352,80.403651
Anuradhapura: 8.311352,80.403651
app psw: axsrbizmfuepylid

Mongodb Detaisl

password: oWfBHWmnl77NQYao

username: admin

How to deploy App in Gcloud
git clone
cd project-name
virtualenv env
source env/bin/activate
pip install -r requirements.txt
run app - gunicorn -w 4 -k uvicorn.workers.UvicornWorker index:app
