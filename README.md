aerpwise - Sales Stock Check




Odoo 18 module to check product stock availability before confirming a Sales Order.

The module prevents users from confirming a Sales Order when the ordered quantity exceeds the available free_qty_today on the Sales Order Line.

Features




Enable or disable stock checking per company.
Check stock availability before Sales Order confirmation.
Compare ordered quantity with free_qty_today.
Support multiple companies with independent configuration.
Automatically ignore non-storable products.
Display clear validation messages when stock is insufficient.
Uses Odoo's existing stock availability calculation.
How It Works

When a user clicks Confirm on a Sales Order, the module checks each order line containing a storable product.

Ordered Quantity
       │
       ▼
free_qty_today
       │
       ▼
 ┌───────────────┐
 │ Ordered > Free│
 └───────┬───────┘
         │
       YES
         │
         ▼
 Block Confirmation
Example




Product	Ordered Qty	Free Qty Today	Result
Product A	10	15	Pass
Product B	20	12	Block

If the ordered quantity exceeds free_qty_today, the Sales Order cannot be confirmed.

Stock Warning




When insufficient stock is detected, the user receives a clear validation message.

Example:

Sales Order cannot be confirmed because there is not enough stock:

- Laptop: ordered 10.00 Units, available 7.00 Units

The user can then adjust the order quantity or resolve the stock availability issue before confirming the Sales Order.

Configuration

Stock checking can be configured independently for each company.
