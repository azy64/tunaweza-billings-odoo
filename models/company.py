from odoo import models, fields

class Company(models.Model):
    _name="company"
    _description="company into the bill"

    company_name= fields.Char("nom du client", required=True, help='Entrez le nom du client', copy=False)
    company_address= fields.Text("l'adresse du client", required=True,help="Adresse du client")