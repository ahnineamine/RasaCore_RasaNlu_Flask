# # Part 2:Adding dialogue capabilities
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import tensorflow
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.run import serve_application
from rasa_core.utils import EndpointConfig
from settings import Settings

class CoreServer():
	def __init__(self):
		self.agent = None
		self.config = Settings.Settings().getConfig()

	logger = logging.getLogger(__name__)


	def train_dialogue(self, domain_file, model_path, training_data_file):
		fallback = FallbackPolicy(fallback_action_name="utter_default",core_threshold=0.2, nlu_threshold=0.5)
		featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=10)
		self.agent = Agent(domain_file , policies=[MemoizationPolicy(max_history=10), KerasPolicy(epochs = 90, batch_size = 20, validation_split = 0.1), fallback])
		data = self.agent.load_data(training_data_file)
		self.agent.train(data)
		self.agent.persist(model_path)

	def run_dialogue(self, core_model_path, nlu_model_path, serve_forever=True):
		interpreter = RasaNLUInterpreter(nlu_model_path)
		action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
		self.agent = Agent.load(core_model_path, interpreter=interpreter, action_endpoint=action_endpoint)
		#rasa_core.run.serve_application(self.agent ,channel='cmdline')

	def build_core(self):
		if self.agent is None:
			self.train_dialogue(self.config['domain_file_path'], self.config['core_model_path'], self.config['training_core_data_path'])
			self.run_dialogue(self.config['core_model_path'], self.config['default_nlu_model_path'])
		return self.agent

"""
if __name__ == '__main__':
	train_dialogue()
"""
