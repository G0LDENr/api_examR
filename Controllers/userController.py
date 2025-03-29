from Models.User import User
from flask import jsonify
from config import db
from flask_jwt_extended import create_access_token

def get_all_users():
    try:
        users = [user.to_dict() for user in User.query.all()]
        return jsonify(users), 200
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({'msg': 'Error al obtener usuarios'}), 500

def create_user(name, email, password):
    try:
        if User.query.filter_by(email=email).first():
            return jsonify({'msg': 'El email ya existe'}), 400
            
        new_user = User(name=name, email=email)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        print(f"ERROR: {e}")
        return jsonify({'msg': 'Error al crear usuario'}), 500

def login_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            return jsonify({'msg': 'Credenciales inválidas'}), 401
            
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'access_token': access_token,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({'msg': 'Error en el servidor'}), 500