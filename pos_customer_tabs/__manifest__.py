# -*- coding: utf-8 -*-
# Copyright 2018 Soltuin - Cesar M. Garcia Murguia

{
    'name': "POS customer's name on tabs",
    'summary': """
        This module adds the customer's name to the POS tabs when a customer has been selected.
        If not, a number will be used as usual.""",
    'description': """
        By adding the customer's name to the POS tabs, it is easier to find them when multiple customers are being serviced at the same time.
    """,
    'author': "Cesar M. Garcia Murguia",
    'company':"Soltuin",
    'website': "http://www.soltuin.com",
    'category': 'Point of Sale',
    'version': '0.2.0',
    'license': 'LGPL-3',
    'price': 0.00,
    'currency': 'USD',
    'depends': ['point_of_sale'],
    'data': [],
    'qweb': ['static/src/xml/pos_customer_tabs.xml'],
    'installable': True,
}