from ..models import User, HDetTache, Tache

def get_nom_user_by_id(id):
    try:
        return User.query.get(id).nom
    except:
        return 'Undefined'

def get_all_nom_user():
    return [(user.id_users, user.nom) for user in User.query.all()]

def get_num_tache(id):
    try:
        return HDetTache.query.filter_by(id_h_l_ent_tache=id).count()
    except:
        return 'Undefined'
    
def get_nom_tache():
    return [(tache.id_tache, tache.libelle_tache) for tache in Tache.query.all()]
