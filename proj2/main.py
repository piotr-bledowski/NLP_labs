import tkinter as tk
from tkinter import ttk
from vocabulary import EsperantoVocabulary

class SentenceGenerator:
    def __init__(self):
        self.vocab = EsperantoVocabulary()
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Esperanto Sentence Generator")
        
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('TLabelframe', padding=10)
        style.configure('TLabelframe.Label', font=('Helvetica', 10, 'bold'))
        style.configure('TLabel', padding=5)
        style.configure('TButton', padding=10)
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        
        main_container = ttk.Frame(self.root, padding="20")
        main_container.pack(fill="both", expand=True)
        
        title_label = ttk.Label(main_container, text="Esperanto Sentence Generator", style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        subject_frame = ttk.LabelFrame(main_container, text="Subject")
        subject_frame.pack(padx=10, pady=5, fill="x")
        
        subject_inner = ttk.Frame(subject_frame, padding=10)
        subject_inner.pack(fill="x")
        
        label_width = 15
        
        subject_type_frame = ttk.Frame(subject_inner)
        subject_type_frame.pack(fill="x", pady=2)
        ttk.Label(subject_type_frame, text="Subject type:", width=label_width).pack(side="left")
        self.subject_type = ttk.Combobox(subject_type_frame, 
            values=["Personal Pronoun", "Noun Phrase"],
            width=30)
        self.subject_type.set("Personal Pronoun")
        self.subject_type.pack(side="left", padx=(5, 0))
        self.subject_type.bind('<<ComboboxSelected>>', self.update_subject_options)
        
        self.subject_options_frame = ttk.Frame(subject_inner)
        self.subject_options_frame.pack(fill="x", pady=5)
        
        self.pronoun_frame = ttk.Frame(self.subject_options_frame)
        ttk.Label(self.pronoun_frame, text="Pronoun:", width=label_width).pack(side="left")
        self.pronoun_var = ttk.Combobox(self.pronoun_frame,
            values=self.vocab.personal_pronouns,
            width=30)
        self.pronoun_var.pack(side="left", padx=(5, 0))
        
        self.noun_options_frame = ttk.Frame(self.subject_options_frame)
        
        article_frame = ttk.Frame(self.noun_options_frame)
        article_frame.pack(fill="x", pady=2)
        ttk.Label(article_frame, text="Article:", width=label_width).pack(side="left")
        self.article_var = ttk.Combobox(article_frame,
            values=["None", "la"] + self.vocab.demonstrative_pronouns,
            width=30)
        self.article_var.set("None")
        self.article_var.pack(side="left", padx=(5, 0))
        
        adj_frame = ttk.Frame(self.noun_options_frame)
        adj_frame.pack(fill="x", pady=2)
        ttk.Label(adj_frame, text="Adjective:", width=label_width).pack(side="left")
        self.subject_adj_var = ttk.Combobox(adj_frame,
            values=["None"] + [adj.esperanto for adj in self.vocab.adjectives],
            width=30)
        self.subject_adj_var.set("None")
        self.subject_adj_var.pack(side="left", padx=(5, 0))
        
        noun_frame = ttk.Frame(self.noun_options_frame)
        noun_frame.pack(fill="x", pady=2)
        ttk.Label(noun_frame, text="Noun:", width=label_width).pack(side="left")
        self.subject_noun_var = ttk.Combobox(noun_frame,
            values=[noun.esperanto for noun in self.vocab.nouns],
            width=30)
        self.subject_noun_var.pack(side="left", padx=(5, 0))
        
        verb_frame = ttk.LabelFrame(main_container, text="Verb")
        verb_frame.pack(padx=10, pady=10, fill="x")
        
        verb_inner = ttk.Frame(verb_frame, padding=10)
        verb_inner.pack(fill="x")
        
        tense_frame = ttk.Frame(verb_inner)
        tense_frame.pack(fill="x", pady=2)
        ttk.Label(tense_frame, text="Tense:", width=label_width).pack(side="left")
        self.tense = ttk.Combobox(tense_frame, 
            values=["Present", "Past", "Future"],
            width=30)
        self.tense.set("Present")
        self.tense.pack(side="left", padx=(5, 0))
        
        verb_select_frame = ttk.Frame(verb_inner)
        verb_select_frame.pack(fill="x", pady=2)
        ttk.Label(verb_select_frame, text="Verb:", width=label_width).pack(side="left")
        self.verb_var = ttk.Combobox(verb_select_frame,
            values=[verb.esperanto for verb in self.vocab.verbs],
            width=30)
        self.verb_var.pack(side="left", padx=(5, 0))
        
        object_frame = ttk.LabelFrame(main_container, text="Object")
        object_frame.pack(padx=10, pady=5, fill="x")
        
        object_inner = ttk.Frame(object_frame, padding=10)
        object_inner.pack(fill="x")
        
        object_type_frame = ttk.Frame(object_inner)
        object_type_frame.pack(fill="x", pady=2)
        ttk.Label(object_type_frame, text="Object type:", width=label_width).pack(side="left")
        self.object_type = ttk.Combobox(object_type_frame,
            values=["None", "Personal Pronoun", "Noun Phrase"],
            width=30)
        self.object_type.set("None")
        self.object_type.pack(side="left", padx=(5, 0))
        self.object_type.bind('<<ComboboxSelected>>', self.update_object_options)
        
        self.object_options_frame = ttk.Frame(object_inner)
        self.object_options_frame.pack(fill="x", pady=5)
        
        self.object_pronoun_frame = ttk.Frame(self.object_options_frame)
        ttk.Label(self.object_pronoun_frame, text="Pronoun:", width=label_width).pack(side="left")
        self.object_pronoun_var = ttk.Combobox(self.object_pronoun_frame,
            values=self.vocab.personal_pronouns,
            width=30)
        self.object_pronoun_var.pack(side="left", padx=(5, 0))
        
        self.object_noun_frame = ttk.Frame(self.object_options_frame)
        
        obj_article_frame = ttk.Frame(self.object_noun_frame)
        obj_article_frame.pack(fill="x", pady=2)
        ttk.Label(obj_article_frame, text="Article:", width=label_width).pack(side="left")
        self.object_article_var = ttk.Combobox(obj_article_frame,
            values=["None", "la"] + self.vocab.demonstrative_pronouns,
            width=30)
        self.object_article_var.set("None")
        self.object_article_var.pack(side="left", padx=(5, 0))
        
        obj_adj_frame = ttk.Frame(self.object_noun_frame)
        obj_adj_frame.pack(fill="x", pady=2)
        ttk.Label(obj_adj_frame, text="Adjective:", width=label_width).pack(side="left")
        self.object_adj_var = ttk.Combobox(obj_adj_frame,
            values=["None"] + [adj.esperanto for adj in self.vocab.adjectives],
            width=30)
        self.object_adj_var.set("None")
        self.object_adj_var.pack(side="left", padx=(5, 0))
        
        obj_noun_frame = ttk.Frame(self.object_noun_frame)
        obj_noun_frame.pack(fill="x", pady=2)
        ttk.Label(obj_noun_frame, text="Noun:", width=label_width).pack(side="left")
        self.object_noun_var = ttk.Combobox(obj_noun_frame,
            values=[noun.esperanto for noun in self.vocab.nouns],
            width=30)
        self.object_noun_var.pack(side="left", padx=(5, 0))
        
        generate_button = ttk.Button(main_container, 
                                   text="Generate Sentence",
                                   command=self.generate_sentence,
                                   style='TButton')
        generate_button.pack(pady=20)
        
        result_frame = ttk.LabelFrame(main_container, text="Generated Sentence")
        result_frame.pack(padx=10, pady=(0, 10), fill="x")
        
        self.result_var = tk.StringVar()
        result_label = ttk.Label(result_frame, 
                               textvariable=self.result_var,
                               padding=15,
                               font=('Helvetica', 11))
        result_label.pack(fill="x")
        
        self.root.minsize(500, 700)
        
        self.update_subject_options(None)
        self.update_object_options(None)

    def update_subject_options(self, event):
        for widget in self.subject_options_frame.winfo_children():
            widget.pack_forget()
            
        if self.subject_type.get() == "Personal Pronoun":
            self.pronoun_var.pack(pady=2)
        else:
            self.noun_options_frame.pack(fill="x", pady=2)

    def update_object_options(self, event):
        for widget in self.object_options_frame.winfo_children():
            widget.pack_forget()
            
        if self.object_type.get() == "Personal Pronoun":
            self.object_pronoun_var.pack(pady=2)
        elif self.object_type.get() == "Noun Phrase":
            self.object_noun_frame.pack(fill="x", pady=2)

    def generate_sentence(self):
        try:
            if self.subject_type.get() == "Personal Pronoun":
                subject = self.pronoun_var.get()
            else:
                subject_parts = []
                if self.article_var.get() != "None":
                    subject_parts.append(self.article_var.get())
                if self.subject_adj_var.get() != "None":
                    subject_parts.append(self.subject_adj_var.get())
                subject_parts.append(self.subject_noun_var.get())
                subject = " ".join(subject_parts)

            verb = self.verb_var.get()
            if self.tense.get() == "Past":
                verb = "is " + verb
            elif self.tense.get() == "Future":
                verb = "os " + verb

            if self.object_type.get() == "None":
                object_phrase = ""
            elif self.object_type.get() == "Personal Pronoun":
                object_phrase = self.object_pronoun_var.get()
            else:
                object_parts = []
                if self.object_article_var.get() != "None":
                    object_parts.append(self.object_article_var.get())
                if self.object_adj_var.get() != "None":
                    object_parts.append(self.object_adj_var.get())
                object_parts.append(self.object_noun_var.get())
                object_phrase = " ".join(object_parts)

            sentence_parts = [subject, verb]
            if object_phrase:
                sentence_parts.append(object_phrase)
            
            self.result_var.set(" ".join(sentence_parts))
        except:
            self.result_var.set("Please fill in all required fields")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    generator = SentenceGenerator()
    generator.run()
