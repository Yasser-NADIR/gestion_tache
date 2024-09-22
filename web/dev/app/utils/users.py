from ..models.f_users import FUser
import time

def find_libelle_fuser_by_id(id):
    try:
        return FUser.query.get(id).libelle_famille
    except:
        return id

def libelle_famille_list():
    return [(user.id_f_user, user.libelle_famille) for user in FUser.query.all()]