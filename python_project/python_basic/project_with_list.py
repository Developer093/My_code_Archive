import tkinter as tk
window = tk.Tk()
window.title("To do list")
window.geometry("400x300")

def click():
    print("버튼이 눌렸습니다!")
button = tk.Button(window,text="추가",command=click)
button.pack()

def click():
    print("버튼을 만들었습니다.")
button = tk.Button(window,text="삭제",command=click)
button.pack()

window.mainloop()