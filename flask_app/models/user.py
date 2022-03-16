from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_register(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False 
            
