#!/usr/bin/env python

import Tkinter as tk


friends = ['dummy1', 'dummy2', 'dummy3', 'dummy4']

def send_button_clicked(user_input_box):
    text = user_input_box.get()
    user_input_box.delete(0, tk.END)
    print text


root = tk.Tk()

screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.title("Tallo app")
root.bind('<Return>',lambda event :send_button_clicked(user_input))


#friends_list = tk.LabelFrame(root, text="Friends list", bg='red', height=screen_height, width=int(screen_width*0.1))
friends_list = tk.Frame(root, bg='red', height=screen_height, width=int(screen_width*0.1))
friends_list.pack(side = tk.LEFT)

for friend in friends:
    new_label = tk.Label(friends_list, text=friend)
    new_label.pack(side=tk.TOP)

user_input = tk.Entry(root)
user_input.pack(side=tk.BOTTOM, fill=tk.X)



messages_frame = tk.Label(root, bg='yellow', height=int(screen_height*0.8), width=int(screen_width*0.8))
messages_frame.pack(side=tk.TOP)


root.mainloop()


