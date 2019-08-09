from utils.util import unique_items

class MetadataItem(object):
	def __init__(self):
		self.metadata = dict()

class Token(MetadataItem):
	def __init__(self, text):
		"""
		:type text: str
		"""
		super(Token, self).__init__()
		self.text = text


class Sentence(MetadataItem):
	def __init__(self, text, token):
		"""
		:typr text: str
		:type tokens: list[Token]
		"""
		super(Sentence, self).__init__()
		self.text = text
		self.tokens = tokens

	@property
	def vocab(self):
		vocab = []
		for token in self.tokens:
			vocab.append(token.text)
		return unique_items(vocab)

class TextItem(MetadataItem):
	def __init__(self, text, sentences):
		"""
		:type text: str
		:type sentences: list[Sentence]
		"""
		super(TextItem, self).__init__()
		self.text = text
		self.sentences = sentences

	@property
	def vocab(self):
		vocab = []
		for sentence in self.sentences:
			vocab += sentence.vocab
		return unique_items(vocab)

class QAPool(object):
	def __init__(self, question, pooled_answers, ground_truth):
		"""
			:type question: TextItem
			:type pooled_answers: list[TextItem]
			:type ground_truth: list[TextItem]
		"""
		self.question = question
		self.pooled_answers = pooled_answers
		self.ground_truth = ground_truth

class Data(object):
	
