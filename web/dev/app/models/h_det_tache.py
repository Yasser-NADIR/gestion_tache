from .. import db

class HDetTache(db.Model):
    __tablename__ = 'h_det_tache'

    id_h_det_tache = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_h_l_ent_tache = db.Column(db.Integer, nullable=False)
    id_tache = db.Column(db.Integer, nullable=False)
    h_debut = db.Column(db.Time, nullable=False, default='00:01:00.000000')
    h_fin = db.Column(db.Time, nullable=False, default='23:59:00.000000')
    temps_diff = db.Column(db.Integer, nullable=False)
    coefficient = db.Column(db.Integer, nullable=False)
    prix_calc = db.Column(db.Integer, nullable=False)
    remarques = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<HDetTache {self.id_h_det_tache}>'