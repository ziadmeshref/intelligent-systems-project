# Data Dictionary

## Real Data (from UCI Online Retail II)
- `Invoice`: Invoice number. 6-digit integral number. If starts with 'C', it's a cancellation.
- `StockCode`: Product code. 5-digit integral number.
- `Description`: Product name.
- `Quantity`: Quantities of each product per transaction.
- `InvoiceDate`: Day and time when transaction was generated.
- `Price`: Unit price.
- `Customer ID`: 5-digit integer.
- `Country`: Name of the country where customer resides.

## Derived / Aggregated Inputs for NN
- `log_units_past_8w`: Log(1 + units sold) over the past 8 weeks.
- `week_of_year`: Week number (1-52).
- `mean_price`: Average price of the product over the week.
- `invoice_count`: Number of invoices the product appeared in.

## Generated Data (Simulation)
- `warehouse_grid`: 2D coordinate system representing shelf slots.
- `slot_capacities`: Number of items each slot can hold.
- `is_heavy`: Boolean flag (True for heavy items placed on low shelves).
- `is_incompatible`: List of incompatible product categories for aisle separation.
- `distances`: Simulated walking distances between depot and slots.
