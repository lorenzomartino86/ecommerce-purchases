from src.domain.port.purchases_repository import PurchasesRepository

class FilePurchasesRepository(PurchasesRepository):

    def __init__(self, location):
        self.location = location

    def getPurchases(self):
        return self.location


