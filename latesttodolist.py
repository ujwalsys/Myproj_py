import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ujwal's To-Do List 💖")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        self.tasks = []

        self.title_label = tk.Label(self.root, text="My To-Do List", font=("Helvetica", 18, "bold"), fg="#ff69b4")
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=30, height=10, bd=0, font=("Helvetica", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.entry = tk.Entry(self.entry_frame, width=30, font=("Helvetica", 12))
        self.entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, bg="#ff69b4", fg="white", font=("Helvetica", 12))
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=("Helvetica", 12))
        self.delete_button.pack(pady=10)

        self.populate_listbox()

    def populate_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
