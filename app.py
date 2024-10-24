from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        income = request.form.get('income')
        expenses = request.form.get('expenses')

        if income and expenses:
            try:
                income = float(income)
                expenses = float(expenses)
                profit_loss = income - expenses

                if profit_loss > 0:
                    result = f"Profit: ${profit_loss:.2f}"
                elif profit_loss < 0:
                    result = f"Loss: ${-profit_loss:.2f}"
                else:
                    result = "Break-even: No profit, no loss."
            except ValueError:
                result = "Please enter valid numeric values."
        else:
            result = "Please enter values for both income and expenses."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
