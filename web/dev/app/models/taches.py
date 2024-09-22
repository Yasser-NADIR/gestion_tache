from .. import db

class Tache(db.Model):
    __tablename__ = 'tache'

    id_tache = db.Column(db.Integer,primary_key=True,autoincrement=True)
    libelle_tache = db.Column(db.String(100),nullable=False)
    coefficient = db.Column(db.Integer,nullable=False)
    remarques = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f'<Tache {self.libelle_tache}>'