import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()

# Load the image
image = Image.open("один-пингвин.jpg")
photo = ImageTk.PhotoImage(image)

# Create a label with the image
label = tk.Label(root, image=photo)
label.pack()

# Set the window title
root.title("Пингвин")

# Run the main loop
root.mainloop()
