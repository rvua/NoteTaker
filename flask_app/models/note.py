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
        if len(form_data['title']) == 0:
            flash("Enter a title for the note")
            is_valid = False 
        if len(form_data['description']) < 2: 
            flash("Your description must be at least 2 characters long")
            is_valid = False
        return is_valid
        