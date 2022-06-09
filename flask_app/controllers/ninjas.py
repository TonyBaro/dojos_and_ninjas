from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/ninja')
def ninja():
    dojos = Dojo.retrieve_dojos()
    return render_template('ninja.html', dojos = dojos)

@app.route('/add_ninja', methods = ['POST'])
def add_ninja():
    data = {
        'id':request.form['city'],
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age']
    }
    Ninja.add_ninja(data)
    return redirect("/dojos")