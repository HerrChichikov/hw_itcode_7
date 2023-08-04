class TestMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('до')

        response = self.get_response(request)

        print('после')

        return response