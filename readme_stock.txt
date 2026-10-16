========================================================================
                      STOCK PORTFOLIO TRACKER
========================================================================

DESCRIPTION
-----------
This is a simple Python program that calculates the total investment value 
for a selected stock based on pre-defined market prices and a user-specified 
quantity.

FEATURES
--------
- Hardcoded price list for popular stock tickers (AAPL, TSLA, GOOG, AMZN).
- Automatic uppercase formatting for stock ticker inputs.
- Validates input against available stock options.
- Calculates and displays the total investment value instantly.

REQUIREMENTS
------------
- Python 3.x installed on your system.

HOW TO RUN
----------
1. Open your terminal or command prompt.
2. Navigate to the folder containing 'STOK PORTFOLIO TRACKER.py':

   cd path/to/your/folder

3. Run the script:

   python "STOK PORTFOLIO TRACKER.py"

USAGE / EXAMPLE INTERACTION
---------------------------
When prompted, enter a valid ticker symbol and the quantity of shares:

Available Stocks & Prices:
- AAPL: $180
- TSLA: $250
- GOOG: $150
- AMZN: $200

Example 1 (Valid Stock):
------------------------
===== STOK PORTFOLIO TRACKER =====
Enter stock name(AAPL/TSLA/GOOG/AMZN): aapl
Enter quentity: 5
Stock: AAPL
Price: 180
Quentity: 5
Total Investment: 900

Example 2 (Invalid Stock):
--------------------------
===== STOK PORTFOLIO TRACKER =====
Enter stock name(AAPL/TSLA/GOOG/AMZN): MSFT
Enter quentity: 2
Stock not found.

LICENSE
-------
This project is open-source and available under the MIT License.
========================================================================