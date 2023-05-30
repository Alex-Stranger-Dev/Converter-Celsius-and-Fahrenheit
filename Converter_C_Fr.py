import tkinter as tk
root = tk.Tk()
root.geometry("450x350")
root.minsize(350,350)
root.maxsize(450,350)
root.title("Converter Celsius and Fahrenheit by AlexDev")
root.configure(background="grey")
def convert2c():
    f = float(f_entry.get())
    c = round((f-32) / (9/5), 2)
    c_entry.delete(0, tk.END)
    c_entry.insert(0, c)
    
def convert2f():
    c = float(c_entry.get())
    f = round((c*9/5) + 32, 2)
    f_entry.delete(0, tk.END)
    f_entry.insert(0,f)
f_entry = tk.Entry(root, font="lucida 14")
f_entry.grid(row=0, column = 0)
f_label= tk.Label(root, text = "F", font="lucida 14")
f_label.grid(row=0, column=1)
c_entry = tk.Entry(root, font="lucida 14")
c_entry.grid(row=1, column=0)
c_label = tk.Label(root, text="C", font="lucida 14")
c_label.grid(row=1, column=1)

convert2c_but = tk.Button(root, text="Convert to Celsius", padx=23.5,pady=11,font="lucida 14",bg="green",command=convert2c)
convert2c_but.grid(row=2, column=0)

convert2f_but = tk.Button(root, text="Convert to Fahrenheit", padx=11,pady=11,font="lucida 14",bg="green", command=convert2f)
convert2f_but.grid(row=3, column=0)
root.mainloop()

