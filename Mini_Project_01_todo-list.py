# To-DoList
## add, remove, edit, done, display, reset, exit

def add():
	"""add a new task to the To-Do List if not exist"""
	task = input("your task: ")
	if task not in tasks:
		tasks.append(task)
		is_done.append(False)
	else:
		print(f"'{task}' is exist!")

def display():
	"""Show list of all tasks from To-Do list"""
	for i in range(len(tasks)):
		print(f"{i+1}: {tasks[i]}-->{is_done[i]}")

def remove():
	""" Remove a task from To-Do list if exist """
	error1 = True
	while error1:
		try:
			index = int(input("index: "))
			if index <= len(tasks) and index >= 1:
				del_task = input("are you sure to remove '{tasks[index]}'?(y/n) ")
				if del_task == "y":
					index -= 1
					tasks.pop(index)
					is_done.pop(index)
					error1 = False
					print("Your task has been successfully deleted")
			else:
				print("index out of range")
		except Exception as e:
			print(e)

def search(): 
	""" Search in To-Do list with a word """
	for i, task in enumerate(tasks):
		if search_word in task:
			print("{task} ---> {is_done[i]}")

def edit():
	""" Edit a task from To-Do list if exist """
	error1 = True
	while error1:
		try:
			index = int(input("index: "))
			if index <= len(tasks) and index >= 1:
				del_task = input("are you sure to edit '{tasks[index]}'?(y/n) ")
				if del_task == "y":
					index -= 1
					tasks[index] = input("your new task: ")
					error1 = False
					print("Your task has been successfully edited")
			else:
				print("index out of range")
		except Exception as e:
			print(e)

def done(done_tasks):
	"""Changing tasks from not done to done"""
	for i in done_tasks:
		try:
			is_done[i-1] = True
		except Exception as e:
			print(e)

def reset():
	"""Reset To-Do List and clear all tasks"""
	tasks.clear()
	is_done.clear()
	print("Your To-Do list has been successfully clear")

tasks = []
is_done = []
while True:
	command = input("To-DoList@To-DoList:$ ").lower()
	if command == "add":
		add()
	elif command == "remove":
		display()
		remove()
	elif command == "edit":
		display()
		edit()
	elif command == "done":
		s = input("tasks: ")
		done_tasks = list(map (int, s.split()))
		done(done_tasks)
	elif command == "display":
		display()
	elif command == "search":
		search()
	elif command == "reset":
		reset()
	elif command == "":
		pass
	elif command == "exit":
		exit()
	else:
		print(f"{command}: command not found")