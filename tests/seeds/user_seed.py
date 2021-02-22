
def user_noob_object():
    return {
        'email': 'harmylarry20@gmail.com',
        'password': 'harmydiano',
        'currency': 'naira',
        'user_type': 'noob',
        'access': {
            "noob": True,
            "elite": False,
            "admin": False
        }
    }

def user_elite_object():
    return {
        'email': 'harmylarry20@gmail.com',
        'password': 'harmydiano',
        'currency': 'naira',
        'user_type': 'elite',
        'access': {
            "noob": False,
            "elite": True,
            "admin": False
        }
    }

def user_admin_object():
    return {
        'email': 'harmylarry20@gmail.com',
        'password': 'harmydiano',
        'currency': 'naira',
        'user_type': 'admin',
        'access': {
            "noob": False,
            "elite": False,
            "admin": True
        }
    }