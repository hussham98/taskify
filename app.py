from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application instance
app = Flask(__name__)

# Initialize tasks list with sample data
tasks = [
    {'task': 'Create a Web App', 'completed': False, 'due_date': '2024-05-29'},
    {'task': 'Do Unit tests of the App', 'completed': False, 'due_date': '2024-05-29'},
    {'task': 'Github Actions for CI/CD', 'completed': False, 'due_date': '2024-05-29'}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        # Get the task and due date from the form
        task = request.form['task']
        due_date = request.form['due_date']
        # Add the new task to the tasks list
        tasks.append({'task': task, 'completed': False, 'due_date': due_date})
        # Redirect to the index page
        return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        task = request.form['task']
        due_date = request.form['due_date']
        tasks[index]['task'] = task
        tasks[index]['due_date'] = due_date
        return redirect(url_for('index'))
    return render_template('edit_task.html', index=index, task=tasks[index])

@app.route('/complete/<int:index>')
def complete_task(index):
    tasks[index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_task():
    query = request.args.get('query')
    if query is None:
        query = ''  # Set query to empty string if it's None
    results = [task for task in tasks if query.lower() in task['task'].lower()]
    return render_template('search_result.html', query=query, results=results)

if __name__ == '__main__':
    # Use the assigned port from Heroku or default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
