import tkinter as tk

window = tk.Tk()
window.title('JEFFS PROJECT')
frame1 =tk.Frame(master=window,width=200,height=100,bg='grey')
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame2 =tk.Frame(master=window,width=100,bg='white')
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

frame3 =tk.Frame(master=window,width=50,bg='green')
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

window.mainloop()

