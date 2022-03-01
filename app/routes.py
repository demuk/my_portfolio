from app import app
from flask import render_template, url_for, request, redirect


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/home')
def home():
    return render_template('home.html')
