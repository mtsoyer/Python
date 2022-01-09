class AnonySurvey():
    """
    collects anonymous answers to a survey
    """

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)


    def store_response(self, response):
        self.responses.append(response)


    def show_results(self):
        print("These are the survey responses")
        for response in self.responses:
            print(response)
