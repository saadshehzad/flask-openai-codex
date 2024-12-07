from flask import Flask, render_template, request, jsonify
import openai
from .config import openai_api_key

app = Flask(__name__)


app.route('/')
def index():
    return render_template()