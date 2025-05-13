import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit UI
st.title("🧠 Mental Health Condition Predictor")
st.write("Enter your health indicators below:")

# Input form
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, value=6)
appetite_loss = st.selectbox("Appetite Loss", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
fatigue = st.slider("Fatigue Level", min_value=0, max_value=10, value=2)
mood_swings = st.selectbox("Mood Swings", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Predict button
if st.button("Predict"):
    input_data = [[sleep_hours, appetite_loss, fatigue, mood_swings]]
    prediction = model.predict(input_data)
    st.success(f"🧾 Predicted Condition: **{prediction[0]}**")
