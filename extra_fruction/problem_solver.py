import secrets
import string

def frind_list(arr1, arr2):
   
   
    # user is the frind1 in arr1 and  user is the friend2 in arr2
    frd_list = []
    for single_frd_obj in arr1:
        frd_profile_profile = single_frd_obj.friend_two
        profile_data = {
            "user_id": frd_profile_profile.user.id,
            "profile_id": frd_profile_profile.id,
            "name": f"{frd_profile_profile.user.first_name} { frd_profile_profile.user.last_name}",
            "profile_pic": frd_profile_profile. profile_picture,
        }
        frd_list.append(profile_data)

    for single_frd_obj in arr2:
        frd_profile_profile = single_frd_obj.friend_one
        profile_data = {
            "user_id": frd_profile_profile.user.id,
            "profile_id": frd_profile_profile.id,
            "name": f"{frd_profile_profile.user.first_name} { frd_profile_profile.user.last_name}",
            "profile_pic": frd_profile_profile. profile_picture,
        }
        frd_list.append(profile_data)
    # Sort the list of dictionaries by the "name" key
    ar_sorted = sorted(frd_list, key=lambda x: x["name"])
    return ar_sorted





def generate_token(length=30):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
