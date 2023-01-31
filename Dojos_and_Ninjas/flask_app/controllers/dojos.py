from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

# Home page, with New Dojo and All Dojos list
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos) 

# Create Dojos, should save the new dojo to the list of All Dojos
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

# Link to page that displays all the students at the selected Dojo Location
@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    return render_template('dojo.html', dojo = Dojo.get_ninja(data))