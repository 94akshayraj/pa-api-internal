class VecModel:
    def __init__(self, success, data, error, message):
        self.success = success
        self.data = data
        self.error = error
        self.message = message

    """
    Method to set response for dashboard
    """

    def get_response(self):
        try:
            response = {
                'success': self.success,
                'data': self.data,
                'error': self.error,
                'message': self.message
            }
        except Exception as error:
            print(error)
        finally:
            return response
