import requests
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

# Awesome free to use api by alexwohlbruck
api_endpoint = "https://cat-fact.herokuapp.com/facts/random"

# Necessary parameters
parameters = {
    "animal_type": "cat",
    "amount": 10,
}

response = requests.get(url=api_endpoint, params=parameters)
data = response.json()

fact_db = []
# Sometimes the facts are gibberish or in some other language. Don't think that there's a language parameter
for items in data:
    fact_db.append(items["text"])

FONT = ("Calibri", 15, "bold")


# Displays the fact as a messagebox and changes the cute kitty image after its closed
def display_fact():
    global fact_db
    global display
    messagebox.showinfo("Fact", random.choice(fact_db))
    canvas.itemconfigure(tagOrId=display, image=random.choice(images))


# Initialization and creation of the UI.
window = Tk()
window.title("Cat Facts!")
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(height=500, width=500, highlightthickness=0)
images = []
for i in range(1, 4):
    image = Image.open(f"Images/cat{i}.png")
    resized_image = image.resize((500, 500), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    images.append(new_image)

display_image = random.choice(images)
display = canvas.create_image(250, 250, image=display_image)
canvas.grid(row=0, column=0, columnspan=2, pady=20)

fact_button = Button(text="Get Fact", font=FONT, width=40, command=display_fact)
fact_button.grid(row=1, column=0, columnspan=2)

window.mainloop()
