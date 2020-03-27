from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Calculator")

def calc(key):
	global memory
	if key =='=':
		s = '0123456789+-*/.'
		if entry.get()[0] not in s:
			entry.insert(END,'Error')
			messagebox.showerror('Error', 'Error')
		try:
			res = eval(entry.get())
			entry.insert(END, '=' + str(res))
		except:
			entry.insert(END, 'Error')
			messagebox.showerror('Error')
	elif key =='C':
		entry.delete(0,END)
	elif key =='+/-':
		if '=' in entry.get():
			entry.delete(0, END)
		try:
				if entry.get()[0] == '+':
					entry.delete(0)
				else:
					entry.insert(0, '-')
		except IndexError:
			pass
	else:
		if '=' in entry.get():
			entry.delete(0, END)
		entry.insert(END, key)



buttons_list = ['1','2','3','4','5','6','7','8','9','0',
				'+','-','*','/','+/-','C','=', '.']
r=1
c=0

for i in buttons_list:
	s = ''
	cmd = lambda x=i: calc(x)
	ttk.Button(root, text=i, command=cmd).grid(row=r,column=c)
	c+=1
	if c>2:
		c = 0
		r+=1

entry = Entry(root, width=30)
entry.grid(row=0,column=0,columnspan=5)

root.mainloop()