import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, CENTER, X
from PIL import Image, ImageTk
import requests
from datetime import datetime, timedelta

def get_weather():
    city = e_var.get()
    api_key = '*************************'  # Replace with your actual API key
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    try:
        response = requests.get(api_url)
        data = response.json()
        if data['cod'] != 200:
            raise KeyError

        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        temp_in_Centigrade = round(temp - 273.5, 2)
        humid = data['main']['humidity']
        w_speed = data['wind']['speed']
        pressure = data['main']['pressure']

        timezone = data['timezone']
        localtime = datetime.utcnow() + timedelta(seconds=timezone)
        formatted_time = localtime.strftime("%H:%M:%S")

        time_label.configure(text=f'{formatted_time}')
        city_country_label.configure(text=f'{city}/{country}', fg='#2E4053')
        temp_label.configure(text=f'  {temp_in_Centigrade}  °C')
        humid_label.configure(text=f'      {humid}   %')
        w_speed_label.configure(text=f'  {w_speed} m/s')
        pressure_label.configure(text=f'{pressure} hPa')

    except requests.exceptions.RequestException:
        city_country_label.configure(text="Error fetching data", bg='white', fg='red')
        time_label.configure(text='')
        temp_label.configure(text='')
        humid_label.configure(text='')
        w_speed_label.configure(text='')
        pressure_label.configure(text='')
    except KeyError:
        city_country_label.configure(text="City not found", bg='white', fg='red')
        time_label.configure(text='')
        temp_label.configure(text='')
        humid_label.configure(text='')
        w_speed_label.configure(text='')
        pressure_label.configure(text='')

# GUI setup
root = tk.Tk()
root.geometry('760x575')
root.title('Weather API')
root.configure(bg='white')
root.wm_iconbitmap('1.ico')

# Background image
image_path = 'C:/Users/Administrator/Desktop/Humidity2.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((755, 400))
bg_image = ImageTk.PhotoImage(resized_image)
bg_label = Label(root, image=bg_image)
bg_label.place(x=1, y=170)

# Heading
heading = Label(root, text='Weather Vista: Real-Time Weather at a Glance',
                fg='white', font=('times new roman', 22, 'bold'), bg='#2E4053')
heading.pack(anchor=CENTER, fill=X)

search_here = Label(root, text='Search here', font=('Times new roman', 20, 'bold'),
                    fg='#2E4053', bg='white')
search_here.place(x=66, y=85)

# Search bar
search_image = tk.PhotoImage(file='C:/Users/Administrator/Desktop/Copy of search.png')
searchimage_lbl = Label(root, image=search_image, bg='white')
searchimage_lbl.place(x=210, y=63)

# Entry
e_var = StringVar()
e = Entry(root, fg='white', textvariable=e_var, font=('Times New Roman', 22, 'bold'),
          bg='#404040', border=0, width=20)
e.place(x=262, y=84)

# Search icon
search_icon = tk.PhotoImage(file='C:/Users/Administrator/Desktop/Copy of search_icon.png')
searchicon_label = Button(root, image=search_icon, cursor='hand2', border=0,
                          bg='#404040', command=get_weather)
searchicon_label.place(x=590, y=75)

# Labels for weather info
city_country_label = Label(root, text='', bg='white', fg='#1ABC9C',
                           font=('lucida calligraphy', 18, 'bold'))
city_country_label.place(x=9, y=133)

time_label = Label(root, text='', bg='#2E4053', fg='white',
                   font=('Times new roman', 18, 'bold'))
time_label.place(x=67, y=439)

temp_label = Label(root, text='', bg='#2E4053', fg='white',
                   font=('Times new roman', 18, 'bold'))
temp_label.place(x=205, y=439)

pressure_label = Label(root, text='', bg='#2E4053', fg='white',
                       font=('Times new roman', 18, 'bold'))
pressure_label.place(x=355, y=439)

humid_label = Label(root, text='', bg='#2E4053', fg='white',
                    font=('Times new roman', 18, 'bold'))
humid_label.place(x=488, y=439)

w_speed_label = Label(root, text='', bg='#2E4053', fg='white',
                      font=('Times new roman', 18, 'bold'))
w_speed_label.place(x=640, y=440)

root.mainloop()
