class ComponentBase(object):
    def __init__(self, config, config_global, logger):
	    """This is a simple base object for all experiment components
        	
            :type config: dict
            :type config_global: dict
            :type logger: logging.Logger
        """

        self.config =  config or dict()
        self.config_global = config_global or dict()
        self.logger = logger

class Data(ComponentBase):
    def setup(self):
        pass

    def get_fold_data(self, fold_i, n_folds):
        """Generates and returns a new Data instance that contains only the data for a specific fold.
            This method is used for hyperparameter optimization on multiple folds.
        """
