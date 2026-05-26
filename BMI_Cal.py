import tkinter as tk

def calculate_bmi():
    try:
        weight_text=weight_entry.get()
        height_text=height_entry.get()

        weight=float(weight_text)
        height=float(height_text)
        bmi = weight / (height*height)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            status= "Under weight"
            color="orange"
        elif bmi >=18.5 and bmi <= 24.9:
            status="Healthy"
            color="green"
        elif bmi >=25 and bmi <= 29.9:
            status="over weight"
            color="Orange"
        else:
            status="You are fat"
            color="red"
        result_label.config(text="Your BMI is :" + str(bmi) + "Status: " + status, fg=color)
    except ValueError:
        result_label.config(text+"Error")

window=tk.Tk()
window.title("BMI Calculator")

window.iconbitmap("E:\work\python\BMI_Cal\pp_icon.ico")
window.geometry("600x350")

title_label=tk.Label(window, text="BMI calculator", font=("Arial",16,"bold"))
title_label.pack(pady=10)

weight_label = tk.Label(window, text="Enter yout Weight( KG): ")
weight_label.pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Enter yout Height( Meter, Ex: 1.75): ")
height_label.pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack()

calc_button = tk.Button(window, text="Calculate", command = calculate_bmi, bg="lightblue", font=("Arial", 10, "bold"))
calc_button.pack(pady=10)

result_label= tk.Label(window, text="Result is here.", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
