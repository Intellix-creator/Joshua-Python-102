

from chatbot import cprint, cinput

def ask_questions(questions):
	answers = 
[]

	for question in 
questions
:
		answer = cinput(
question
)
		answers.
append
(answer)
	return(
answers
)

questions = [
	"How many days do you eat Meat?",
	"How many days do you eat as a Vegetarian?",
	"How many days do you eat as a Vegan?"
]
answers = ask_questions(questions)

for i in range(len(answers)):
	cprint(questions[
i
], answers[
i
])