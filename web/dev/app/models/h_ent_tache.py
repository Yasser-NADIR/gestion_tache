from .. import db

class HEntTache(db.Model):
    __tablename__ = 'h_ent_tache'

    id_h_ent_tache = db.Column(db.Integer,primary_key=True,autoincrement=True)
    libelle_journee = db.Column(db.String(100),nullable=False)
    id_users = db.Column(db.Integer,nullable=False)
    date_operation = db.Column(db.Date,nullable=False)
    remarques = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f'<HEntTache {self.libelle_journee}>'