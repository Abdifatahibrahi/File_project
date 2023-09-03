read_questions = open('questions.txt', 'r')
questions = [question.strip().split('=') for question in read_questions.readlines()]
score = []
total_q = len(questions)
for query in questions:
    question = input(f'Question: {query[0]} = ')
    if question == query[1]:
        score.append(1)


result = open('result.txt', 'a')
result.write(f"Your final score is {len(score)}/{total_q}")
result.close()

# print(f"Your final score is {len(results)}/{total_q}")



