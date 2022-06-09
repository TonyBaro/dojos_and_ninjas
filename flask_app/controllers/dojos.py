from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/dojos')
def dojos():
    dojos = Dojo.retrieve_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/add_dojo' , methods=["POST"])
def add_dojo():
    data={
        'name':request.form['name']
    }
    Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_one_dojo(dojo_id):
    print ('DOJO ID IS',dojo_id)
    data={
        'dojo_id':dojo_id
    }
    one_dojo = Dojo.retrieve_dojo(data)
    return render_template('dojo.html' , dojo = one_dojo)
