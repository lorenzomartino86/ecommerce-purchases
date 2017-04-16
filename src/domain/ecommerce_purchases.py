import pandas

class EcommercePurchases(object):
    def create_data_frame(self, repository):
        purchases_repository = repository.get_purchases()
        self.data_frame = pandas.read_csv(purchases_repository)

    def get_data_frame(self, rows=None):
        if self.data_frame is None:
            raise ValueError("dataframe not initialized")
        if rows is None:
            return self.data_frame
        if rows > 0:
            return self.data_frame.head(rows)
        if rows < 0:
            return self.data_frame.tail(rows)