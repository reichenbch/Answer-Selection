import math
import utils

import numpy as np
import models
from utils.util import read_embeddings

class QAData(utils.Data):
	def __init__(self, config, config_global, logger):
		super(QAData, self).__init__(config, config_global, logger)

		#public fields
		self.archive = None
		self.vocab_to_index = dict()
		self.embeddings = None
		self.lowercased = self.config.get('lowercased', False)

		self.map_oov = self.config.get('map_oov',False)
		self.map_numbers =  self.config.get('map_numbers',False)

	def _get_reader(self):
		"""
		:rtype: InsuranceQAReader
		"""
		raise NotImplementedError()

	def setup(self):
		self.logger.info('Loading Dataset')
		reader = self._get_reader()
		self.archive = reader.read()

		self.logger.debu('Dataset questions: train={}, dev = {}, test= {}'.format(len(self.archive.train.qa), len(self.archive.valid.qa), [len(t.qa) for t in self.archive.test]))

		embedding_size = self.config_global['embedding_size']

		if('embedding_path' in self.config):
			#Loading initial embeddings
			self.logger.info('Fetching the dataset vocab')
			vocab = self.archive.vocab
			self.logger.info('Loading embeddings (vocab size = {})'.format(len(vocab)))