import tkinter
import math
from tkinter import *
import simpleaudio

goal_sessions = 4
black = "#000000"
white = "#FFFFFF"
background = "#1100ff"
break_min = 10
work_min = 50
sessions_done = 0
font_name = "Palatino Linotype"
img_directory = "28 (pomodoro)/shf.png"
img_width = 300
img_height = 300
reps = 1


def stop_timer():
    window.after_cancel(timer)


def start_timer():
    global reps
    
    work_sess = work_min * 60 # * 60
    break_sess = break_min * 60
    #reps += 1
    
    if reps % 2 == 1:
        #current_session_label.config(text=f"study({current_session}/{goal_sessions})"
        type = "study"
        countdown(work_sess, type)
    elif reps % 2 == 0:
        #current_session_label.config(text="break")
        type="break"
        countdown(break_sess, type)

def countdown(count, type):
    global reps
    global current_session
    #current_session = math.floor(reps/2)

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)

    timer_text.config(text=f"{count_min}:{count_sec}")

    global timer   
    if count > 0:
        timer = window.after(1000, countdown, count-1, type) #a cada 1000milisec ativa dnv o countdown
    else:
        reps +=1
        print(reps)

        print("som final")


        if type == "break":
            #reps += 1
            current_session = math.ceil(reps/2)
            #current_session = reps
            current_session_label.config(text=f"study({current_session}/{goal_sessions})")
            if work_min < 10:
                timer_text.config(text=f"0{work_min}:00")
            else:
                timer_text.config(text=f"{work_min}:00")
        else:
            current_session_label.config(text=f"break")
            if break_min < 10:
                timer_text.config(text=f"0{break_min}:00")
            else:
                timer_text.config(text=f"{break_min}:00")
                 





#visualmente
window = Tk()
window.title("pomodoro")
window.config(padx=40, pady=20, bg=background, highlightthickness=0)
window.minsize(width=380, height=260)

current_session_label = Label(text=f"study(1/{goal_sessions})", fg=white, font=(font_name, 50), bg=background)
current_session_label.grid(row=0, column=0)

canvas = Canvas(width=img_width, height=img_height) # usar tamanho da imagem pra nao ficar esticado
img = PhotoImage(file=img_directory)
canvas.create_image(img_width/2,img_height/2, image=img)
canvas.grid(column=0, row=4, pady=20)

#timer_text = canvas.create_text(img_width, img_height, text="00:00", fill=black,font=(font_name, 35, "bold"))
timer_text = Label(text="50:00", fg=white,font=(font_name, 50), bg=background)
timer_text.grid(row=1, column=0)

button_frame = tkinter.Frame(window, bg=background)
button_frame.grid(column=0, row=2)

start_button = tkinter.Button(button_frame,text="start studying", highlightthickness=0, font=(font_name,10),
                    bg=background, fg=white, borderwidth=0, pady=10, command=start_timer)
start_button.pack(side="left", padx=10)


stop_button = tkinter.Button(button_frame, text="stop timer", highlightthickness=0, font=(font_name, 10),
                     bg=background, fg=white, borderwidth=0, pady=10, command=stop_timer)
stop_button.pack(side="right", padx=10)









# #Entry
# input = Entry(width=40)
# input.grid(column=1, row=3)

# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=10)
# todo = []
# for item in todo:
#     listbox.insert(todo.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.grid(column=1, row=2)



window.mainloop()