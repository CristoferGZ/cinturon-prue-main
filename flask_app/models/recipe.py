from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, flash 
import re


class Recipe:
    db_name = 'certificacion'

    def __init__(self,db_data):
        self.id = db_data.get['id']
        self.name = db_data.get['name']
        self.status = db_data.get['status']
        self.created_at = db_data.get['created_at']
        self.updated_at = db_data.get['updated_at']
        self.user_id = db_data.get['user_id']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO appointments (`name`,`status`,`date_made`,`created_at`,`updated_at`,`user_id`)
        VALUES (%(name)s, %(status)s, %(date_made)s, NOW(), NOW(),%(user_id)s)
        """
        return connectToMySQL("esquema_citas").query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL("esquema_citas").query_db(query)
        all_recipes = []
        for row in results:
            print(row['date_made'])
            all_recipes.append( cls(row) )
        return all_recipes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("esquema_citas").query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under30=%(under30)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("esquema_citas").query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("esquema_citas").query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        return is_valid
