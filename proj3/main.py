import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import defaultdict
from typing import Dict, Set
from verb_noun_sets import DATA

class TextAnalyzer:
    def __init__(self):
        self.verbs_nouns: Dict[str, Set[str]] = defaultdict(set)
        self._initialize_test_data()
    
    def _initialize_test_data(self):
        """Initialize with sample Esperanto verb-noun pairs."""
        self.verbs_nouns.update(DATA)

    def execute_operations(self, verb1: str, operation: str, verb2: str = None) -> Set[str]:
        """Executes set operations based on given verbs and operation."""
        if operation == "show":
            return self._get_set(verb1)
        elif operation == "intersection" and verb2:
            return self._get_set(verb1) & self._get_set(verb2)
        elif operation == "union" and verb2:
            return self._get_set(verb1) | self._get_set(verb2)
        return set()

    def _get_set(self, verb: str) -> Set[str]:
        """Returns set of nouns for given verb."""
        return self.verbs_nouns.get(verb, set())
    
    def get_all_verbs(self) -> Set[str]:
        """Returns all available verbs."""
        return set(self.verbs_nouns.keys())

class AnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.analyzer = TextAnalyzer()
        self.root.title("Esperanto Verb-Noun Analyzer")
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 10))
        self.style.configure('TButton', 
                           background='#4a90e2', 
                           foreground='white',
                           font=('Helvetica', 10, 'bold'),
                           padding=10)
        self.style.configure('Header.TLabel', 
                           font=('Helvetica', 12, 'bold'),
                           foreground='#2c3e50',
                           background='#f0f0f0')
        self.style.configure('Results.TLabel', 
                           font=('Helvetica', 11),
                           foreground='#2c3e50',
                           background='#f0f0f0')
        
        # Configure root window
        self.root.configure(background='#f0f0f0')
        self.root.geometry('500x600')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20", style='TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, 
                              text="Esperanto Verb-Noun Analysis Tool", 
                              style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # First verb selection
        ttk.Label(main_frame, text="First verb:", style='TLabel').grid(row=1, column=0, sticky=tk.W)
        self.verb1_var = tk.StringVar()
        verbs = sorted(self.analyzer.get_all_verbs())
        self.verb1_combo = ttk.Combobox(main_frame, 
                                      textvariable=self.verb1_var, 
                                      values=verbs, 
                                      width=30)
        self.verb1_combo.grid(row=1, column=1, sticky=(tk.W, tk.E))
        if verbs:
            self.verb1_combo.set(verbs[0])
        
        # Operation selection
        ttk.Label(main_frame, text="Operation:", style='TLabel').grid(row=2, column=0, sticky=tk.W)
        self.operation_var = tk.StringVar()
        operations = ["show", "intersection", "union"]
        self.operation_combo = ttk.Combobox(main_frame, 
                                          textvariable=self.operation_var, 
                                          values=operations, 
                                          width=30)
        self.operation_combo.grid(row=2, column=1, sticky=(tk.W, tk.E))
        self.operation_combo.set(operations[0])
        self.operation_combo.bind('<<ComboboxSelected>>', self._on_operation_change)
        
        # Second verb selection
        ttk.Label(main_frame, text="Second verb:", style='TLabel').grid(row=3, column=0, sticky=tk.W)
        self.verb2_var = tk.StringVar()
        self.verb2_combo = ttk.Combobox(main_frame, 
                                      textvariable=self.verb2_var, 
                                      values=verbs, 
                                      width=30, 
                                      state='disabled')
        self.verb2_combo.grid(row=3, column=1, sticky=(tk.W, tk.E))
        if verbs:
            self.verb2_combo.set(verbs[0])
        
        # Execute button
        execute_button = ttk.Button(main_frame, 
                                  text="Execute Analysis", 
                                  command=self.execute,
                                  style='TButton')
        execute_button.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Results area
        ttk.Label(main_frame, text="Results:", style='Results.TLabel').grid(row=5, column=0, sticky=tk.W)
        self.result_text = scrolledtext.ScrolledText(
            main_frame, 
            width=40, 
            height=10, 
            wrap=tk.WORD,
            font=('Helvetica', 10),
            background='white',
            foreground='#2c3e50'
        )
        self.result_text.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Help text
        help_frame = ttk.Frame(main_frame, style='TFrame')
        help_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0), sticky=(tk.W, tk.E))
        
        help_text = ("Instructions:\n"
                    "• Select a verb to see its associated nouns\n"
                    "• Use intersection (∩) to find common nouns between verbs\n"
                    "• Use union (∪) to see all nouns from both verbs")
        help_label = ttk.Label(help_frame, 
                             text=help_text, 
                             style='TLabel',
                             justify=tk.LEFT)
        help_label.pack(anchor=tk.W)
        
        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Add padding to all children
        for child in main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
    
    def _on_operation_change(self, event=None):
        """Enable/disable second verb based on operation selection."""
        if self.operation_var.get() == "show":
            self.verb2_combo.config(state='disabled')
        else:
            self.verb2_combo.config(state='normal')
    
    def execute(self):
        """Execute the operation and display results."""
        try:
            verb1 = self.verb1_var.get()
            operation = self.operation_var.get()
            verb2 = self.verb2_var.get() if operation != "show" else None
            
            result = self.analyzer.execute_operations(verb1, operation, verb2)
            
            self.result_text.delete(1.0, tk.END)
            if result:
                self.result_text.insert(tk.END, ", ".join(sorted(result)))
            else:
                self.result_text.insert(tk.END, "No results found")
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = AnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
