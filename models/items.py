from odoo import api, fields, models

class Items(models.Model):
    _name="items"
    _description="items of the bill"

    item_label=fields.Char("label du produit", required=True)
    unit_price= fields.Float("prix unitaire", required=True)
    quantity = fields.Integer("quantité", required=True)
    #bill_id=fields.Many2one("facture", required=True)
    item_description = fields.Text("description du produit", required=True)
    item_tva = fields.Selection([("15%",15),("20%",20),("30%",30)], string="TVA %", required=True, translate=True)
    price_all_taxes = fields.Float("prix tout taxe comprise",
                                    compute="_all_tax_in", store=True)

    @api.depends("unit_price")
    def _all_tax_in(self):
        self.price_all_taxes=self.unit_price+(self.unit_price)*(self.item_tva/100)