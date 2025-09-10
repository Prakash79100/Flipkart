#!/usr/bin/env python3
"""
Modern Python UI Application
A clean, professional GUI application built with tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import font
import os
import json
from datetime import datetime


class ModernUI:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.tasks = []
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Modern Python UI")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
        
        # Configure window icon and styling
        self.root.configure(bg='#f0f0f0')
        
    def setup_styles(self):
        """Configure modern styling"""
        self.style = ttk.Style()
        
        # Configure colors and fonts
        self.colors = {
            'primary': '#2563eb',
            'secondary': '#64748b',
            'success': '#059669',
            'danger': '#dc2626',
            'warning': '#d97706',
            'light': '#f8fafc',
            'dark': '#1e293b',
            'background': '#ffffff'
        }
        
        # Configure custom fonts
        self.fonts = {
            'heading': font.Font(family="Helvetica", size=16, weight="bold"),
            'subheading': font.Font(family="Helvetica", size=12, weight="bold"),
            'body': font.Font(family="Helvetica", size=10),
            'small': font.Font(family="Helvetica", size=9)
        }
        
        # Configure ttk styles
        self.style.theme_use('clam')
        
        # Button styles
        self.style.configure('Primary.TButton',
                           background=self.colors['primary'],
                           foreground='white',
                           borderwidth=0,
                           focuscolor='none',
                           padding=(20, 10))
        
        self.style.map('Primary.TButton',
                      background=[('active', '#1d4ed8')])
        
        self.style.configure('Success.TButton',
                           background=self.colors['success'],
                           foreground='white',
                           borderwidth=0,
                           focuscolor='none',
                           padding=(15, 8))
        
        # Entry styles
        self.style.configure('Modern.TEntry',
                           borderwidth=1,
                           relief='solid',
                           padding=10)
        
        # Frame styles
        self.style.configure('Card.TFrame',
                           background=self.colors['background'],
                           relief='solid',
                           borderwidth=1)
        
    def create_widgets(self):
        """Create and layout all widgets"""
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Main content area with tabs
        self.create_tabs(main_container)
        
        # Footer
        self.create_footer(main_container)
        
    def create_header(self, parent):
        """Create the header section"""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title_label = tk.Label(header_frame, 
                              text="Modern Python UI",
                              font=self.fonts['heading'],
                              bg='#f0f0f0',
                              fg=self.colors['dark'])
        title_label.pack(side=tk.LEFT)
        
        # Header buttons
        btn_frame = ttk.Frame(header_frame)
        btn_frame.pack(side=tk.RIGHT)
        
        ttk.Button(btn_frame, text="Settings", 
                  command=self.open_settings).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(btn_frame, text="Help", 
                  command=self.show_help).pack(side=tk.RIGHT, padx=(5, 0))
        
    def create_tabs(self, parent):
        """Create the tabbed interface"""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Dashboard
        self.create_dashboard_tab()
        
        # Tab 2: Task Manager
        self.create_task_manager_tab()
        
        # Tab 3: File Manager
        self.create_file_manager_tab()
        
        # Tab 4: Calculator
        self.create_calculator_tab()
        
    def create_dashboard_tab(self):
        """Create the dashboard tab"""
        dashboard_frame = ttk.Frame(self.notebook)
        self.notebook.add(dashboard_frame, text="Dashboard")
        
        # Welcome card
        welcome_card = ttk.Frame(dashboard_frame, style='Card.TFrame')
        welcome_card.pack(fill=tk.X, pady=(0, 20), padx=10, ipady=20)
        
        welcome_label = tk.Label(welcome_card,
                                text="Welcome to Modern Python UI",
                                font=self.fonts['subheading'],
                                bg=self.colors['background'])
        welcome_label.pack(pady=10)
        
        description = tk.Label(welcome_card,
                              text="This is a modern, clean UI built with Python and tkinter.\n"
                                   "Explore the different tabs to see various features.",
                              font=self.fonts['body'],
                              bg=self.colors['background'],
                              fg=self.colors['secondary'],
                              justify=tk.CENTER)
        description.pack(pady=5)
        
        # Quick actions
        actions_frame = ttk.Frame(dashboard_frame)
        actions_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(actions_frame, text="Quick Actions", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        buttons_frame = ttk.Frame(actions_frame)
        buttons_frame.pack(fill=tk.X)
        
        ttk.Button(buttons_frame, text="New Task", 
                  style='Primary.TButton',
                  command=lambda: self.notebook.select(1)).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Open File", 
                  command=self.open_file).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(buttons_frame, text="Calculator", 
                  command=lambda: self.notebook.select(3)).pack(side=tk.LEFT)
        
        # Stats cards
        stats_frame = ttk.Frame(dashboard_frame)
        stats_frame.pack(fill=tk.X, pady=20)
        
        tk.Label(stats_frame, text="Statistics", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        stats_container = ttk.Frame(stats_frame)
        stats_container.pack(fill=tk.X)
        
        # Create stat cards
        self.create_stat_card(stats_container, "Tasks", "0", self.colors['primary'])
        self.create_stat_card(stats_container, "Files", "0", self.colors['success'])
        self.create_stat_card(stats_container, "Sessions", "1", self.colors['warning'])
        
    def create_stat_card(self, parent, title, value, color):
        """Create a statistics card"""
        card = ttk.Frame(parent, style='Card.TFrame')
        card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=5)
        
        # Color indicator
        indicator = tk.Frame(card, bg=color, height=4)
        indicator.pack(fill=tk.X, pady=(0, 10))
        
        value_label = tk.Label(card, text=value, font=self.fonts['heading'],
                              bg=self.colors['background'], fg=color)
        value_label.pack(pady=5)
        
        title_label = tk.Label(card, text=title, font=self.fonts['body'],
                              bg=self.colors['background'], fg=self.colors['secondary'])
        title_label.pack(pady=(0, 10))
        
    def create_task_manager_tab(self):
        """Create the task manager tab"""
        task_frame = ttk.Frame(self.notebook)
        self.notebook.add(task_frame, text="Task Manager")
        
        # Task input section
        input_frame = ttk.Frame(task_frame)
        input_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        tk.Label(input_frame, text="Add New Task", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        entry_frame = ttk.Frame(input_frame)
        entry_frame.pack(fill=tk.X)
        
        self.task_entry = ttk.Entry(entry_frame, style='Modern.TEntry', font=self.fonts['body'])
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        ttk.Button(entry_frame, text="Add Task", 
                  style='Success.TButton',
                  command=self.add_task).pack(side=tk.RIGHT)
        
        # Task list
        list_frame = ttk.Frame(task_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        tk.Label(list_frame, text="Your Tasks", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        # Create treeview for tasks
        self.task_tree = ttk.Treeview(list_frame, columns=('Status', 'Created'), show='tree headings')
        self.task_tree.heading('#0', text='Task')
        self.task_tree.heading('Status', text='Status')
        self.task_tree.heading('Created', text='Created')
        
        self.task_tree.column('#0', width=300)
        self.task_tree.column('Status', width=100)
        self.task_tree.column('Created', width=150)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)
        
        self.task_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Task actions
        actions_frame = ttk.Frame(task_frame)
        actions_frame.pack(fill=tk.X, pady=10, padx=10)
        
        ttk.Button(actions_frame, text="Complete Task", 
                  command=self.complete_task).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(actions_frame, text="Delete Task", 
                  command=self.delete_task).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(actions_frame, text="Clear All", 
                  command=self.clear_all_tasks).pack(side=tk.LEFT)
        
    def create_file_manager_tab(self):
        """Create the file manager tab"""
        file_frame = ttk.Frame(self.notebook)
        self.notebook.add(file_frame, text="File Manager")
        
        # File operations
        ops_frame = ttk.Frame(file_frame)
        ops_frame.pack(fill=tk.X, pady=(0, 20), padx=10)
        
        tk.Label(ops_frame, text="File Operations", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        btn_frame = ttk.Frame(ops_frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Open File", 
                  command=self.open_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Save Data", 
                  command=self.save_data).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Load Data", 
                  command=self.load_data).pack(side=tk.LEFT)
        
        # File content display
        content_frame = ttk.Frame(file_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        tk.Label(content_frame, text="File Content", 
                font=self.fonts['subheading'], bg='#f0f0f0').pack(anchor=tk.W, pady=(0, 10))
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(content_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        self.file_text = tk.Text(text_frame, wrap=tk.WORD, font=self.fonts['body'])
        text_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.file_text.yview)
        self.file_text.configure(yscrollcommand=text_scrollbar.set)
        
        self.file_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_calculator_tab(self):
        """Create the calculator tab"""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="Calculator")
        
        # Calculator display
        display_frame = ttk.Frame(calc_frame)
        display_frame.pack(fill=tk.X, pady=20, padx=20)
        
        self.calc_display = tk.Entry(display_frame, font=('Courier', 16), 
                                   justify=tk.RIGHT, state='readonly',
                                   readonlybackground='white')
        self.calc_display.pack(fill=tk.X, pady=(0, 20))
        
        # Calculator buttons
        buttons_frame = ttk.Frame(calc_frame)
        buttons_frame.pack(pady=20, padx=20)
        
        self.calc_expression = ""
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            row_frame = ttk.Frame(buttons_frame)
            row_frame.pack(fill=tk.X, pady=2)
            
            for j, btn_text in enumerate(row):
                if btn_text == '0' and i == 4:  # Make 0 button wider
                    btn = tk.Button(row_frame, text=btn_text, font=self.fonts['subheading'],
                                  command=lambda t=btn_text: self.calc_button_click(t),
                                  width=10, height=2)
                    btn.pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
                elif btn_text == '=' and i == 4:
                    btn = tk.Button(row_frame, text=btn_text, font=self.fonts['subheading'],
                                  command=lambda t=btn_text: self.calc_button_click(t),
                                  width=5, height=2, bg=self.colors['primary'], fg='white')
                    btn.pack(side=tk.RIGHT, padx=2)
                else:
                    btn = tk.Button(row_frame, text=btn_text, font=self.fonts['subheading'],
                                  command=lambda t=btn_text: self.calc_button_click(t),
                                  width=5, height=2)
                    btn.pack(side=tk.LEFT, padx=2)
        
    def create_footer(self, parent):
        """Create the footer section"""
        footer_frame = ttk.Frame(parent)
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_label = tk.Label(footer_frame, 
                               textvariable=self.status_var,
                               font=self.fonts['small'],
                               bg='#f0f0f0',
                               fg=self.colors['secondary'])
        status_label.pack(side=tk.LEFT)
        
        # Current time
        self.time_var = tk.StringVar()
        self.update_time()
        
        time_label = tk.Label(footer_frame,
                             textvariable=self.time_var,
                             font=self.fonts['small'],
                             bg='#f0f0f0',
                             fg=self.colors['secondary'])
        time_label.pack(side=tk.RIGHT)
        
    def update_time(self):
        """Update the time display"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_var.set(current_time)
        self.root.after(1000, self.update_time)
        
    def add_task(self):
        """Add a new task"""
        task_text = self.task_entry.get().strip()
        if task_text:
            task_id = len(self.tasks)
            created_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            self.task_tree.insert('', 'end', iid=task_id,
                                 text=task_text,
                                 values=('Pending', created_time))
            
            self.tasks.append({
                'id': task_id,
                'text': task_text,
                'status': 'Pending',
                'created': created_time
            })
            
            self.task_entry.delete(0, tk.END)
            self.status_var.set(f"Task added: {task_text}")
            self.update_task_count()
        
    def complete_task(self):
        """Mark selected task as complete"""
        selected = self.task_tree.selection()
        if selected:
            item_id = selected[0]
            self.task_tree.set(item_id, 'Status', 'Completed')
            
            # Update tasks list
            for task in self.tasks:
                if str(task['id']) == item_id:
                    task['status'] = 'Completed'
                    break
                    
            self.status_var.set("Task completed")
        
    def delete_task(self):
        """Delete selected task"""
        selected = self.task_tree.selection()
        if selected:
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
                item_id = selected[0]
                self.task_tree.delete(item_id)
                
                # Remove from tasks list
                self.tasks = [task for task in self.tasks if str(task['id']) != item_id]
                
                self.status_var.set("Task deleted")
                self.update_task_count()
        
    def clear_all_tasks(self):
        """Clear all tasks"""
        if self.tasks and messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all tasks?"):
            for item in self.task_tree.get_children():
                self.task_tree.delete(item)
            self.tasks.clear()
            self.status_var.set("All tasks cleared")
            self.update_task_count()
        
    def update_task_count(self):
        """Update task count in dashboard"""
        # This would update the dashboard stats
        pass
        
    def open_file(self):
        """Open and display a file"""
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.file_text.delete(1.0, tk.END)
                    self.file_text.insert(1.0, content)
                    self.status_var.set(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
        
    def save_data(self):
        """Save current data to file"""
        file_path = filedialog.asksaveasfilename(
            title="Save Data",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                data = {
                    'tasks': self.tasks,
                    'timestamp': datetime.now().isoformat()
                }
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=2)
                    
                self.status_var.set(f"Data saved to: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save data:\n{str(e)}")
        
    def load_data(self):
        """Load data from file"""
        file_path = filedialog.askopenfilename(
            title="Load Data",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                if 'tasks' in data:
                    # Clear current tasks
                    for item in self.task_tree.get_children():
                        self.task_tree.delete(item)
                    
                    # Load tasks
                    self.tasks = data['tasks']
                    for task in self.tasks:
                        self.task_tree.insert('', 'end', iid=task['id'],
                                            text=task['text'],
                                            values=(task['status'], task['created']))
                    
                    self.status_var.set(f"Data loaded from: {os.path.basename(file_path)}")
                else:
                    messagebox.showwarning("Warning", "No valid task data found in file")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Could not load data:\n{str(e)}")
        
    def calc_button_click(self, value):
        """Handle calculator button clicks"""
        if value == 'C':
            self.calc_expression = ""
        elif value == '=':
            try:
                # Replace display symbols with Python operators
                expression = self.calc_expression.replace('×', '*').replace('÷', '/').replace('−', '-')
                result = str(eval(expression))
                self.calc_expression = result
            except:
                self.calc_expression = "Error"
        elif value == '±':
            if self.calc_expression and self.calc_expression != "Error":
                if self.calc_expression.startswith('-'):
                    self.calc_expression = self.calc_expression[1:]
                else:
                    self.calc_expression = '-' + self.calc_expression
        else:
            if self.calc_expression == "Error":
                self.calc_expression = ""
            self.calc_expression += value
            
        # Update display
        self.calc_display.config(state='normal')
        self.calc_display.delete(0, tk.END)
        self.calc_display.insert(0, self.calc_expression)
        self.calc_display.config(state='readonly')
        
    def open_settings(self):
        """Open settings dialog"""
        messagebox.showinfo("Settings", "Settings panel coming soon!")
        
    def show_help(self):
        """Show help dialog"""
        help_text = """Modern Python UI Help

Dashboard: Overview of your activities and quick actions
Task Manager: Create, manage, and track your tasks
File Manager: Open, view, and manage files
Calculator: Basic calculator functionality

Features:
- Modern, clean interface
- Task management with status tracking
- File operations (open, save, load)
- Built-in calculator
- Real-time clock display

Created with Python and tkinter"""
        
        messagebox.showinfo("Help", help_text)
        
    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = ModernUI()
    app.run()