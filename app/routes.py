from app import app
from flask import render_template, url_for

@app.route('/contact')
def contact():
    return render_template(url_for('contact'))