import pandas

class EcommercePurchases(object):
    def create_data_frame(self, repository):
        purchases_repository = repository.get_purchases()
        self.data_frame = pandas.read_csv(purchases_repository)

    def get_data_frame(self):
        if self.data_frame is None:
            raise ValueError("dataframe not initialized")
        return self.data_frame

    def get_first_rows_data_frame(self, rows):
        if self.data_frame is None:
            raise ValueError("dataframe not initialized")
        return self.data_frame.head(rows)