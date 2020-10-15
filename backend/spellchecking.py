from rasa_nlu.components import Component
from rasa_nlu import utils
from rasa_nlu.model import Metadata

from spellchecker import SpellChecker
spell = SpellChecker()
spell = SpellChecker(language='fr')
spell.word_frequency.load_text_file('./dict.txt')
spell.word_frequency.remove('salit')

class CorrectSpelling(Component):

    name = "Spell_checker"
    provides = ["text"]
    #requires = ["message"]
    language_list = ["fr"]

    def __init__(self, component_config=None):
        super(CorrectSpelling, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def process(self, message, **kwargs):
        """Retrieve the text message, do spelling correction word by word,
        then append all the words and form the sentence,
        pass it to next component of pipeline"""

        textdata = message.text
        textdata = textdata.split()
        new_message = ' '.join(spell.correction(w) for w in textdata)
        message.text = new_message

    def persist(self,file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass
