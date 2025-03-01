from tkinter import *
from Node import Node
from Splaytree import SplayTree 

class TreeVisualizer:
    def __init__(self, master):
        self.master = master
        self.tree = SplayTree()
        self.setup_gui()

    def setup_gui(self):
        frame = Frame(self.master)
        frame.grid(column=1)
        Label(frame, text="Key").grid(row=0)
        Label(frame, text="Data").grid(row=1)
        self.e1 = Entry(frame)
        self.e2 = Entry(frame)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        Button(frame, text="Insert", command=self.insert).grid(row=2, column=0)
        Button(frame, text="Search", command=self.search).grid(row=2, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=2, column=2)
        self.canvas = Canvas(self.master, width=1000, height=500, bg="white")
        self.canvas.grid(row=3, column=1)

    def insert(self):
        key = int(self.e1.get())
        data = self.e2.get()
        self.tree.insert(key, data)
        self.tree.draw(self.canvas)
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def search(self):
        key = int(self.e1.get())
        result = self.tree.search(key)
        if result:
            print(f"Found: {result.key}")
        else:
            print("Not found")
        self.tree.draw(self.canvas)
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def delete(self):
        key = int(self.e1.get())
        self.tree.delete(key)
        self.tree.draw(self.canvas)
        self.e1.delete(0, END)
        self.e2.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = TreeVisualizer(root)
    root.mainloop()