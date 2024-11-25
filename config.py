from dotenv import load_dotenv
from urllib.parse import quote_plus
from flask import Flask, request
import mysql.connector
import os


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS =os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_DATABASE_USER=os.getenv('SQLALCHEMY_DATABASE_USER')
    SQLALCHEMY_DATABASE_PASSWORD=os.getenv('SQLALCHEMY_DATABASE_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{SQLALCHEMY_DATABASE_USER}:{quote_plus(SQLALCHEMY_DATABASE_PASSWORD)}@localhost/sports-performance-pro-db"


