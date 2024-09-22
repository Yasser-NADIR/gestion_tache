from . import db

class FUser(db.Model):
    id_f_user = db.Column(db.Integer, primary_key=True)
    libelle_famille = db.Column(db.String(100), nullable=False)
    coefficient = db.Column(db.Integer, nullable=False)
    remarques = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<FUser {self.libelle_famille}'