"""A utility class for saving and loading models to and from a local directory."""

import pickle


class ModelStorageManager:
    """A utility class for saving and loading models to and from a local directory."""

    def __init__(self):
        self.models = {}

    def load_model(self, model_path, model_type):
        """Load a model from a given path."""
        with open(model_path, "rb") as f:
            self.models[model_type] = pickle.load(f)
        print(f"{model_type.upper()} model loaded from {model_path}")

    def save_model(self, model, model_path, model_type):
        """Save a model to the given path."""
        with open(model_path, "wb") as f:
            pickle.dump(model, f)
        print(f"{model_type.upper()} model saved to {model_path}")

    def get_model(self, model_type):
        """Return the loaded model."""
        return self.models.get(model_type, None)
