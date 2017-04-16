from abc import abstractmethod

class PurchasesRepository:

    @abstractmethod
    def get_purchases(self): raise NotImplementedError