import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Word:
    esperanto: str
    type: str  # 'noun', 'verb', 'adjective', 'pronoun', 'article'
    properties: dict  # For grammatical properties

class EsperantoGrammar:
    def __init__(self):
        self.nouns = self.load_nouns()
        self.verbs = self.load_verbs()
        self.adjectives = self.load_adjectives()
        self.personal_pronouns = ['mi', 'vi', 'li', 'ŝi', 'ĝi', 'ni', 'vi', 'ili']
        self.articles = ['la']  # Esperanto only has definite article
        self.demonstrative_pronouns = ['tiu', 'tia', 'tio']
        self.possessive_pronouns = ['mia', 'via', 'lia', 'ŝia', 'ĝia', 'nia', 'via', 'ilia']

    def load_nouns(self) -> List[Word]:
        return [
            Word('homo', 'noun', {'number': 'singular'}),
            Word('kato', 'noun', {'number': 'singular'}),
            Word('domo', 'noun', {'number': 'singular'}),
            Word('urbo', 'noun', {'number': 'singular'}),
            Word('floro', 'noun', {'number': 'singular'}),
            Word('infano', 'noun', {'number': 'singular'}),
            Word('viro', 'noun', {'number': 'singular'}),
            Word('virino', 'noun', {'number': 'singular'}),
            Word('libro', 'noun', {'number': 'singular'}),
            Word('lernanto', 'noun', {'number': 'singular'}),
            Word('instrukciisto', 'noun', {'number': 'singular'}),
            Word('lago', 'noun', {'number': 'singular'}),
            Word('rivero', 'noun', {'number': 'singular'}),
            Word('mondo', 'noun', {'number': 'singular'}),
            Word('amiko', 'noun', {'number': 'singular'}),
            Word('frukto', 'noun', {'number': 'singular'}),
            Word('bovo', 'noun', {'number': 'singular'}),
            Word('aŭto', 'noun', {'number': 'singular'}),
            Word('biciklo', 'noun', {'number': 'singular'}),
            Word('teatro', 'noun', {'number': 'singular'}),
            Word('kampo', 'noun', {'number': 'singular'}),
            Word('bildo', 'noun', {'number': 'singular'}),
            Word('filmo', 'noun', {'number': 'singular'}),
            Word('vojo', 'noun', {'number': 'singular'}),
            Word('klubo', 'noun', {'number': 'singular'}),
            Word('laboro', 'noun', {'number': 'singular'}),
            Word('tago', 'noun', {'number': 'singular'}),
            Word('nokto', 'noun', {'number': 'singular'}),
            Word('muziko', 'noun', {'number': 'singular'}),
            Word('horo', 'noun', {'number': 'singular'}),
            Word('lingvo', 'noun', {'number': 'singular'}),
            Word('arto', 'noun', {'number': 'singular'}),
            Word('edzo', 'noun', {'number': 'singular'}),
            Word('edzino', 'noun', {'number': 'singular'}),
            Word('telefono', 'noun', {'number': 'singular'}),
            Word('kafeto', 'noun', {'number': 'singular'}),
            Word('birdo', 'noun', {'number': 'singular'}),
            Word('arbo', 'noun', {'number': 'singular'}),
            Word('luno', 'noun', {'number': 'singular'}),
            Word('suno', 'noun', {'number': 'singular'}),
            Word('nubo', 'noun', {'number': 'singular'}),
            Word('vetero', 'noun', {'number': 'singular'}),
            Word('fiŝo', 'noun', {'number': 'singular'}),
            Word('hundo', 'noun', {'number': 'singular'}),
            Word('patro', 'noun', {'number': 'singular'}),
            Word('patrino', 'noun', {'number': 'singular'}),
            Word('pluvo', 'noun', {'number': 'singular'}),
            Word('mono', 'noun', {'number': 'singular'}),
        ]

    def load_verbs(self) -> List[Word]:
        return [
            Word('manĝi', 'verb', {'transitivity': 'transitive'}),
            Word('vidi', 'verb', {'transitivity': 'transitive'}),
            Word('kuri', 'verb', {'transitivity': 'intransitive'}),
            Word('ludi', 'verb', {'transitivity': 'intransitive'}),
            Word('dormi', 'verb', {'transitivity': 'intransitive'}),
            Word('trinki', 'verb', {'transitivity': 'transitive'}),
            Word('paroli', 'verb', {'transitivity': 'intransitive'}),
            Word('skribi', 'verb', {'transitivity': 'transitive'}),
            Word('legi', 'verb', {'transitivity': 'transitive'}),
            Word('sidi', 'verb', {'transitivity': 'intransitive'}),
            Word('stari', 'verb', {'transitivity': 'intransitive'}),
            Word('iri', 'verb', {'transitivity': 'intransitive'}),
            Word('veni', 'verb', {'transitivity': 'intransitive'}),
            Word('porti', 'verb', {'transitivity': 'transitive'}),
            Word('fari', 'verb', {'transitivity': 'transitive'}),
            Word('preni', 'verb', {'transitivity': 'transitive'}),
            Word('doni', 'verb', {'transitivity': 'transitive'}),
            Word('helpi', 'verb', {'transitivity': 'transitive'}),
            Word('vivi', 'verb', {'transitivity': 'intransitive'}),
            Word('koni', 'verb', {'transitivity': 'transitive'}),
            Word('ami', 'verb', {'transitivity': 'transitive'}),
            Word('pensi', 'verb', {'transitivity': 'intransitive'}),
            Word('esperi', 'verb', {'transitivity': 'intransitive'}),
            Word('kompreni', 'verb', {'transitivity': 'transitive'}),
            Word('aŭdi', 'verb', {'transitivity': 'transitive'}),
            Word('lerni', 'verb', {'transitivity': 'transitive'}),
            Word('instrui', 'verb', {'transitivity': 'transitive'}),
            Word('kisi', 'verb', {'transitivity': 'transitive'}),
            Word('ŝati', 'verb', {'transitivity': 'transitive'}),
            Word('atendi', 'verb', {'transitivity': 'transitive'}),
            Word('renkonti', 'verb', {'transitivity': 'transitive'}),
            Word('gajni', 'verb', {'transitivity': 'transitive'}),
            Word('perdi', 'verb', {'transitivity': 'transitive'}),
            Word('danki', 'verb', {'transitivity': 'transitive'}),
            Word('inviti', 'verb', {'transitivity': 'transitive'}),
            Word('vidi', 'verb', {'transitivity': 'transitive'}),
            Word('montri', 'verb', {'transitivity': 'transitive'}),
            Word('demandi', 'verb', {'transitivity': 'transitive'}),
            Word('respondi', 'verb', {'transitivity': 'transitive'}),
            Word('farti', 'verb', {'transitivity': 'intransitive'}),
            Word('veturi', 'verb', {'transitivity': 'intransitive'}),
            Word('ŝofori', 'verb', {'transitivity': 'intransitive'}),
            Word('bani', 'verb', {'transitivity': 'transitive'}),
            Word('malsani', 'verb', {'transitivity': 'intransitive'}),
            Word('kuiri', 'verb', {'transitivity': 'transitive'}),
            Word('plori', 'verb', {'transitivity': 'intransitive'}),
            Word('ŝanĝi', 'verb', {'transitivity': 'transitive'}),
        ]

    def load_adjectives(self) -> List[Word]:
        return [
            Word('granda', 'adjective', {}),
            Word('bela', 'adjective', {}),
            Word('rapida', 'adjective', {}),
            Word('malnova', 'adjective', {}),
            Word('nova', 'adjective', {}),
            Word('forta', 'adjective', {}),
            Word('malsana', 'adjective', {}),
            Word('juna', 'adjective', {}),
            Word('maljuna', 'adjective', {}),
            Word('saĝa', 'adjective', {}),
            Word('feliĉa', 'adjective', {}),
            Word('malfeliĉa', 'adjective', {}),
            Word('klara', 'adjective', {}),
            Word('malhela', 'adjective', {}),
            Word('varma', 'adjective', {}),
            Word('malvarma', 'adjective', {}),
            Word('facila', 'adjective', {}),
            Word('malfacila', 'adjective', {}),
            Word('alta', 'adjective', {}),
            Word('malalta', 'adjective', {}),
            Word('peza', 'adjective', {}),
            Word('malpeza', 'adjective', {}),
            Word('seka', 'adjective', {}),
            Word('malseka', 'adjective', {}),
            Word('sukcesa', 'adjective', {}),
            Word('malsukcesa', 'adjective', {}),
            Word('lerta', 'adjective', {}),
            Word('mallerta', 'adjective', {}),
            Word('sincera', 'adjective', {}),
            Word('mensoga', 'adjective', {}),
            Word('pacema', 'adjective', {}),
            Word('kolerema', 'adjective', {}),
            Word('bonkora', 'adjective', {}),
            Word('malbonkora', 'adjective', {}),
            Word('diligenta', 'adjective', {}),
            Word('pigra', 'adjective', {}),
            Word('honesta', 'adjective', {}),
            Word('malhonesta', 'adjective', {}),
            Word('zorgema', 'adjective', {}),
            Word('zorgema', 'adjective', {}),
            Word('obeema', 'adjective', {}),
            Word('ribelema', 'adjective', {}),
            Word('trankvila', 'adjective', {}),
            Word('nervozigita', 'adjective', {}),
            Word('fidinda', 'adjective', {}),
            Word('sendanĝera', 'adjective', {}),
            Word('danĝera', 'adjective', {}),
            Word('bona', 'adjective', {}),
            Word('malbona', 'adjective', {}),
        ]

