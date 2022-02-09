from flask import render_template, request
from app import app

from . import db, models
from .forms import *
from .models import *


@app.route('/')
def index():
    # display homepage
    return render_template('index.html', title='Homepage')
