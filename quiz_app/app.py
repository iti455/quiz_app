from flask import Flask, render_template, request

app = Flask(__name__)

# Add a unique 'id' to each question for grouping
questions = [
    {
        'id': 0,
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 'Paris'
    },
    {
        'id': 1,
        'question': 'Who developed Python?',
        'options': ['Guido van Rossum', 'Elon Musk', 'Bill Gates', 'Mark Zuckerberg'],
        'answer': 'Guido van Rossum'
    },
    {
        'id': 2,
        'question': 'Which keyword is used to define a function in Python?',
        'options': ['func', 'define', 'def', 'function'],
        'answer': 'def'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in questions:
        user_answer = request.form.get(f'q{q["id"]}')
        if user_answer == q['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
