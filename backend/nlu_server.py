# # Part-1:Add Natural Language understanding(create NLU  model)

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config
import pprint
from settings import Settings
import spacy
#print(spacy.load("fr")("Salut"))

class NluServer():
	def __init__(self):
		self.interpreter = None
		self.config = Settings.Settings().getConfig()


	def train(self, data, configs, model_dir, model_name):
		training_data=load_data(data)																#load NLU training sample
		trainer = Trainer(config.load(configs))														#train the pipeline first
		self.interpreter = trainer.train(training_data)													#train the model
		model_directory = trainer.persist(model_dir,fixed_model_name=model_name)					#store in directory

	def run(self, default_model_dir):
		self.interpreter = Interpreter.load(default_model_dir)
		#pprint.pprint(interpreter.parse("j'aimerai bien établir un dossier de maladie"))

	def build_nlu(self):
		if self.interpreter is None:
			self.train(self.config['training_nlu_data_path'], self.config['rasa_config'], self.config['nlu_model_path'], self.config['nlu_model_name'])
			self.run(self.config['default_nlu_model_path'])


#if __name__ == '__main__':
	#train_nlu('./data/nlu.md', './config.yml', './models/nlu')
	#run_nlu()
