from abc import abstractmethod, ABC


class Page(ABC):
    """
    Abstract class that defines the functions that need to be implemented by all the other pages
    """

    def __init__(self):
        # self.page_name = page_name
        pass

    @abstractmethod
    def load_page(self):
        pass

    @abstractmethod
    def main(self):
        pass
