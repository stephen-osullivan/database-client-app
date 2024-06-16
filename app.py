import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from tkinter import ttk

class CSVViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Viewer")
        self.root.geometry("800x600")
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        
        self.table = ttk.Treeview(self.frame)
        self.table.pack(fill=tk.BOTH, expand=1)
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open CSV", command=self.load_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
    
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                self.display_csv(df)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file\n{str(e)}")
    
    def display_csv(self, df):
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(df.columns)
        self.table["show"] = "headings"
        
        for col in self.table["columns"]:
            self.table.heading(col, text=col)
        
        for index, row in df.iterrows():
            self.table.insert("", "end", values=list(row))
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVViewerApp(root)
    root.mainloop()