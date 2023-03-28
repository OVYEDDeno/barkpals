"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Owner, Dogs, Breeds, Playdates, Message
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/owner', methods=['POST'])
def handle_owner():
    request_body = request.get_json()
    # owner=Owner.query.get(request_body['name'])
    new_owner=Owner(
        name=request_body['name'],
        img_url = request_body['img_url'],
        zipcode = request_body['zipcode'],
        email = request_body['email'],
        password = request_body['password'],)
    db.session.add(new_owner)
    db.session.commit()
    return jsonify(new_owner.serialize()), 200
@api.route('/owner/<int:owner_id>', methods=['GET'])
def get_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner is None:
        return jsonify({'message': 'Owner not found'}), 404
    return jsonify(owner.serialize()), 200

@api.route('/owners', methods=['GET'])
def get_all_owner():
    owner_list = Owner.query.all()
    owner_serialized = [owner.serialize() for owner in owner_list]
    if owner_list is None:
        return jsonify({'message': 'Owner not found'}), 404
    return jsonify(owner_serialized), 200

@api.route('/owner/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id):
    owner = Owner.query.get(owner_id)
    if owner is None:
        return jsonify({'message': 'Owner not found'}), 404
    request_body = request.get_json()
    owner.name = request_body.get('name', owner.name)
    owner.img_url = request_body.get('img_url', owner.img_url)
    owner.zipcode = request_body.get('zipcode', owner.zipcode)
    owner.email = request_body.get('email', owner.email)
    owner.password = request_body.get('password', owner.password)
    db.session.commit()
    return jsonify(owner.serialize()), 200
    
@api.route('/owner/<int:id>', methods=['DELETE'])
def delete_owner(id):
    owner = Owner.query.get(id)
    if owner is None:
        raise APIException("Owner not found", 404)
    db.session.delete(owner)
    db.session.commit()
    return jsonify({'message': f'Owner{owner.id} was deleted'}), 201
 

# DOGS LINE START HERE
@api.route('/dogs', methods=['POST'])
def handle_dogs():
    request_body = request.get_json()
    new_dog=Dog(
        name=request_body['name'],
        img_url=request_body['img_url'],
        breed=request_body['breed'],
        chip_number=request_body['chip_number'],
        weight=request_body['weight'],
        neutered_or_spayed=request_body['neutered_or_spayed'],
        dog_id=request_body['dog_id'],)
    db.session.add(new_dog)
    db.session.commit()
    return jsonify(new_dog.serialize()), 200

@api.route('/dogs', methods=['GET'])
def get_all_dogs():
    dogs_list = Dogs.query.all()
    dogs_serialized = [dogs.serialize() for dogs in dogs_list]
    if dogs_list is None:
        return jsonify({'message': 'Dogs not found'}), 404
    return jsonify(dogs_serialized), 200

@api.route('/dogs/<int:dog_id>', methods=['GET'])
def get_dog(dog_id):
    dog = Dog.query.get(dog_id)
    if dog is None:
        return jsonify({'message': 'Dog not found'}), 404
    return jsonify(dog.serialize()), 200

@api.route('/dogs/<int:dog_id>', methods=['PUT'])
def update_dog(dog_id):
    dog = Dogs.query.get(dog_id)
    if dog is None:
        return jsonify({'message': 'Dog not found'}), 404
    request_body = request.get_json()
    dog.name = request_body.get('name', dog.name)
    dog.img_url = request_body.get('img_url', dog.img_url)
    dog.zipcode = request_body.get('zipcode', dog.zipcode)
    dog.email = request_body.get('email', dog.email)
    dog.password = request_body.get('password', dog.password)
    db.session.commit()
    return jsonify(dog.serialize()), 200
    
@api.route('/dogs/<int:id>', methods=['DELETE'])
def delete_dog(id):
    dog = Dogs.query.get(id)
    if dog is None:
        raise APIException("Dog not found", 404)
    db.session.delete(dog)
    db.session.commit()
    return jsonify({'message': f'Dogs{dog.id} was deleted'}), 201

# BREEDS LINE START HERE
@api.route('/breeds', methods=['POST'])
def handle_breeds():
    request_body = request.get_json()
    # owner=Owner.query.get(request_body['name'])
    new_breeds=Breeds(
        name=request_body['name'],
        img_url = request_body['img_url'],
        zipcode = request_body['zipcode'],
        email = request_body['email'],
        password = request_body['password'],)
    db.session.add(new_breeds)
    db.session.commit()
    return jsonify(new_breeds.serialize()), 200
@api.route('/breeds/<int:breeds_id>', methods=['GET'])
def get_breeds(breeds_id):
    breeds = breeds.query.get(breeds_id)
    if breeds is None:
        return jsonify({'message': 'Breeds not found'}), 404
    return jsonify(breeds.serialize()), 200

@api.route('/breeds/<int:breeds_id>', methods=['PUT'])
def update_breeds(breeds_id):
    breeds = Breeds.query.get(breeds_id)
    if breeds is None:
        return jsonify({'message': 'Breeds not found'}), 404
    request_body = request.get_json()
    breeds.name = request_body.get('name', breeds.name)
    breeds.img_url = request_body.get('img_url', breeds.img_url)
    breeds.zipcode = request_body.get('zipcode', breeds.zipcode)
    breeds.email = request_body.get('email', breeds.email)
    db.session.commit()
    return jsonify(breeds.serialize()), 200
    
@api.route('/breeds/<int:breeds_id>', methods=['DELETE'])
def delete_breeds(id):
    breeds = Breeds.query.get(id)
    if breeds is None:
        raise APIException("Breeds not found", 404)
    db.session.delete(breeds)
    db.session.commit()
    return jsonify({'message': f'breeds{breeds.id} was deleted'}), 201

# PLAYDATES LINE START HERE
@api.route('/playdates' , methods=['POST'])
def Playdates():
    request_body = request.get_json()
    # owner=Owner.query.get(request_body['name'])
    new_playdate=Playdates(
        dog1_id=request_body['dog1_id'],
        dog2_id = request_body['dog2_id'],
        owner1_id=request_body['owner1_id'],
        owner2_id = request_body['owner2_id'],
        messages = request_body['messages'],)
    db.session.add(new_playdate)
    db.session.commit()
    return jsonify(new_playdate.serialize()), 200

# @api.route('/playdates/<int:breeds_id>', methods=['GET'])
# def get_breeds(breeds_id):
#     breeds = breeds.query.get(breeds_id)
#     if breeds is None:
#         return jsonify({'message': 'Breeds not found'}), 404
#     return jsonify(breeds.serialize()), 200

# @api.route('/breeds/<int:breeds_id>', methods=['PUT'])
# def update_breeds(breeds_id):
#     breeds = Breeds.query.get(breeds_id)
#     if breeds is None:
#         return jsonify({'message': 'Breeds not found'}), 404
#     request_body = request.get_json()
#     breeds.name = request_body.get('name', breeds.name)
#     breeds.img_url = request_body.get('img_url', breeds.img_url)
#     breeds.zipcode = request_body.get('zipcode', breeds.zipcode)
#     breeds.email = request_body.get('email', breeds.email)
#     db.session.commit()
#     return jsonify(breeds.serialize()), 200
    
# @api.route('/breeds/<int:breeds_id>', methods=['DELETE'])
# def delete_breeds(id):
#     breeds = Breeds.query.get(id)
#     if breeds is None:
#         raise APIException("Breeds not found", 404)
#     db.session.delete(breeds)
#     db.session.commit()
#     return jsonify({'message': f'breeds{breeds.id} was deleted'}), 201