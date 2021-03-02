from interfaces.cache_interface import CacheInterface

class Cache(CacheInterface):

    def __init__(self,connection):
        super().__init__(connection)

    def set(self,data:dict):
        key = next(iter(data))
        self.connection.set(key,data.get(key))
    
    def get(self,key):
        return self.connection.get(key)