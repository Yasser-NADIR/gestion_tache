from .. import db

class User(db.Model):
    __tablename__ = 'users'
    id_users = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    id_f_user = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f'<User {self.nom}>'
    
