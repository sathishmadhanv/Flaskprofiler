from flask import url_for,redirect,render_template,request
from PIL import Image

import glob

def base():
    return render_template('base.html') 
def exper():
    return render_template('experience.html') 
def c():
    return render_template('certificates.html') 
def pp():
    return render_template('personalprojects.html') 
def skills():
    return render_template('skills.html') 
def index():
    return render_template('index.html')
def about():
    return render_template('about.html')



