# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

#################################################################################
#
# Author      : Soldigo Srl (<https://www.onchat.ai>)
# Copyright(c): 2024
# All Rights Reserved.
#
#################################################################################

{
    'name': 'Onchat Chatbot',
    'version': '15.0.1.3.0',
    'category': 'Website',
    'sequence': 40,
    'author': 'Soldiro Srl',
    'license': 'OPL-1',
    "summary": "Onchat - AI powered virtual assistant for your Odoo website",
    "price": "00.0",
    "currency": "EUR",
    'depends': [
        'base', 
        'base_setup', 
        'web'],
    
    'data': [
        'views/onchat_settings.xml'
    ],
    
    'installable': True,
    'application': True,
    'website': 'https://onchat.ai',
    'images': ['static/description/banner.jpg'],
    'live_test_url': 'https://www.onchat.ai',
    'assets': {
        'point_of_sale.assets': [
        ],
        'web.assets_frontend': [
            '/onchat/static/src/notificationPatch.js',
        ],
    }
}
