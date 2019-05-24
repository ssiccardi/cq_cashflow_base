# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 CQ creativiquadrati snc - Stefano SIccardi
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

from openerp.osv import osv, fields

class config_cashflow_base(osv.osv):

    _name='config.cashflow.base'
    
    _columns={
        'name':fields.char('Nome'),
        'line_id': fields.one2many('config.cashflow.base.line','conf_id',string='Selezione Conti')
    }
    _defaults={
        'name':'Configurazione Cashflow'
    }
    
config_cashflow_base()  

class config_cashflow_base_line(osv.osv):

    _name='config.cashflow.base.line'
    
    _columns={
        'conf_id':fields.many2one('config.cashflow.base',ondelete='cascade'),
        'account_id': fields.many2one('account.account','Conto',required=True,domain=[('type','!=','view')]),
        'type':fields.selection([('costo','Costo'),('ricavo','Ricavo')],'Tipo',required=True)
    }
    
config_cashflow_base_line()    
