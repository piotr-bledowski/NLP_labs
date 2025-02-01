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
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # First verb selection
        ttk.Label(main_frame, text="First verb:").grid(row=0, column=0, sticky=tk.W)
        self.verb1_var = tk.StringVar()
        verbs = sorted(self.analyzer.get_all_verbs())
        self.verb1_combo = ttk.Combobox(main_frame, textvariable=self.verb1_var, values=verbs, width=20)
        self.verb1_combo.grid(row=0, column=1, sticky=(tk.W, tk.E))
        if verbs:
            self.verb1_combo.set(verbs[0])
        
        # Operation selection
        ttk.Label(main_frame, text="Operation:").grid(row=1, column=0, sticky=tk.W)
        self.operation_var = tk.StringVar()
        operations = ["show", "intersection", "union"]
        self.operation_combo = ttk.Combobox(main_frame, textvariable=self.operation_var, 
                                          values=operations, width=20)
        self.operation_combo.grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.operation_combo.set(operations[0])
        self.operation_combo.bind('<<ComboboxSelected>>', self._on_operation_change)
        
        # Second verb selection
        ttk.Label(main_frame, text="Second verb:").grid(row=2, column=0, sticky=tk.W)
        self.verb2_var = tk.StringVar()
        self.verb2_combo = ttk.Combobox(main_frame, textvariable=self.verb2_var, 
                                       values=verbs, width=20, state='disabled')
        self.verb2_combo.grid(row=2, column=1, sticky=(tk.W, tk.E))
        if verbs:
            self.verb2_combo.set(verbs[0])
        
        # Execute button
        ttk.Button(main_frame, text="Execute", command=self.execute).grid(row=3, column=0, 
                                                                        columnspan=2, pady=10)
        
        # Results area
        ttk.Label(main_frame, text="Results:").grid(row=4, column=0, sticky=tk.W)
        self.result_text = scrolledtext.ScrolledText(main_frame, width=40, height=5, wrap=tk.WORD)
        self.result_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Help text
        help_text = ("Select a verb to see its nouns.\n"
                    "Use intersection (∩) to find common nouns between two verbs.\n"
                    "Use union (∪) to combine nouns from two verbs.")
        ttk.Label(main_frame, text=help_text).grid(row=6, column=0, columnspan=2, sticky=tk.W)
        
        # Configure grid
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
