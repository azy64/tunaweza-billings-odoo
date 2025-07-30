
from odoo import fields, models

class Customer(models.Model):
    _name="customer"
    _description="client of the bill"

    customer_name= fields.Char("nom du client", required=True, help='Entrez le nom du client')
    customer_address= fields.Text("l'adresse du client", required=True,help="Adresse du client")
    company = fields.Many2one("company","le nom de l'entreprise" ,required=True)