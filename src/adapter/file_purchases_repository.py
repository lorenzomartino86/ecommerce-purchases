from src.domain.port.purchases_repository import PurchasesRepository

class FilePurchasesRepository(PurchasesRepository):
    def getPurchases(self):
        return "resources/EcommercePurchases.csv"


