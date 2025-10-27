import tkinter as tk

window_main = tk.Tk()

label1 = tk.Label(window_main, text="Label 1")
label2 = tk.Label(window_main, text="Label 2")

tombol1 = tk.Button(window_main, text="Tombol 1")
tombol2 = tk.Button(window_main, text="Tombol 2")

# method positioning
label1.pack()
label2.pack()

tombol1.pack()
tombol2.pack()

# method tampil
window_main.mainloop()