from abc import abstractmethod, ABC

class CacheInterface(ABC):

    def __init__(self,connection):
        self.connection = connection

    @abstractmethod
    def set(self,data:dict):
        pass

    @abstractmethod
    def get(self,key):
        pass