import sqlite3
from abc import ABC, abstractmethod

class tipe_mobil(ABC):
    @abstractmethod
    def set_tipe(self, tipe):
        pass
    
    @abstractmethod
    def get_data_tipe(self):
        pass

    @abstractmethod
    def delete_tipe_byID(self):
        pass

# tipe = tipe_mobil()
# tipe.tambah_tipe()
# tipe.get_data_tipe()