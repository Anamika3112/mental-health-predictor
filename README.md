# mental-health-predictor
Streamlit-based machine learning app for mental health condition predictior

This is a full-stack machine learning project that uses a trained model to predict mental health conditions based on user input.

Built with:
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

