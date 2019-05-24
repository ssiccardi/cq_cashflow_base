# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 CQ creativiquadrati snc di Stefano Siccardi e C.
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
from openerp.osv import osv, fields
import math
from datetime import date
import openerp.addons.decimal_precision as dp


class account_invoice(osv.osv):
    _inherit = "account.invoice"


    _columns = {
        'data_validazione': fields.date('Data Validazione prevista', help='Valida se la fattura non ha una data di scadenza e la si vuole includere nel calcolo del cashflow'),
       }

#    _defaults = {
#        'data_validazione': lambda *a: date.today(),       
#    }  
