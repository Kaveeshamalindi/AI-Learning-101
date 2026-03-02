import os
from dotenv import load_dotenv
from google import genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import render_template

#Load API key
load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("api_key")
client = genai.Client(api_key=API_KEY)

#Function to generate content
def generate(prompt):
    response = client.models.generate_content(
     model="gemini-3-flash-preview", contents=prompt
    )
    return response.text 

#Create Flask app
app = Flask(__name__)
CORS(app)

#Route to handle POST requests
@app.route('/generate', methods=['POST'])
def generate_route():
    data = request.json  # Get JSON from the request
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    result = generate(prompt)
    return jsonify({'result': result})

#show index.html when someone opens the website
@app.route('/')
def home():
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

