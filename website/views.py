from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if not name or not message:
            flash("All fields are required.", category='error')
        else:
            flash("Message sent successfully!", category='success')
            return redirect(url_for('views.contact'))

    return render_template('contact.html')
