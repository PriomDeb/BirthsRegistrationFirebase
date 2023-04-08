import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import ttk

class ImageViewer:
    def __init__(self, window):
        self.master = window
        window.title("Image Viewer")
        window.configure(bg="white")

        self.width = 600
        self.height = 600

        # Create container for the label and image
        self.container = tk.Frame(window, width=self.width, height=self.height, bg="#ffffff")
        self.container.pack(fill=tk.BOTH, expand=True)

        # Create a centered label at the top
        self.label = tk.Label(self.container, text="Images Uploaded by Shastho Kormi", font=("Helvetica", 16), bg="#ffffff")
        self.label.place(relx=0.5, rely=0.05, anchor="center")

        # Create container for the image
        self.image_container = tk.Frame(window, width=self.width, height=self.height, bg="#f0f0f0")
        self.image_container.pack()

        # Center the container in the window
        self.image_container.place(relx=0.5, rely=0.5, anchor="center")

        # Create label for the image
        self.image_label = tk.Label(self.image_container)
        self.image_label.pack()

        # Create navigation buttons
        self.prev_button = tk.Button(window, text="Prev", command=self.prev_image, width=20, height=4, bg="#F0A3E7", fg="white", font=("Helvetica", 14), highlightthickness=0, bd=0)
        self.prev_button.pack(side="left")

        self.next_button = tk.Button(window, text="Next", command=self.next_image, width=20, height=4, bg="#F0A3E7", fg="white", font=("Helvetica", 14), highlightthickness=0, bd=0)
        self.next_button.pack(side="right")

        # Load and display the first image
        self.current_index = 0
        self.image_filenames = sorted(os.listdir("ui"))
        self.show_image()

        self.open_folder_button = tk.Button(window, text="Open Folder", command=self.open_folder, width=20, height=4, bg="#F0A3E7", fg="white", font=("Helvetica", 14), highlightthickness=0, bd=0)
        self.open_folder_button.pack(side="bottom")

    def open_folder(self):
        os.startfile(os.path.abspath("ui"))

    def show_image(self):
        # Load the image and scale it to fit in the container
        image_filename = self.image_filenames[self.current_index]
        image = Image.open(os.path.join("ui", image_filename))
        width, height = image.size
        if width > height:
            new_width = self.width
            new_height = int(height * new_width / width)
        else:
            new_height = self.height
            new_width = int(width * new_height / height)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create a PhotoImage object and display it
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_filenames)
        self.show_image()

    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_filenames)
        self.show_image()


def call():
    root = tk.Tk()
    app = ImageViewer(root)
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

    root.mainloop()


if __name__ == "__main__":
    call()


