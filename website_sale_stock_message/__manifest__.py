# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Sale Stock Message',
    'category': 'Website/Website',
    'summary': 'Manage the message regarding inventory and product availability',
    "version": "15.0.1.0.0",
    "license": "LGPL-3",
    "author": "Valentín Romero, Tecnicanet BA",
    'description': """Manage the message regarding inventory and product availability""",
    'depends': [
        'website_sale',
        'sale_stock',
    ],
    'data': [
        'views/product_template_views.xml',
        'views/website_sale_stock_templates.xml',
    ],
    'auto_install': True,
}
