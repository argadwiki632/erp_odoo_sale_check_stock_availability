# -*- coding: utf-8 -*-

{
    'name': 'Sales Stock Check',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Prevent sales orders from being confirmed when stock is insufficient',
    'description': """
Sales Stock Check
=================

Check product availability before confirming a Sales Order.

This module helps sales teams prevent sales orders from being confirmed
when the required product quantity is not available in stock.

Features
--------
* Check stock availability before confirming a Sales Order.
* Compare ordered quantity with available quantity.
* Support product UoM conversion.
* Block Sales Order confirmation when stock is insufficient.
* Display detailed stock shortage information.
* Work with the warehouse configured on the Sales Order.

Use Case
--------
Before confirming a Sales Order, Odoo checks whether the required quantity
of each stockable product is available. If one or more products do not have
sufficient available stock, the Sales Order cannot be confirmed.

Example
-------
A Sales Order contains:

    Product A: 100 Units
    Available: 60 Units

The confirmation is blocked and the user is informed that 40 Units
are not available.
    """,
    'author': 'Arga Dwiki Suwandi',
    'maintainer': 'Arga Dwiki Suwandi',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'stock',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}