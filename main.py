import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import sys
import re
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from config.settings import *
from utils.logger import logger

class MarkdownEditor:
    """Advanced Markdown Editor Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg="#1e1e1e")
        
        self.current_file = None
        self.is_modified = False
        
        self.setup_styles()
        self.create_ui()
        
        logger.info(f"Application started - {APP_NAME}")
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
    
    def create_ui(self):
        # Header
        header = tk.Frame(self.root, bg='#333333', height=50)
        header.pack(fill='x', padx=0, pady=0)
        header.pack_propagate(False)
        
        self.title_label = tk.Label(
            header,
            text="📝 Markdown Editor - Untitled",
            font=("Segoe UI", 14, "bold"),
            fg='white',
            bg='#333333'
        )
        self.title_label.pack(side='left', padx=20, pady=12)
        
        # Toolbar
        toolbar = tk.Frame(self.root, bg='#2d2d2d', height=40)
        toolbar.pack(fill='x', padx=0, pady=0)
        toolbar.pack_propagate(False)
        
        buttons = [("New", self.new_file), ("Open", self.open_file),
                   ("Save", self.save_file), ("Save As", self.save_as_file)]
        
        for btn_text, cmd in buttons:
            btn = tk.Button(toolbar, text=btn_text, font=("Segoe UI", 9),
                           bg='#0078d4', fg='white', relief='flat', bd=0,
                           padx=15, command=cmd)
            btn.pack(side='left', padx=5, pady=8)
        
        # Content
        content = tk.Frame(self.root, bg='#1e1e1e')
        content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Paned window
        paned = ttk.PanedWindow(content, orient='horizontal')
        paned.pack(fill='both', expand=True)
        
        # Editor
        editor_frame = tk.Frame(paned, bg='#1e1e1e')
        paned.add(editor_frame, weight=1)
        
        editor_label = tk.Label(editor_frame, text="Editor", font=("Segoe UI", 10, "bold"),
                               fg='#858585', bg='#1e1e1e')
        editor_label.pack(anchor='w', padx=5, pady=5)
        
        scroll = tk.Scrollbar(editor_frame)
        scroll.pack(side='right', fill='y')
        
        self.editor = tk.Text(editor_frame, bg='#252526', fg='#d4d4d4',
                             font=("Consolas", 11), relief='flat', bd=0,
                             yscrollcommand=scroll.set, wrap='word', undo=True)
        self.editor.pack(side='left', fill='both', expand=True)
        scroll.config(command=self.editor.yview)
        self.editor.bind('<KeyRelease>', self.on_text_change)
        
        # Preview
        preview_frame = tk.Frame(paned, bg='#1e1e1e')
        paned.add(preview_frame, weight=1)
        
        preview_label = tk.Label(preview_frame, text="Preview", font=("Segoe UI", 10, "bold"),
                                fg='#858585', bg='#1e1e1e')
        preview_label.pack(anchor='w', padx=5, pady=5)
        
        scroll2 = tk.Scrollbar(preview_frame)
        scroll2.pack(side='right', fill='y')
        
        self.preview = tk.Text(preview_frame, bg='#f5f5f5', fg='#333333',
                              font=("Segoe UI", 10), relief='flat', bd=0,
                              yscrollcommand=scroll2.set, wrap='word', state='disabled')
        self.preview.pack(side='left', fill='both', expand=True)
        scroll2.config(command=self.preview.yview)
        
        # Configure preview tags
        self.preview.tag_configure('h1', font=("Segoe UI", 18, "bold"), foreground='#0078d4')
        self.preview.tag_configure('h2', font=("Segoe UI", 14, "bold"), foreground='#0078d4')
        self.preview.tag_configure('h3', font=("Segoe UI", 12, "bold"), foreground='#0078d4')
        self.preview.tag_configure('bold', font=("Segoe UI", 10, "bold"))
        self.preview.tag_configure('italic', font=("Segoe UI", 10, "italic"))
        self.preview.tag_configure('code', font=("Consolas", 9), background='#f0f0f0')
    
    def on_text_change(self, event=None):
        self.is_modified = True
        self.update_preview()
        self.update_title()
    
    def update_preview(self):
        content = self.editor.get('1.0', 'end-1c')
        self.preview.config(state='normal')
        self.preview.delete('1.0', 'end')
        
        for line in content.split('\n'):
            if line.startswith('# '):
                self.preview.insert('end', line[2:] + '\n', 'h1')
            elif line.startswith('## '):
                self.preview.insert('end', line[3:] + '\n', 'h2')
            elif line.startswith('### '):
                self.preview.insert('end', line[4:] + '\n', 'h3')
            else:
                self.insert_formatted_line(line)
                self.preview.insert('end', '\n')
        
        self.preview.config(state='disabled')
    
    def insert_formatted_line(self, line):
        words = line.split()
        for word in words:
            if word.startswith('**') and word.endswith('**'):
                self.preview.insert('end', word[2:-2], 'bold')
            elif word.startswith('*') and word.endswith('*'):
                self.preview.insert('end', word[1:-1], 'italic')
            elif word.startswith('`') and word.endswith('`'):
                self.preview.insert('end', word[1:-1], 'code')
            else:
                self.preview.insert('end', word)
            self.preview.insert('end', ' ')
    
    def new_file(self):
        if self.is_modified and messagebox.askyesno("Unsaved", "Save changes?"):
            self.save_file()
        self.editor.delete('1.0', 'end')
        self.current_file = None
        self.is_modified = False
        self.update_title()
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown", "*.md"), ("Text", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.editor.delete('1.0', 'end')
                self.editor.insert('1.0', f.read())
            self.current_file = file_path
            self.is_modified = False
            self.update_title()
    
    def save_file(self):
        if not self.current_file:
            self.save_as_file()
            return
        
        with open(self.current_file, 'w', encoding='utf-8') as f:
            f.write(self.editor.get('1.0', 'end-1c'))
        self.is_modified = False
        self.update_title()
        messagebox.showinfo("Success", "File saved!")
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md",
                                                filetypes=[("Markdown", "*.md"), ("Text", "*.txt")])
        if file_path:
            self.current_file = file_path
            self.save_file()
    
    def update_title(self):
        if self.current_file:
            filename = Path(self.current_file).name
            status = " (Modified)" if self.is_modified else ""
            self.title_label.config(text=f"📝 {APP_NAME} - {filename}{status}")
        else:
            status = " (Modified)" if self.is_modified else ""
            self.title_label.config(text=f"📝 {APP_NAME} - Untitled{status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()
