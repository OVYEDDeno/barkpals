"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Owner
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
        raise APIException("User not found", 404)
    db.session.delete(owner)
    db.session.commit()
    return jsonify({'message': f'Owner{owner.id} was deleted'}), 201