from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Terminal: pip3 install -U Flask-SQLAlchemy
from flask_bootstrap import Bootstrap
# Terminal: pip3 install flask-bootstrap


app = Flask(__name__)
app.app_context().push()
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chores.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Chores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), unique=True, nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)


db.create_all()


@app.route("/")
def home():
    all_chores = db.session.query(Chores).all()
    return render_template('index.html', chores=all_chores)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_chore = Chores(
            description=request.form["description"],
            frequency=request.form["frequency"],
            date=request.form["date"]
        )
        db.session.add(new_chore)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("log_chores.html")

