from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

# Create New Ninja Page, Dojo location drop down menu with all location options
@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos= dojo.Dojo.get_all())

# Saves New Ninja Profile and redirects to home page
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')