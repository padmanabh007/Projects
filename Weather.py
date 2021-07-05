import tkinter as tk
import requests

def getWeather(canvas) :
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=[api key]"
    json_d=requests.get(api).json()
    condition=json_d['weather'][0]['main']
    temp=int(json_d['main']['temp']-273.15)
    max_temp=int(json_d['main']['temp_max']-273.15)
    min_temp=int(json_d['main']['temp_min']-273.15)
    humidity=int(json_d['main']['humidity'])

    final_info=condition+"\n"+str(temp)+"°C"
    final_data="\n"+"Max Temp "+str(max_temp)+"\n"+"Min Temp "+str(min_temp)+"\n"+"Humidity "+str(humidity)
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f=("poppins",15,"bold")
t=("poppins",25,"bold")

textfield=tk.Entry(canvas,justify="center",font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()