class SentenceGenerator:
    def __init__(self):
        self.grammar = EsperantoGrammar()
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Esperanto Sentence Generator")
        
        # Set theme and configure styles
        style = ttk.Style()
        style.theme_use('clam')  # Use 'clam' theme for a modern look
        
        # Configure custom styles
        style.configure('TLabelframe', padding=10)
        style.configure('TLabelframe.Label', font=('Helvetica', 10, 'bold'))
        style.configure('TLabel', padding=5)
        style.configure('TButton', padding=10)
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        
        # Main container with padding
        main_container = ttk.Frame(self.root, padding="20")
        main_container.pack(fill="both", expand=True)
        
        # Title
        title_label = ttk.Label(main_container, 
                              text="Esperanto Sentence Generator",
                              style='Header.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Subject frame
        subject_frame = ttk.LabelFrame(main_container, text="Subject")
        subject_frame.pack(padx=10, pady=5, fill="x")
        
        # Add padding inside frames
        subject_inner = ttk.Frame(subject_frame, padding=10)
        subject_inner.pack(fill="x")
        
        # Create two-column layout for labels and controls
        label_width = 15  # Consistent width for all labels
        
        # Subject type selection with better layout
        subject_type_frame = ttk.Frame(subject_inner)
        subject_type_frame.pack(fill="x", pady=2)
        ttk.Label(subject_type_frame, text="Subject type:", width=label_width).pack(side="left")
        self.subject_type = ttk.Combobox(subject_type_frame, 
            values=["Personal Pronoun", "Noun Phrase"],
            width=30)
        self.subject_type.set("Personal Pronoun")
        self.subject_type.pack(side="left", padx=(5, 0))
        self.subject_type.bind('<<ComboboxSelected>>', self.update_subject_options)
        
        # Subject options frame with better spacing
        self.subject_options_frame = ttk.Frame(subject_inner)
        self.subject_options_frame.pack(fill="x", pady=5)
        
        # Personal pronoun selection
        self.pronoun_frame = ttk.Frame(self.subject_options_frame)
        ttk.Label(self.pronoun_frame, text="Pronoun:", width=label_width).pack(side="left")
        self.pronoun_var = ttk.Combobox(self.pronoun_frame,
            values=self.grammar.personal_pronouns,
            width=30)
        self.pronoun_var.pack(side="left", padx=(5, 0))
        
        # Noun phrase options
        self.noun_options_frame = ttk.Frame(self.subject_options_frame)
        
        # Article frame
        article_frame = ttk.Frame(self.noun_options_frame)
        article_frame.pack(fill="x", pady=2)
        ttk.Label(article_frame, text="Article:", width=label_width).pack(side="left")
        self.article_var = ttk.Combobox(article_frame,
            values=["None", "la"] + self.grammar.demonstrative_pronouns,
            width=30)
        self.article_var.set("None")
        self.article_var.pack(side="left", padx=(5, 0))
        
        # Adjective frame
        adj_frame = ttk.Frame(self.noun_options_frame)
        adj_frame.pack(fill="x", pady=2)
        ttk.Label(adj_frame, text="Adjective:", width=label_width).pack(side="left")
        self.subject_adj_var = ttk.Combobox(adj_frame,
            values=["None"] + [adj.esperanto for adj in self.grammar.adjectives],
            width=30)
        self.subject_adj_var.set("None")
        self.subject_adj_var.pack(side="left", padx=(5, 0))
        
        # Noun frame
        noun_frame = ttk.Frame(self.noun_options_frame)
        noun_frame.pack(fill="x", pady=2)
        ttk.Label(noun_frame, text="Noun:", width=label_width).pack(side="left")
        self.subject_noun_var = ttk.Combobox(noun_frame,
            values=[noun.esperanto for noun in self.grammar.nouns],
            width=30)
        self.subject_noun_var.pack(side="left", padx=(5, 0))
        
        # Verb frame
        verb_frame = ttk.LabelFrame(main_container, text="Verb")
        verb_frame.pack(padx=10, pady=10, fill="x")
        
        # Add padding inside verb frame
        verb_inner = ttk.Frame(verb_frame, padding=10)
        verb_inner.pack(fill="x")
        
        # Tense frame
        tense_frame = ttk.Frame(verb_inner)
        tense_frame.pack(fill="x", pady=2)
        ttk.Label(tense_frame, text="Tense:", width=label_width).pack(side="left")
        self.tense = ttk.Combobox(tense_frame, 
            values=["Present", "Past", "Future"],
            width=30)
        self.tense.set("Present")
        self.tense.pack(side="left", padx=(5, 0))
        
        # Verb selection frame
        verb_select_frame = ttk.Frame(verb_inner)
        verb_select_frame.pack(fill="x", pady=2)
        ttk.Label(verb_select_frame, text="Verb:", width=label_width).pack(side="left")
        self.verb_var = ttk.Combobox(verb_select_frame,
            values=[verb.esperanto for verb in self.grammar.verbs],
            width=30)
        self.verb_var.pack(side="left", padx=(5, 0))
        
        # Object frame
        object_frame = ttk.LabelFrame(main_container, text="Object")
        object_frame.pack(padx=10, pady=5, fill="x")
        
        # Add padding inside object frame
        object_inner = ttk.Frame(object_frame, padding=10)
        object_inner.pack(fill="x")
        
        # Object type frame
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
        
        # Object pronoun frame
        self.object_pronoun_frame = ttk.Frame(self.object_options_frame)
        ttk.Label(self.object_pronoun_frame, text="Pronoun:", width=label_width).pack(side="left")
        self.object_pronoun_var = ttk.Combobox(self.object_pronoun_frame,
            values=self.grammar.personal_pronouns,
            width=30)
        self.object_pronoun_var.pack(side="left", padx=(5, 0))
        
        # Object noun phrase options
        self.object_noun_frame = ttk.Frame(self.object_options_frame)
        
        # Object article frame
        obj_article_frame = ttk.Frame(self.object_noun_frame)
        obj_article_frame.pack(fill="x", pady=2)
        ttk.Label(obj_article_frame, text="Article:", width=label_width).pack(side="left")
        self.object_article_var = ttk.Combobox(obj_article_frame,
            values=["None", "la"] + self.grammar.demonstrative_pronouns,
            width=30)
        self.object_article_var.set("None")
        self.object_article_var.pack(side="left", padx=(5, 0))
        
        # Object adjective frame
        obj_adj_frame = ttk.Frame(self.object_noun_frame)
        obj_adj_frame.pack(fill="x", pady=2)
        ttk.Label(obj_adj_frame, text="Adjective:", width=label_width).pack(side="left")
        self.object_adj_var = ttk.Combobox(obj_adj_frame,
            values=["None"] + [adj.esperanto for adj in self.grammar.adjectives],
            width=30)
        self.object_adj_var.set("None")
        self.object_adj_var.pack(side="left", padx=(5, 0))
        
        # Object noun frame
        obj_noun_frame = ttk.Frame(self.object_noun_frame)
        obj_noun_frame.pack(fill="x", pady=2)
        ttk.Label(obj_noun_frame, text="Noun:", width=label_width).pack(side="left")
        self.object_noun_var = ttk.Combobox(obj_noun_frame,
            values=[noun.esperanto for noun in self.grammar.nouns],
            width=30)
        self.object_noun_var.pack(side="left", padx=(5, 0))
        
        # Generate button with better styling
        generate_button = ttk.Button(main_container, 
                                   text="Generate Sentence",
                                   command=self.generate_sentence,
                                   style='TButton')
        generate_button.pack(pady=20)
        
        # Result display with better styling
        result_frame = ttk.LabelFrame(main_container, text="Generated Sentence")
        result_frame.pack(padx=10, pady=(0, 10), fill="x")
        
        self.result_var = tk.StringVar()
        result_label = ttk.Label(result_frame, 
                               textvariable=self.result_var,
                               padding=15,
                               font=('Helvetica', 11))
        result_label.pack(fill="x")
        
        # Set minimum window size
        self.root.minsize(500, 700)
        
        # Initial update of subject/object options
        self.update_subject_options(None)
        self.update_object_options(None)

    def update_subject_options(self, event):
        # Clear current options
        for widget in self.subject_options_frame.winfo_children():
            widget.pack_forget()
            
        if self.subject_type.get() == "Personal Pronoun":
            self.pronoun_var.pack(pady=2)
        else:
            self.noun_options_frame.pack(fill="x", pady=2)

    def update_object_options(self, event):
        # Clear current options
        for widget in self.object_options_frame.winfo_children():
            widget.pack_forget()
            
        if self.object_type.get() == "Personal Pronoun":
            self.object_pronoun_var.pack(pady=2)
        elif self.object_type.get() == "Noun Phrase":
            self.object_noun_frame.pack(fill="x", pady=2)

    def generate_sentence(self):
        try:
            # Build subject
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

            # Build verb (add tense markers)
            verb = self.verb_var.get()
            if self.tense.get() == "Past":
                verb = "is " + verb
            elif self.tense.get() == "Future":
                verb = "os " + verb

            # Build object
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

            # Combine all parts
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
