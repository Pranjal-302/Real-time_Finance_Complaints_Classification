from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load your trained model
model = joblib.load('./models/best_model.joblib')  # Replace with your actual model filename

# Load the TfidfVectorizer used during training
vectorizer = joblib.load('./models/vectorizer.joblib')  # Replace with your actual vectorizer filename

encoder = joblib.load('./models/label_encoder.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text input from the HTML form
        text = request.form['text']

        # Vectorize the input text using the same TfidfVectorizer used during training
        text_vectorized = vectorizer.transform([text])

        # Make predictions
        prediction = model.predict(text_vectorized)[0]
#         score = model.predict_proba(text_vectorized)[0]
#         score = [round(float(num),3) for num in score]
        new = encoder.inverse_transform([prediction])[0]
#         raw = f"{score} {new}"
        # Return the prediction as JSON
        return render_template('index.html', prediction=new)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
