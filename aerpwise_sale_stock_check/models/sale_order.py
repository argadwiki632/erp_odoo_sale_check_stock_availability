from odoo import models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _check_stock_before_confirm(self):
        self.ensure_one()

        if not self.company_id.sale_stock_check_enabled:
            return

        shortages = []

        for line in self.order_line.filtered(
            lambda l: l.product_id and l.product_id.is_storable
        ):
            required_qty = line.product_uom._compute_quantity(
                line.product_uom_qty,
                line.product_id.uom_id,
            )

            available_qty = line.free_qty_today

            if required_qty > available_qty:
                shortages.append(
                    _(
                        '%(product)s: ordered %(ordered).2f %(uom)s, '
                        'available %(available).2f %(uom)s'
                    ) % {
                        'product': line.product_id.display_name,
                        'ordered': required_qty,
                        'available': available_qty,
                        'uom': line.product_id.uom_id.name,
                    }
                )

        if shortages:
            raise UserError(_(
                'Sales Order cannot be confirmed because there is '
                'not enough stock:\n\n%s'
            ) % '\n'.join(
                '- ' + shortage for shortage in shortages
            ))

    def action_confirm(self):
        for order in self:
            order._check_stock_before_confirm()

        return super().action_confirm()