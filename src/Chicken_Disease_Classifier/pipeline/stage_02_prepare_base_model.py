from Chicken_Disease_Classifier.config.configuration import ConfigurationManager
from Chicken_Disease_Classifier.components.prepare_base_model import PrepareBaseModel
from Chicken_Disease_Classifier import logger


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()