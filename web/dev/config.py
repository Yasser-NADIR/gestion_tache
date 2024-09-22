import os

class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:qwerty@db/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False