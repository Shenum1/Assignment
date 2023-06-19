import tkinter as tk
def convert_fah_to_cel():
    fahrenheit = float(ent_fah.get())
    celsius =((5/9) * fahrenheit)-32
    lbl_result['text'] = round(celsius, 2),"/N{DEGREE CELSIUS}"
window = tk.Tk()
window.title("fahrenheit to Celsius")

frame = tk.Frame(master=window)
ent_fah = tk.Entry(master=frame, width=10)
lbl_fah = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
btn_convert = tk.Button(master=frame,command=convert_fah_to_cel, text= "Convert")
lbl_result = tk.Label(master=frame, text="\N{DEGREE CELSIUS}")

frame.grid(row=0, column=0)

ent_fah.grid(row=0, column=0)
ent_fah.grid(row=0, column=1)

lbl_fah.grid(row=0, column=1)
btn_convert.grid(row=0, column=2)
lbl_result.grid(row=0, column=3)










window.mainloop()
