from flask import render_template
from app import app

@app.route('/')
def send_index():
    return render_template('index.html')

@app.route('/admin')
def send_admin():
    return render_template('admin.html')
