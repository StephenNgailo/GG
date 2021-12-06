# -*- coding: utf-8 -*-
{
    'name': 'Mass Cancel Purchase Order',
    'summary': "Mass Cancel Purchase Order",
    'description': "Mass Cancel Purchase Order",
    'author': 'Stephen Ngailo',
    'category': 'Purchases',
    'version': '14.0.0.1.0',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_order_cancel.xml',
    ],
   'pre_init_hook': 'pre_init_check',
   'application':True,
}
