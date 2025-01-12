from logger import logger
from models.svm import SVM
from models.cnn import CNN
from utils.model_storage_manager import ModelStorageManager
from utils.svm_builder import SVMBuilder
from utils.model_analyzer import ModelAnalyzer
from utils.model_plotter import ModelPlotter
from utils.data_transformer import DataTransformer
def main():
    """TODO: Steps..."""
    logger.info("Starting the program...")
    data = DataTransformer("SVM","C:/Users/Shaked/Msc/project/SVM/13AugA/condXnoTarget/condXnoTarget",180).create()
    logger.debug(data)


if __name__ == "__main__":
    main()
