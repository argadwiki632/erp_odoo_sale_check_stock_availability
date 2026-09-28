from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_stock_check_enabled = fields.Boolean(
        string='Check Stock Before Sales Confirmation',
        default=False,
        help=(
            'If enabled, sales orders will be blocked from confirmation '
            'when the ordered quantity exceeds the available free quantity.'
        ),
    )