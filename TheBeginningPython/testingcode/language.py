from mysurvey import AnonySurvey


question = "What language do you speak?"
survey = AnonySurvey(question)
survey.show_question()
print("Press q to quit")
while True:
    answer = input("Language: ")
    if answer.lower() == "q":
        break
    survey.store_response(answer)
print("Thanks for showing. Here are the results: ")
survey.show_results()