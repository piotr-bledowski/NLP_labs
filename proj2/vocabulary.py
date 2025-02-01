from dataclasses import dataclass
from typing import List

@dataclass
class Word:
    esperanto: str
    type: str
    properties: dict

class EsperantoVocabulary:
    def __init__(self):
        self.personal_pronouns = ['mi', 'vi', 'li', 'ŝi', 'ĝi', 'ni', 'vi', 'ili']
        self.articles = ['la']
        self.demonstrative_pronouns = ['tiu', 'tia', 'tio']
        self.possessive_pronouns = ['mia', 'via', 'lia', 'ŝia', 'ĝia', 'nia', 'via', 'ilia']
        self.nouns = self.load_nouns()
        self.verbs = self.load_verbs()
        self.adjectives = self.load_adjectives()

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
            Word('ŝanĝi', 'verb', {'transitivity': 'transitive'})
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
