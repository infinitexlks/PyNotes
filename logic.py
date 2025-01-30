import tkinter as tk
from tkinter import simpledialog, messagebox

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        
        self.notes = {}
        
        self.note_listbox = tk.Listbox(root)
        self.note_listbox.pack(fill=tk.BOTH, expand=1)
        
        self.note_listbox.bind("<Double-Button-1>", self.open_note)
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Note", command=self.new_note)
        self.file_menu.add_command(label="Delete Note", command=self.delete_note)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        
    def new_note(self):
        note_title = simpledialog.askstring("Title", "Enter note title:")
        if note_title:
            self.notes[note_title] = ""
            self.update_note_list()
    
    def delete_note(self):
        selected_note = self.note_listbox.get(tk.ACTIVE)
        if selected_note:
            del self.notes[selected_note]
            self.update_note_list()
    
    def open_note(self, event):
        selected_note = self.note_listbox.get(tk.ACTIVE)
        if selected_note:
            note_content = simpledialog.askstring("Content", "Edit note content:", initialvalue=self.notes[selected_note])
            if note_content is not None:
                self.notes[selected_note] = note_content
    
    def update_note_list(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            self.note_listbox.insert(tk.END, note)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
