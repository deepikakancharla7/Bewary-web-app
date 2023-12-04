# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Database Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    brewery_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Routes and Views
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        city = request.form.get('city')
        # Implement Open Brewery API search logic here and pass data to template
        return render_template('search_results.html', breweries=[])  # Pass brewery data here

    return render_template('search.html')


@app.route('/brewery/<brewery_id>', methods=['GET', 'POST'])
@login_required
def brewery_detail(brewery_id):
    # Implement Open Brewery API details logic here and pass data to template

    if request.method == 'POST':
        rating = int(request.form.get('rating'))
        description = request.form.get('description')
        review = Review(rating=rating, description=description, brewery_id=brewery_id, user_id=current_user.id)
        db.session.add(review)
        db.session.commit()
        flash('Review added successfully!', 'success')

    reviews = Review.query.filter_by(brewery_id=brewery_id).all()
    return render_template('brewery_detail.html', reviews=reviews)  # Pass brewery and reviews data here


# Run the application
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
