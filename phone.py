import json 
import pycountry
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country

class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("600x400")
        self.window.configure(bg="#8DA290")
        self.window.resizable(False, False)

        #___________Application menu_____________
        Label(App, text="Enter a phone number",fg="black", font=("Times", 20), bg="#8DA290").place(x=170,y= 40)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Track Country", bg="#BEC7B4", relief="sunken")
        self.country_label = Label(App,fg="black", font=("Times", 20), bg="#8DA290")

        #___________Place widgets on the window______
        self.phone_number.place(x=200, y=130)
        self.track_button.place(x=250, y=200)
        self.country_label.place(x=100, y=280)

        #__________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.Track_location)
        #255757294146

    def Track_location(self,event):
        phone_number = self.phone_number.get()
        country = "Country is Unknown"
        if phone_number:
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
            print(tracked)
            if tracked:
                country = tracked.official_name
        self.country_label.configure(text=country)

PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()