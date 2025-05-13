# mental-health-predictor

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : KUZIKKATIL ANAMIKA

*INTERN ID* : CT06WT245

*DOMAIN* : DATA SCIENCE

*DURATION* : 6 WEEKS

*MENTOR* : NEELA SANTOSH

Streamlit-based machine learning app for mental health condition predictior

This is a full-stack machine learning project that uses a trained model to predict mental health conditions based on user input.

##  Built with:

- Python & scikit-learn
- Streamlit frontend ('streamlit_app.py')
- Flask backend option ('app.py')
- CSV-based dataset & saved model

##  Features

- Trains a model using train_model.py
- Saves model as model.pkl
- Provides both API (app.py) and UI (streamlit_app.py)
- Accepts inputs like sleep hours, appetite loss, mood swings, etc.

##  How to Run (Streamlit UI)

pip install streamlit scikit-learn pandas
python train_model.py  # train and save model
streamlit run streamlit_app.py

## Description

In this project, I built a simple machine learning application that predicts mental health conditions based on user inputs such as sleep hours, appetite loss, fatigue, and mood swings. I started by training a Random Forest Classifier using a labeled dataset, then saved the model using Python’s pickle library. To make the model usable outside of a notebook, I created a Flask API that accepts user input through a POST request and returns a prediction. For a user-friendly experience, I also developed a Streamlit app that allows users to enter their symptoms using sliders and buttons. The Streamlit app sends the input to the trained model and displays a result like “Depression” or “No condition.” This project helped me understand the full machine learning workflow—from training a model to deploying it in a web interface. Technologies used include Python, scikit-learn, pandas, Flask, and Streamlit.


## Output

![Image](https://github.com/user-attachments/assets/beaf845c-38db-4d9d-af9a-80bca6e9f3e6)

