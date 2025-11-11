from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
            return render_template('main.html')
    first_numb = request.form.get('first_numb', '')
    second_numb = request.form.get('second_numb', '')
    operation = request.form.get('operation', '')
    errors = ''
    if not is_float(first_numb):
        errors += 'В поле a введено некорректное значение<br>'
    if not is_float(second_numb):
        errors += 'В поле b введено некорректное значение<br>'
    if len(errors) > 0:
        return errors
    try:
        result = eval(f"{first_numb} {operation} {second_numb}")
    except Exception as e:
        return f"Ошибка: {e}"
    return render_template('result.html', first_numb = first_numb, second_numb = second_numb, operation = operation, result = result)

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8083)