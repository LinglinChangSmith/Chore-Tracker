from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Terminal: pip3 install -U Flask-SQLAlchemy
from flask_bootstrap import Bootstrap
# Terminal: pip3 install flask-bootstrap


app = Flask(__name__)
app.app_context().push()
Bootstrap(app)

