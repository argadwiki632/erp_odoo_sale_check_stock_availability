from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_stock_check_enabled = fields.Boolean(
        related='company_id.sale_stock_check_enabled',
        readonly=False,
        string='Check Stock Before Sales Confirmation',
    )