from initialize_firebase import initialize
import os

firebase = initialize()
storage = firebase.storage()

def download():
    all_files = storage.list_files()

    for file in all_files:
        print(file.name)
        if file.name.endswith(".png") or file.name.endswith(".jpg") or file.name.endswith(".jpeg"):
            # storage.child(file.name).download(filename=file.name, path="firebase_images")
            file.download_to_filename(f"firebase_images/{file.name}")

def call():
    try:
        download()
    except:
        pass


if __name__ == "__main__":
    call()





