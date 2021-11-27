# Ask a question
# User will provide the answer
# check answer is correct or wrong
# if answer is correct continue asking questions
# else stop the game


from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
# Creating a list of question objects
for i in range(0, len(question_data)):
    q = question_data[i]["text"]
    a = question_data[i]["answer"]
    new_ques = Question(q, a)
    # print('q',q)
    # print('a',a)
    # print('new_ques_text :',new_ques.text)
    # print('new_ques_ans :', new_ques.ans)
# Creating a question object from each entry in question_data
    # Append each question object to the question_bank
    question_bank.append(new_ques)

print(question_bank)

# Asking questions to users

# Create a class to retrieve current question number from question_list
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.ques_num}")