from odoo import api,fields,models

class Facture(models.Model):
    _name="facture"
    _description="bill object"

    total_amount = fields.Float(
        "montant total", 
        required=True, readonly=True, default=0.00,
        compute="_total_computed",
        store=True
        )
    date_facturation = fields.Datetime("date de facturation", default=fields.Datetime.now,
                                       readonly=True,required=True)
    due_date = fields.Datetime("Echéance de facturation",required=True)
    bill_status = fields.Selection(
        [
            ("paid","paid"),("unpaid","unpaid"),("pending","pending")
        ],
        "statut de la facture",required=True, default="pending"
        )
    items = fields.Many2many("items", string="mes produits", required=True)
    customer= fields.Many2one("customer","Client", required=True)
    company=fields.Many2one("company","Entreprise", required=True, )

    _sql_constraints=[
        ('check_due_date','CHECK(due_date>= date_facturation)',"l'échéance doit etre egale ou superiere à la date actuelle"),
        ('check_total_amount','CHECK(total_amount>0)',"le montant total doit etre > 0")
        ]

    @api.depends("items")
    def _total_computed(self):
        for item in self.items:
            self.total_amount+= item.price_all_taxes

    def _sub_total_computed(self):
        for record in self:
            for item in record.items:
                record.total_amount-= item.unit_price*item.quantity