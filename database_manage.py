import datetime

from initialize_firebase import initialize
from datetime import datetime

firebase = initialize()

db = firebase.database()


def get_all_ids():
    """
    Get all the birth registration ids.
    :return: List of all ids in integer
    """
    ids = db.child("births").shallow().get().val()
    ids = list(ids)
    ids = [int(i) for i in ids]
    ids.sort()
    return ids


def set_data(name,
             date_of_birth,
             father_name,
             mother_name,
             guardian_contact_number,
             birth_location,
             guardian_nid,
             address):


    data = {"name": f"{name}",
            "date_of_birth": f"{date_of_birth}",
            "father_name": f"{father_name}",
            "mother_name": f"{mother_name}",
            "guardian_contact_number": f"{guardian_contact_number}",
            "birth_location": f"{birth_location}1",
            "guardian_nid": f"{guardian_nid}",
            "address": f"{address}",
            "created_at": f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            "updated_at": f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
            }
    return data

def get_last_child_id():
    ids = db.child("births").shallow().get().val()

    if ids:
        last_id = [int(i) for i in db.child("births").shallow().get().val()]
        last_id.sort()
        return last_id[-1]
    else:
        return 0

def push_data(root="births", data=None):
    last_child_id = int(get_last_child_id())
    last_child_id += 1
    db.child(root).child(f"{last_child_id}").set(data)


# push_data(data={"name": "n1", "age": "10"})

def get_data_by_child_id(child_id):
    data = db.child("births").child(f"{child_id}").get().val()
    return data

def retrieve_all_data():
    # child_keys = db.child("births").shallow().get().val()
    # rows = [db.child("births").child(child_key).get().val() for child_key in child_keys]
    # data_list = [{**row} for row in rows]

    ids = get_all_ids()
    data_list = [get_data_by_child_id(i) for i in ids]

    return data_list


def update_data(root="births", child_id=None, data=None):
    current_data = get_data_by_child_id(child_id)

    db.child(root).child(f"{child_id}").set(data)







# update_data(child_id=1, data={"name": "name1",
#             "date_of_birth": "date_of_birth1",
#             "father_name": "father_name1",
#             "mother_name": "mother_name1",
#             "guardian_contact": "guardian_contact1",
#             "birth_location": "birth_location1",
#             "guardian_nid": "guardian_nid1",
#             "created_at": f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
#             "updated_at": f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
#             })




