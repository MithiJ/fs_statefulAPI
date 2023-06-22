class Data:
    def __init__(self, initial_data):
        self.data = initial_data.copy()
        self.last_step = initial_data.copy()
        # This should actually take in the parameters and load data from data store

    def get_data(self):
        return self.data.copy()
    
    def set_data(self, new_data):
        self.data = new_data.copy()
