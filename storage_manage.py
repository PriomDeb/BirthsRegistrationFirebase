from initialize_firebase import initialize

firebase = initialize()
storage = firebase.storage()

all_files = storage.list_files()

# for file in all_files:
#     print(file.name)
#     if file.name.endswith(".png"):
#       file.download_to_filename(file.name)

# storage.child("images/Screenshot 2023-04-03 001553.png").download("file.png")
