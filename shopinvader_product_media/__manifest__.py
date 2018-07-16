# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Shopinvader Product Media',
    'version': '10.0.1.0.0',
    'author': "Akretion,"
              "Serpent Consulting Services Pvt. Ltd.",
    'website': 'https://akretion.com',
    'license': 'AGPL-3',
    'category': 'e-commerce',
    'summary': 'Shopinvader Product Media',
    'depends': [
        'shopinvader',
        'product_media',
    ],
    'data': [
        'data/ir_product_export.xml',
    ],
    'installable': True,
    'auto_install': True,
}
