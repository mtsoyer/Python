import unittest
from mysurvey import AnonySurvey


class SurveyTest(unittest.TestCase):
    
    def setUp(self):
        question = "What language do you speak?"
        self.survey = AnonySurvey(question)
        self.answer = ["English", "Afrikaans", "Kantonese"]
    
    def test__surveyone(self):
        self.assertEqual(self.answer[0], "English")

    def test_surveythree(self):
        for response in self.answer:
            self.survey.store_response(response)
        for response in self.answer:
            self.assertIn(response, self.survey.responses)


if __name__ == "__main__":
    unittest.main()
