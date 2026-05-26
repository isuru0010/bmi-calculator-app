import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def calculate_bmi():
    try:
        weight_text=weight_entry.get()
        height_text=height_entry.get()

        weight=float(weight_text)
        height=float(height_text)
        bmi = weight / (height*height)
        bmi = round(bmi, 2)
        progress_value = 0.0

        if bmi < 18.5:
            status= "Under weight"
            color="orange"
            progress_value = 0.25
        elif bmi >=18.5 and bmi <= 24.9:
            status="Healthy"
            color="green"
            progress_value = 0.50
        elif bmi >=25 and bmi <= 29.9:
            status="over weight"
            color="Orange"
            progress_value = 0.75
        else:
            status="You are fat"
            color="red"
            progress_value = 1.0
        result_label.configure(text="Your BMI is: " + str(bmi) + "\nStatus: " + status, text_color=color)
        
        progress_bar.set(progress_value)
        progress_bar.configure(progress_color=color)
        
    except ValueError:
        result_label.configure(text="Error", text_color="red")
        progress_bar.set(0)

window=ctk.CTk()
window.title("BMI Calculator Pro")

window.iconbitmap("E:\\work\\python\\BMI_Cal\\pp_icon.ico")
window.geometry("700x550")


title_label=ctk.CTkLabel(window, text="BMI calculator", font=("Arial",24,"bold"))
title_label.pack(pady=(30, 20))

#weight_label = ctk.CTkLabel(window, placeholder_text="Enter yout Weight(KG):", width=250, height=40, font=("Arial", 14))
#weight_label.pack(10)
weight_entry = ctk.CTkEntry(window, placeholder_text="Enter yout Weight(KG):", width=250, height=40, font=("Arial", 14))
weight_entry.pack(pady=10)

#height_label = ctk.CTkLabel(window, placeholder_text="Enter yout Height( Meter, Ex: 1.75): ", width=250, height=40, font=("Arial", 14))
#height_label.pack(pady=10)
height_entry = ctk.CTkEntry(window, placeholder_text="Enter yout Height( Meter, Ex: 1.75): ", width=250, height=40, font=("Arial", 14))
height_entry.pack(pady=10)

calc_button = ctk.CTkButton(window, text="Calculate", command = calculate_bmi, corner_radius=32, width=200, height=45, font=("Arial", 15, "bold"))
calc_button.pack(pady=30)

result_label = ctk.CTkLabel(window, text="Result is here.", font=("Arial", 16))
result_label.pack(pady=10)

progress_bar= ctk.CTkProgressBar(window, width=300, height=15, corner_radius=10)
progress_bar.pack(pady=(0, 15))
progress_bar.set(0)

window.mainloop()
