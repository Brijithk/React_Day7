import mysql.connector

class Database:

    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="clinic_management_system"
        )