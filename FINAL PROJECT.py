import tkinter
import random
from tkinter import messagebox 
#root window most important
root=tkinter.Tk()
#root.configure(bg="white")
root.title("ENTERTAINERS")
root.geometry("250x280")
#list for keeping data
l=[]
q=0
def clear_it():
	list_to_do.delete(0,"end")
def update():
	clear_it()
	for i in l:
		if i=="" or i==" " or i==None or i=="  " or i=="   ":
			l.remove(i)
			#display["text"]="Please enter a task"
			messagebox.showwarning("Request","Enter a valid request")
		else:
			display["text"]="We shall upload ASAP"
			list_to_do.insert("end",i)
def add_task():
	global l
	b=inp.get()	
	l.append(b)
	inp.delete(0,"end")
	update()
def del_all():
	c=messagebox.askyesno("Confirm","Do you really want to delte all requests??")
	global l
	if c:
		l=[]
		update()
def del_task():
	b=list_to_do.get("active")
	if b in l:
		l.remove(b)
	update() 
def sort_asc_task():
	l.sort()
	update()
def sort_dsc_task():
	l.sort(reverse=True)
	update()
def choose_random():
	a=random.choice(l)
	display['text']=a
def number():
	global q
	q+=1
	display["text"]="Number of likes: "+str(q)
def car():
	import pgme_1
def snake():
	import Snake_Game
title=tkinter.Label(root,text="ENTERTAINERS",bg="white")
title.grid(row=0,column=0)
display=tkinter.Label(root,text="Welcome Challenger!!!",bg="white")
display.grid(row=0,column=1)
inp=tkinter.Entry(root,width=15)
inp.grid(row=1,column=1)
badd_task=tkinter.Button(root,text="Car Game",command=car,fg="green",bg="white")
badd_task.grid(row=1,column=0)

bdel_all=tkinter.Button(root,text="Snake Game",command=snake,fg="green",bg="white")
bdel_all.grid(row=2,column=0)

bdel_task=tkinter.Button(root,text="Add request",command=add_task,fg="green",bg="white")
bdel_task.grid(row=3,column=0)

sort_asc=tkinter.Button(root,text="Delete request",command=del_task,fg="green",bg="white")
sort_asc.grid(row=4,column=0)

sort_desc=tkinter.Button(root,text="Delete all",command=del_all,fg="green",bg="white")
sort_desc.grid(row=5,column=0)

choose_task=tkinter.Button(root,text="Choose Random",command=choose_random,fg="green",bg="white")
choose_task.grid(row=6,column=0)

number_task=tkinter.Button(root,text="LIKE",command=number,fg="green",bg="white")
number_task.grid(row=7,column=0)

exit=tkinter.Button(root,text="Exit",command=exit,fg="red",bg="white")
exit.grid(row=8,column=0)

list_to_do=tkinter.Listbox(root)
list_to_do.grid(row=2,column=1,rowspan=6)
