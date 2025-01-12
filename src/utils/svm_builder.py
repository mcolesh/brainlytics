"""A utility class for creating SVMi models"""


class SVMBuilder:
    """A utility class for creating SVMi models"""

    def __init__(self):
        pass

    def build(self, frame_i, ws, data):
        """Building SVMi:
        Create a SVM model, train it with labeled frames j, ws<=j<=i to i+ws-1

        Args:
            frame_i (int): The starting frame.
            ws (int): The window size.
            data (TODO): The raw MATLAB output data.

        returns:
        Trained SVMi
        """
