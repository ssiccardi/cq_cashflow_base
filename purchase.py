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

class purchase_order(orm.Model):

    _inherit = "purchase.order"
    
    _columns = {
       'divisione_fatturazione_line': fields.one2many('divisione.fatturazione.purchase','order_id','Divisione fatturazione', invisible=True),
    }

    def create_div_fatt_line(self, cr, uid, ids, context=None):
        cur_obj=self.pool.get('res.currency')
        for order in self.browse(cr, uid, ids, context=context):
            if order.divisione_fatturazione_line:
                order.divisione_fatturazione_line.unlink()
            div_fatt_lines = {}
            cur = order.pricelist_id.currency_id
            for line in order.order_line:
                if line.date_planned:
                    date = line.date_planned
                    amount_tax = 0.0
                    for c in self.pool.get('account.tax').compute_all(cr, uid, line.taxes_id, line.price_unit, line.product_qty, line.product_id, order.partner_id)['taxes']:
                        amount_tax += c.get('amount', 0.0)
                    if date in div_fatt_lines:
                        div_fatt_lines[date] += line.price_subtotal + amount_tax
                    else:
                        div_fatt_lines[date] = line.price_subtotal + amount_tax
            order.write({'divisione_fatturazione_line': map(lambda x: (0,0,{'importo': cur_obj.round(cr, uid, cur, x[1]), 'data_prevista': x[0]}), div_fatt_lines.items())})
        return True

class divisione_fatturazione_purchase(orm.Model):

    _name = "divisione.fatturazione.purchase"
    
    _columns = {
        'order_id': fields.many2one('purchase.order','Ordine',required=True),
        'importo': fields.float('Importo'),
        'data_prevista': fields.date('Data Prevista'),    
    }                 
    _order='data_prevista asc'        
