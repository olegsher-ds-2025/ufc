from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('manifest.html')