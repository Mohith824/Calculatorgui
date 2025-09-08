import tkinter
import math
button_values= [
     ["AC","+/-","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],

    ["0",".","√","="]
]

right_but=["÷","×","-","+","="]
top_but=["AC","+/-","%"]




row_count=len(button_values)
column_count=len(button_values[0])

clr_lightgrey="#D4D4D2"
clr_black="#1C1C1C"
clr_drkgrey="#505050"
clr__orange="#083FF4"
clr_white="white"

window=tkinter.Tk()
window.title('Calculator')
window.resizable(False,False)

frame=tkinter.Frame(window)

label=tkinter.Label(frame,text="0",font=("Arial",45),bg=clr_black,fg=clr_white,anchor='e',width=column_count)
label.grid(row=0,column=0,columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value=button_values[row][column]
        button=tkinter.Button(frame,text=value,font=("Arial",25),
                              width=column_count-1,height=1,
                              command=lambda value=value:button_clicked(value))
        
        if value in top_but:
            button.config(background=clr_lightgrey,foreground=clr_black)
        elif value in right_but:
            button.config(background=clr__orange,foreground=clr_white)
       
        else:
            button.config(background=clr_drkgrey,foreground=clr_white)

        button.grid(row=row+1,column=column)

frame.pack()
A="0"
operator=None
B=None
def clearall():
    global A,B,operator
    A="0"
    operator=None
    B=None
def remove_zero(num):
    if num%1==0:
        num=int(num)
    return str(num)

def button_clicked(value):
    global A, B,operator,right_but,top_but,label
    if value in right_but:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)
                if operator=='+':
                    label["text"]=remove_zero(numA+numB)
                elif operator=='-':
                    label["text"]=remove_zero(numA-numB)
                elif operator=='×':
                    label["text"]=remove_zero(numA*numB)
                elif operator=='÷':
                    label["text"]=remove_zero(numA/numB)
    
            clearall()
    

    
        elif value in "+-×÷":
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"
            operator=value
    

       
    elif value in top_but:
        if value=="AC":
            clearall()
            label["text"]='0'
        elif value=="+/-":
            result=float(label["text"])*-1
            label["text"]=remove_zero(result)
        elif value=="%":
            result=float(label["text"])/100
            label["text"]=remove_zero(result)
        
        
    else:
        if value==".":
            if value not in label["text"]:
                    label["text"]+=value
            
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window_y=int((screen_height/2)-(window_height/2))
window_x=int((screen_width/2)-(window_width/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
