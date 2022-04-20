from flask import Flask, render_template
from controllers.book_controller import *
app = Flask(__name__)
app.register_blueprint(book_blueprint)