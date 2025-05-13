from flask import Flask, request, jsonify
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Mental Health Prediction API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Received JSON:", data)
    input_values = [data['sleep_hours'], data['appetite_loss'], data['fatigue'], data['mood_swings']]
    prediction = model.predict([input_values])
    return jsonify({'prediction': str(prediction[0])})


if __name__ == "__main__":
    app.run(debug=True)

