import logging
from tkinter import Tk
from tkinter import *
import urllib.request
from PIL import Image, ImageTk
from tkinter import scrolledtext
import pyglet
import webbrowser
from database_manage import set_data, push_data
import tkinter as tk
from tkinter import ttk
import database_manage
import joblib
import registration_ui
import edit_ui
import images
import storage_manage
import os
import view_information

# Adding fonts
pyglet.font.add_file("fonts/Quicksand_Bold.otf")


def home_ui(user_name=""):
    global root
    root = Tk()
    version = "1.1"
    root.title(f"Births Registration v{version}")

    window_x = 800 * 2 - 300
    window_y = 540 * 2 - 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    centered_x = int(screen_width / 2 - window_x / 2)
    centered_y = int(screen_height / 2 - window_y / 2)

    window_string = f"{window_x}x{window_y}+{centered_x}+{centered_y}"

    # Constant Windows size
    root.geometry(window_string)
    root.minsize(window_x, window_y)
    root.maxsize(window_x, window_y)

    root.iconbitmap("ui/birth_registration_icon.ico")

    main_ui = Image.open("ui/home_ui.png")
    resize_main_ui = main_ui.resize((window_x, window_y))
    resized_main_ui = ImageTk.PhotoImage(resize_main_ui)

    bg_canvas = Canvas(root, width=window_x, height=window_y)
    bg_canvas.pack(fill=BOTH, expand=True)
    bg_canvas.create_image(0, 0, image=resized_main_ui, anchor="nw")

    data = database_manage.retrieve_all_data()

    # data = joblib.load("data")

    def card_buttons(key):
        fetch_data = database_manage.get_data_by_child_id(key)
        edit_ui.set_retrieved_data(fetch_data, key)
        root.destroy()
        edit_ui.call()

    def show_information(key):
        fetch_data = database_manage.get_data_by_child_id(key)
        view_information.set_retrieved_data(fetch_data, key)
        root.destroy()
        view_information.call()

    # create the container frame for the cards
    container_frame = Frame(root, background="white")
    container_frame.place(relx=0.5,
                          rely=0.35,
                          anchor="center",
                          x=10,
                          y=92,
                          width=750,
                          height=604)

    scrollbar = Scrollbar(container_frame, orient="vertical", command="")
    scrollbar.pack(side="right", fill="y")

    # add the cards to the container frame
    for i in data:
        card = Frame(container_frame, highlightbackground="black", highlightthickness=0, bd=1)
        card.pack(side="top",
                  fill="x",
                  padx=10,
                  pady=5,
                  )

        key = Label(card,
                    text=f"Child ID: {i}",
                    font=("Quicksand", 10),
                    )
        key.pack(side="top", anchor="w")

        name_label = Label(card,
                           text="Name: " + data[i]["name"],
                           font=("Quicksand", 10),
                           )
        name_label.pack(side="top", anchor="w")

        birth_label = Label(card,
                            text="Birth: " + data[i]["date_of_birth"],
                            font=("Quicksand", 10),
                            )
        birth_label.pack(side="top", anchor="w")

        address = Label(card,
                        text="Address: " + data[i]["address"],
                        font=("Quicksand", 10),
                        )
        address.pack(side="top", anchor="w")

        guardian_contact_number = Label(card,
                                        text="Number: " + data[i]["guardian_contact_number"],
                                        font=("Quicksand", 10),
                                        )
        guardian_contact_number.pack(side="top", anchor="w")

        # Load the edit icon image
        edit_icon = tk.PhotoImage(file="ui/edit.png")

        tk.Button(card, text="Edit", compound="left",
                  command=lambda i=i: card_buttons(i), borderwidth=1, highlightthickness=0, bd=0, bg="#F0A3E7").pack(side=RIGHT)
        tk.Button(card, text="View", compound="left",
                  command=lambda i=i: show_information(i), borderwidth=1, highlightthickness=0, bd=0, bg="#F0A3C7").pack(side=RIGHT, padx=10)

    def mousePosition(mouse_xy):
        mouse_x = mouse_xy.x
        mouse_y = mouse_xy.y

        urls = {"diskaou apps": "http://priomdeb.com",
                "facebook": "http://priomdeb.com/contact",
                "instagram": "http://priomdeb.com/contact",
                "website": "http://priomdeb.com",
                "linkedin": "http://priomdeb.com/contact",
                "email": "mailto:priom@priomdeb.com"
                }

        print(f"x:{mouse_x}, y:{mouse_y}")

        if 14 <= mouse_x <= 272 and 246 <= mouse_y <= 356:
            root.destroy()
            registration_ui.call()
        elif 14 <= mouse_x <= 272 and 382 <= mouse_y <= 488:
            print("Downloading")
            storage_manage.call()
            os.startfile(os.path.abspath("firebase_images"))
        elif 770 <= mouse_x <= 780 and 20 <= mouse_y <= 30:
            print("Exit")
            # root.destroy()
        elif 754 <= mouse_x <= 762 and 22 <= mouse_y <= 30:
            # root.state(newstate="normal")
            print("Maximize Window")
        elif 736 <= mouse_x <= 746 and 20 <= mouse_y <= 30:
            # root.state(newstate="iconic")
            print("Minimize Window")
        elif 20 <= mouse_x <= 306 and 742 <= mouse_y <= 754:
            webbrowser.open_new(urls["diskaou apps"])
            print("Diskaou Apps")
        elif 974 <= mouse_x <= 1010 and 730 <= mouse_y <= 760:
            webbrowser.open_new(urls["facebook"])
            print("Facebook")
        elif 1040 <= mouse_x <= 1076 and 730 <= mouse_y <= 760:
            webbrowser.open_new(urls["instagram"])
            print("Instagram")
        elif 1106 <= mouse_x <= 1140 and 730 <= mouse_y <= 760:
            webbrowser.open_new(urls["website"])
            print("Website")
        elif 1170 <= mouse_x <= 1206 and 730 <= mouse_y <= 760:
            webbrowser.open_new(urls["linkedin"])
            print("Linkedin")
        elif 1236 <= mouse_x <= 1272 and 730 <= mouse_y <= 760:
            webbrowser.open_new(urls["email"])
            print("Email")

    root.bind("<Button 1>", mousePosition)

    # Binding the enter key for translate
    def enter_key_event(event):
        pass

    root.bind("<Return>", enter_key_event)

    # Run App
    root.mainloop()


def call():
    home_ui()


if __name__ == "__main__":
    call()
