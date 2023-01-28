"""Flask app for Cupcakes"""
from flask import Flask, render_template, session, redirect, request, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from serialized import seririalized
# import datetime

app = Flask(__name__)


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cows'
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/api/cupcakes', methods=['POST', 'GET'])
def get_all_cupcakes():
    if request.method == 'POST':
        flavor = request.json['flavor']
        size = request.json['size']
        rating = request.json['rating']
        image = request.json['image']
        print(flavor)
        print(size)
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(new_cupcake)
        db.session.commit()
        return jsonify({'flavor': flavor, 'size':size, 'rating':rating, 'image': image})
  
    else:
        
        cupcakes = Cupcake.query.all()
        print(cupcakes)
        total_cupcakes = []
        for cupcake in cupcakes:
            print(cupcake)
            serial = seririalized(cupcake)
            total_cupcakes.append(serial)
    
        print(total_cupcakes)
        return jsonify(total_cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH', 'GET', 'DELETE'])
def get_single_cupcake(cupcake_id):
    if request.method == 'PATCH':
        single_cupcake = Cupcake.query.get(cupcake_id)
        flavor = request.form['flavor']
        size = request.form['size']
        rating = request.form['rating']
        image = request.form['image']

        if flavor != "":
            single_cupcake.flavor = flavor
            return single_cupcake
        if size != "":
            single_cupcake.size = size
            return single_cupcake
        if rating != "":
            single_cupcake.rating = rating
            return single_cupcake
        if image != "":
            single_cupcake.image = image
            return single_cupcake
        
        db.session.add(single_cupcake)
        db.session.commit()
        return jsonify(seririalized(single_cupcake))
    elif request.method == 'DELETE':
        Cupcake.query.filter_by(id=cupcake_id).delete()
        return jsonify({'cupcake': 'has been deleted'})
    else:
  
  
        print(cupcake_id)
        single_cupcake = Cupcake.query.get(cupcake_id)
        serial = seririalized(single_cupcake)
        print(serial)
        return jsonify(serial)