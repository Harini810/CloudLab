from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Calculator</title>
</head>
<body>
    <h1>Simple Flask Calculator</h1>
    <form method="post">
        <input type="number" name="num1" step="any" required placeholder="Enter first number">
        <input type="number" name="num2" step="any" required placeholder="Enter second number">
        <br><br>
        <input type="radio" name="operation" value="add" required> Add
        <input type="radio" name="operation" value="subtract" required> Subtract
        <input type="radio" name="operation" value="multiply" required> Multiply
        <input type="radio" name="operation" value="divide" required> Divide
        <br><br>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero"
        except ValueError:
            result = "Invalid input"

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
