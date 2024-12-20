from tkinter import *
import math
def click(value):
    st = display.get()
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")", "(", "."]
    try:
        if value == "C":
            st = st[0:len(st) - 1]
            display.delete(0, END)
            display.insert(0, st)
        elif value == "CE":
            display.delete(0, END)
        elif value == "√":
            ans = math.sqrt(eval(st))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "π":
            ans = math.pi
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "cosθ":
            ans = math.cos(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "sinθ":
            ans = math.sin(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "tanθ":
            ans = math.tan(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "2π":
            ans = 2 * math.pi
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "cosh":
            ans = math.cosh(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "sinh":
            ans = math.sinh(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "tanh":
            ans = math.tanh(math.radians(eval(st)))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == chr(8731):  # Cube root
            ans = eval(st) ** (1 / 3)
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "xⁿ":
            display.insert(END, "**")
        elif value == "x³":
            ans = eval(st) ** 3
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "x²":
            ans = eval(st) ** 2
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "ln":
            if st == "0" or st == "0.0":
                display.delete(0, END)
                display.insert(0, "MATH ERROR")
            else:
                ans = math.log2(eval(st))
                display.delete(0, END)
                display.insert(0, ans)
        elif value == "deg":
            ans = math.degrees(eval(st))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "rad":
            ans = math.radians(eval(st))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "e":
            ans = math.e
            display.delete(0, END)
            display.insert(0, ans)
        elif value == "log":
            if st == "0" or st == "0.0":
                display.delete(0, END)
                display.insert(0, "Invalid Input")
            else:
                ans = math.log10(eval(st))
                display.delete(0, END)
                display.insert(0, ans)
        elif value == "x!":
            ans = math.factorial(eval(st))
            display.delete(0, END)
            display.insert(0, ans)
        elif value == chr(247):  # Division symbol
            display.insert(END, "/")
        elif value == "+":
            display.insert(END, "+")
        elif value == "-":
            display.insert(END, "-")
        elif value == "*":
            display.insert(END, "*")
        elif value in list:
            display.insert(END, value)
        elif(value=="%"):
            ans=eval(st)/100
            display.delete(0,END)
            display.insert(0,ans)    
        elif value == "=":
            if len(st) > 1 and st[-1] == "0" and st[-2] == "/":
                display.delete(0, END)
                display.insert(0, "MATH ERROR")
            else:
                ans = eval(st)
                display.delete(0, END)
                display.insert(0, ans)
    except SyntaxError:
        display.delete(0, END)
        display.insert(0, "SYNTAX ERROR")
    
# Main Fxn
                                   
window=Tk()
window.title("Scientific Calculator")
window.config(bg="black")
# window.geometry('680x486+100+100')
window.geometry('433x280+100+100')
window.grid_propagate(False)  # Disable grid resizing
display=Entry(window,font=("ariel",18,"bold"),bg="silver",fg="black",bd=20,relief=SUNKEN,width=30)
display.grid(row=0,column=0,columnspan=8)
button_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*",chr(8731), "xⁿ", "x³", "x²",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%","=","log", "(", ")", "x!"
]
rowvalue=1
columnvalue=0
for i in  button_list:
    button=Button(window,relief=SUNKEN,width=6,height=2,bd=3,bg="silver",fg="black",font=("arial",8,"bold"),activebackground="white",text=i,command=lambda button=i:click(button))
    button.grid(row=rowvalue,column=columnvalue)
    columnvalue+=1
    if(columnvalue>7):
        rowvalue+=1
        columnvalue=0
window.mainloop()