# -*- coding: utf-8 -*-
from odoo import fields, models


class Bill(models.Model):
    _name = "bill"
    _description = "CRM bill revenue plans"

    name = fields.Char('Plan Name', required=True, translate=True)
    date_bill = fields.Date("date de facturation",required=True,translate=True)