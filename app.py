from flask import Flask, render_template, request
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    profit_loss_plot = None

    if request.method == 'POST':
        income = request.form.get('income')
        expenses = request.form.get('expenses')

        if income and expenses:
            try:
                # Remove commas before converting to float
                income = float(income.replace(',', ''))
                expenses = float(expenses.replace(',', ''))
                profit_loss = income - expenses

                # Format income and expenses with commas
                formatted_income = f"{income:,.2f}"
                formatted_expenses = f"{expenses:,.2f}"

                if profit_loss > 0:
                    result = f"Profit: ₱{profit_loss:,.2f}"
                elif profit_loss < 0:
                    result = f"Loss: ₱{-profit_loss:,.2f}"
                else:
                    result = f"Break-even: No profit, no loss."

                # Generate the profit/loss plot using Plotly
                profit_loss_plot = create_profit_loss_plot(income, expenses)

            except ValueError:
                result = "Please enter valid numeric values."
        else:
            result = "Please enter values for both income and expenses."

    return render_template('index.html', result=result, profit_loss_plot=profit_loss_plot)

def create_profit_loss_plot(income, expenses):
    # Create a Plotly bar chart
    fig = go.Figure(data=[
        go.Bar(name='Income', x=['Income'], y=[income], marker_color='green'),
        go.Bar(name='Expenses', x=['Expenses'], y=[expenses], marker_color='red')
    ])
    
    # Update layout
    fig.update_layout(
        title='Profit and Loss Summary',
        yaxis_title='Amount (₱)',
        barmode='group'
    )

    # Convert the figure to HTML div
    plot_div = pio.to_html(fig, full_html=False)
    return plot_div

if __name__ == '__main__':
    app.run(debug=True)