# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'tunaweza',
    'description': 'This is an app for billing powered by Tunaweza Inc.',
    'category': 'account/Bill',
    'website': '',
    'depends': ['base_setup'],
    'data': [
        "data/ir.model.access.csv",
        "views/tunaweza_items_views.xml",
        "views/tunaweza_items_menu.xml",
        "views/search_items.xml",
        "views/search_company.xml",
        "views/search_customer.xml",
        "views/search_facture.xml",
        "views/form_items.xml",
        "views/form_company.xml",
        "views/form_customer.xml",
        "views/form_facture.xml"
        
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}