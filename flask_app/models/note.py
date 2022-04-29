from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class Note:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.note = data['note']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_note(form_data):
        is_valid = True 
        