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

    def execute_operations(self, expression: str) -> Set[str]:
        """Executes set operations based on given expression."""
        if '&' in expression:
            sets = [self._get_set(verb.strip()) for verb in expression.split('&')]
            return set.intersection(*sets)
        elif '|' in expression:
            sets = [self._get_set(verb.strip()) for verb in expression.split('|')]
            return set.union(*sets)
        else:
            return self._get_set(expression.strip())

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
        
        # Available verbs list
        ttk.Label(main_frame, text="Available verbs:").grid(row=0, column=0, sticky=tk.W)
        verbs_text = ", ".join(sorted(self.analyzer.get_all_verbs()))
        verb_display = scrolledtext.ScrolledText(main_frame, width=40, height=3, wrap=tk.WORD)
        verb_display.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        verb_display.insert(tk.END, verbs_text)
        verb_display.config(state='disabled')
        
        # Expression entry
        ttk.Label(main_frame, text="Enter expression:").grid(row=2, column=0, sticky=tk.W)
        self.expression_var = tk.StringVar()
        self.expression_entry = ttk.Entry(main_frame, textvariable=self.expression_var, width=40)
        self.expression_entry.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        # Execute button
        ttk.Button(main_frame, text="Execute", command=self.execute).grid(row=3, column=1, padx=5)
        
        # Results area
        ttk.Label(main_frame, text="Results:").grid(row=4, column=0, sticky=tk.W)
        self.result_text = scrolledtext.ScrolledText(main_frame, width=40, height=5, wrap=tk.WORD)
        self.result_text.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Help text
        help_text = "Use expressions like: 'manĝi'&'trinki' or 'aĉeti'|'vendi'\n& for intersection, | for union"
        ttk.Label(main_frame, text=help_text).grid(row=6, column=0, columnspan=2, sticky=tk.W)
        
        # Configure grid
        for child in main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
    
    def execute(self):
        """Execute the expression and display results."""
        expression = self.expression_var.get()
        try:
            result = self.analyzer.execute_operations(expression)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, ", ".join(sorted(result)))
        except Exception as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = AnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
