from flask import Flask, render_template, request  # Import necessary modules from Flask
import plotly.graph_objects as go  # Import Plotly's graph objects for creating visualizations
import plotly.io as pio  # Import Plotly I/O for rendering graphs as HTML

app = Flask(__name__)  # Create a Flask application instance

@app.route('/', methods=['GET', 'POST'])  # Define the route for the homepage with GET and POST methods
def index():
    result = ""  # Initialize result message
    profit_loss_plot = None  # Initialize variable for the profit/loss plot

    if request.method == 'POST':  # Check if the request method is POST
        income = request.form.get('income')  # Get income from form data
        expenses = request.form.get('expenses')  # Get expenses from form data

        if income and expenses:  # Check if both income and expenses are provided
            try:
                # Convert income and expenses to float after removing commas
                income = float(income.replace(',', ''))
                expenses = float(expenses.replace(',', ''))
                profit_loss = income - expenses  # Calculate profit/loss

                # Determine the result message based on profit/loss value
                if profit_loss > 0:
                    result = f"Profit: ₱{profit_loss:,.2f} ({format_number(profit_loss)})"
                elif profit_loss < 0:
                    result = f"Loss: ₱{-profit_loss:,.2f} ({format_number(-profit_loss)})"
                else:
                    result = "Break-even: No profit, no loss."

                # Create the profit/loss plot using the provided income and expenses
                profit_loss_plot = create_profit_loss_plot(income, expenses)

            except ValueError:  # Handle cases where input cannot be converted to float
                result = "Please enter valid numeric values."
        else:
            result = "Please enter values for both income and expenses."  # Prompt for missing values

    # Render the index.html template, passing in the result message and the plot HTML
    return render_template('index.html', result=result, profit_loss_plot=profit_loss_plot)

def create_profit_loss_plot(income, expenses):
    # Create a bar chart to visualize income and expenses
    fig = go.Figure(data=[
        go.Bar(name='Income', x=['Income'], y=[income], marker_color='green'),  # Bar for income
        go.Bar(name='Expenses', x=['Expenses'], y=[expenses], marker_color='red')  # Bar for expenses
    ])
    
    # Update the layout of the figure
    fig.update_layout(
        title='Profit and Loss Summary',  # Title of the chart
        yaxis_title='Amount (₱)',  # Y-axis label
        barmode='group'  # Group bars side by side
    )

    # Convert the figure to an HTML div element
    plot_div = pio.to_html(fig, full_html=False)
    return plot_div  # Return the HTML representation of the plot

def format_number(value):
    # Format numbers into readable strings (e.g., K for thousands, M for millions)
    if abs(value) < 1_000:  # Less than 1,000
        return f"{value:.1f}"
    elif abs(value) < 1_000_000:  # Less than 1 million
        return f"{value / 1_000:.1f}K"
    elif abs(value) < 1_000_000_000:  # Less than 1 billion
        return f"{value / 1_000_000:.1f}M"
    else:  # 1 billion or more
        return f"{value / 1_000_000_000:.1f}B"

if __name__ == '__main__':  # Check if the script is run directly
    app.run(debug=True)  # Start the Flask application in debug mode
