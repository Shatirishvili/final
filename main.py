from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ragacavakho'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f"username: {self.username} / password: {self.password} /"

db.create_all()


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if u == '' or p == '':
            flash("Something wrong")
        else:
            user1 = Users(username=u, password=p)
            db.session.add(user1)
            db.session.commit()
            return redirect(url_for('enter'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if u == '' or p == '':
            flash("Something wrong")
        else:
            user1 = Users(username=u, password=p)
            db.session.add(user1)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/enter', methods=['POST', 'GET'])
def enter():
    return render_template('enter.html')


if __name__ == '__main__':
    app.run(debug=True)