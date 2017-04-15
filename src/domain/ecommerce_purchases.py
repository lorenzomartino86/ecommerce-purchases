import pandas as pd


class EcommercePurchases(object):
    def createDataFrame(self, repository):
        purchasesRepository = repository.getPurchases()
        self.df = pd.read_csv(purchasesRepository)