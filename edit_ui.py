import logging
from tkinter import Tk
from tkinter import *
import urllib.request
from PIL import Image, ImageTk
from tkinter import scrolledtext
import pyglet
import webbrowser

import database_manage
from database_manage import set_data, push_data
import home

# Adding fonts
pyglet.font.add_file("fonts/Quicksand_Bold.otf")

def set_retrieved_data(data, key):
    global fetched_data
    global id

    fetched_data, id = data, key


def edit_information(user_name=""):
    global root
    root = Tk()
    version = "1.1"
    root.title(f"EZ Translation v{version}")

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

    # root.iconbitmap("ui/ezTranslationIcon.ico")

    main_ui = Image.open("ui/registration_form.png")
    resize_main_ui = main_ui.resize((window_x, window_y))
    resized_main_ui = ImageTk.PhotoImage(resize_main_ui)

    bg_canvas = Canvas(root, width=window_x, height=window_y)
    bg_canvas.pack(fill=BOTH, expand=True)
    bg_canvas.create_image(0, 0, image=resized_main_ui, anchor="nw")

    def text_field(x, y, width, height, default_text="Enter your text here"):
        text = Text(root,
                    bg="white",
                    border=0,
                    highlightthickness=0,
                    font=("Quicksand Book", 14),
                    )

        text.pack()
        text.place(x=x,
                   y=y,
                   width=width,
                   height=height,
                   )

        text.insert(INSERT, default_text)
        return text

    name = text_field(x=66, y=146, width=484, height=40, default_text=f"{fetched_data['name']}")
    date_of_birth = text_field(x=66 + 554, y=146, width=484, height=40, default_text=f"{fetched_data['date_of_birth']}")

    address = text_field(x=66, y=146 + 114, width=484, height=40, default_text=f"{fetched_data['address']}")
    birth_location = text_field(x=66 + 554, y=146 + 114, width=484, height=40, default_text=f"{fetched_data['birth_location']}")

    father_name = text_field(x=66, y=146 + 114 * 2, width=484, height=40, default_text=f"{fetched_data['father_name']}")
    mother_name = text_field(x=66 + 554, y=146 + 114 * 2, width=484, height=40, default_text=f"{fetched_data['mother_name']}")

    guardian_contact_number = text_field(x=66, y=146 + 114 * 3, width=484, height=40,
                                         default_text=f"{fetched_data['guardian_contact_number']}")
    guardian_nid = text_field(x=66 + 554, y=146 + 114 * 3, width=484, height=40, default_text=f"{fetched_data['guardian_nid']}")



    def upload_data():
        data = set_data(name=name.get("1.0", "end-1c"),
                        date_of_birth=date_of_birth.get("1.0", "end-1c"),
                        address=address.get("1.0", "end-1c"),
                        birth_location=birth_location.get("1.0", "end-1c"),
                        father_name=father_name.get("1.0", "end-1c"),
                        mother_name=mother_name.get("1.0", "end-1c"),
                        guardian_contact_number=guardian_contact_number.get("1.0", "end-1c"),
                        guardian_nid=guardian_nid.get("1.0", "end-1c")
                        )

        status = database_manage.update_data(data=data, child_id=id)
        if status:
            root.destroy()
            home.call()



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

        if 670 <= mouse_x <= 880 and 572 <= mouse_y <= 618:
            upload_data()
            # print(name.get("1.0", "end-1c"))
            # print(date_of_birth.get("1.0", "end-1c"))
            # print(address.get("1.0", "end-1c"))
            # print(birth_location.get("1.0", "end-1c"))
            # print(father_name.get("1.0", "end-1c"))
            # print(mother_name.get("1.0", "end-1c"))
            # print(guardian_contact_number.get("1.0", "end-1c"))
            # print(guardian_nid.get("1.0", "end-1c"))
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
            # webbrowser.open_new(urls["diskaou apps"])
            print("Diskaou Apps")
        elif 974 <= mouse_x <= 1010 and 730 <= mouse_y <= 760:
            # webbrowser.open_new(urls["facebook"])
            print("Facebook")
        elif 1040 <= mouse_x <= 1076 and 730 <= mouse_y <= 760:
            # webbrowser.open_new(urls["instagram"])
            print("Instagram")
        elif 1106 <= mouse_x <= 1140 and 730 <= mouse_y <= 760:
            # webbrowser.open_new(urls["website"])
            print("Website")
        elif 1170 <= mouse_x <= 1206 and 730 <= mouse_y <= 760:
            # webbrowser.open_new(urls["linkedin"])
            print("Linkedin")
        elif 1236 <= mouse_x <= 1272 and 730 <= mouse_y <= 760:
            # webbrowser.open_new(urls["email"])
            print("Email")
        elif 906 <= mouse_x <= 1114 and 572 <= mouse_y <= 614:
            root.destroy()
            home.call()

    root.bind("<Button 1>", mousePosition)

    # Binding the enter key for translate
    def call_translate_on_enter_key_pressed(event):
        pass

    root.bind("<Return>", call_translate_on_enter_key_pressed)

    # Drawing display name
    font_size = 20
    if len(user_name) > 14:
        font_size = 14
    if len(user_name) > 21:
        font_size = 10
    if len(user_name) > 32:
        font_size = 8

    logout_button = Button(root,
                           bg="white",
                           text="Log out",
                           border=0,
                           font=("Quicksand Bold", 6),
                           activebackground="#CBC9FE",
                           foreground="black",
                           command=""
                           )
    logout_button.place(x=28,
                        y=492,
                        width=32,
                        height=12
                        )

    # Run App
    root.mainloop()


def call():
    edit_information()


if __name__ == "__main__":
    call()



