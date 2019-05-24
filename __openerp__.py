# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2016 CQ creativiquadrati snc di Stefano Siccardi e C.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Cashflow Base',
    'version': '1.0',
    'category': 'Accounting',
    'description': """Basic functions to compute cash flow, based on sale and purchase orders and invoices
    """,
    'author': 'Stefano Siccardi @ CQ Creativi Quadrati',
    'license': 'AGPL-3',
    'depends' : ['sale','purchase','report_xls'],
    'init_xml': [],    
    'update_xml' : [
        'security/ir.model.access.csv',
        'wizard/previsione_in_out_view.xml',
        'config_cashflow_base_view.xml',
        'account_view.xml',
        'sale_view.xml',
        'purchase_view.xml',
        'report/cq_cashflow_xls.xml'
    ],
    'active': False,
    'installable': True
}
