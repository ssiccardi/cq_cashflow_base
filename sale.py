# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014
#    Stefano Siccardi creativiquadrati snc
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields
from openerp import api

class sale_order(orm.Model):

    _inherit = "sale.order"
    
    _columns = {
       'divisione_fatturazione_line': fields.one2many('divisione.fatturazione.sale','order_id','Divisione fatturazione', invisible=True),
    }


class divisione_fatturazione_sale(orm.Model):

    _name = "divisione.fatturazione.sale"
    
    _columns = {
        'order_id': fields.many2one('sale.order','Ordine',required=True),
        'importo': fields.float('Importo'),
        'data_prevista': fields.date('Data Prevista'),    
    }                 
    _order='data_prevista asc'    
