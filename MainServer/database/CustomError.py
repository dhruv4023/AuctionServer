class APIDataFetchError(Exception):
    def __init__(self, message="Failed to fetch data from the API"):
        self.message = message
        super().__init__(self.message)