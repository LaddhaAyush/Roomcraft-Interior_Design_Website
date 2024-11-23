from flask import Flask, render_template, request, send_file, redirect, url_for, session
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient
from authlib.common.security import generate_token
from diffusers import StableDiffusionPipeline
from flask_cors import CORS
import os
import pickle
import hashlib
import base64
from io import BytesIO

app = Flask(__name__)


# Kinde configuration


# Load or pickle model function remains the same
model_path = "stable_diffusion_model.pkl"

def load_or_pickle_model():
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            pipe = pickle.load(f)
        print("Loaded model from pickle file.")
    else:
        print("Downloading model for the first time... This may take a while.")
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cpu")
        with open(model_path, 'wb') as f:
            pickle.dump(pipe, f)
        print("Model downloaded and saved for future use.")
    return pipe

pipe = load_or_pickle_model()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/wt')
def wt():
    return send_file('wt.html')

@app.route('/kitchen1')
def kitchen1():
    return send_file('kitchen1.html')

@app.route('/bedroom')
def bedroom():
    return send_file('bedroom.html')

@app.route('/index1')
def index1():
    return send_file('index1.html')

@app.route('/contact')
def contact():
    return send_file('contact.html')

@app.route('/about')
def about():
    return send_file('about_us.html')



if __name__ == '__main__':
    app.run(debug=True)
