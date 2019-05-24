# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015
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

import xlwt
from datetime import datetime
from openerp.osv import orm
from openerp.report import report_sxw
from openerp.addons.report_xls.report_xls import report_xls
from openerp.addons.report_xls.utils import rowcol_to_cell, _render
from openerp.tools.translate import translate, _
import logging
_logger = logging.getLogger(__name__)

_ir_translation_name = 'cq.cashflow.xls'

class cq_cashflow_xls_parser(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(cq_cashflow_xls_parser, self).__init__(
            cr, uid, name, context=context)
        previsione_obj = self.pool.get('previsione.in.out')
        self.context = context
        wanted_list = previsione_obj._report_xls_fields(cr, uid, context)
        template_changes = previsione_obj._report_xls_template(cr, uid, context)
        self.localcontext.update({
            'datetime': datetime,
            'wanted_list': wanted_list,
            'template_changes': template_changes,
            '_': self._,
        })

    def _(self, src):
        lang = self.context.get('lang', 'en_US')
        return translate(self.cr, _ir_translation_name, 'report', lang, src) \
            or src


class cq_cashflow_xls(report_xls):

    def __init__(self, name, table, rml=False, parser=False, header=False,
                 store=False):
        super(cq_cashflow_xls, self).__init__(
            name, table, rml, parser, header, store)

        # Cell Styles
        _xs = self.xls_styles
        # lines
        aml_cell_format = _xs['borders_all']
        self.aml_cell_style = xlwt.easyxf(aml_cell_format)
        self.aml_cell_style_center = xlwt.easyxf(
            aml_cell_format + _xs['center'])
        self.aml_cell_style_date = xlwt.easyxf(
            aml_cell_format + _xs['left'],
            num_format_str=report_xls.date_format)
        self.aml_cell_style_decimal = xlwt.easyxf(
            aml_cell_format + _xs['right'],
            num_format_str=report_xls.decimal_format)

        # XLS Template
        self.col_specs_template = {
            'col0': {
                'lines': [1, 0, 'text', _render("col0 or ''")],
                },
            'col1': {
                'lines': [1, 0, 'text', _render("col1 or ''")],
                },
            'col2': {
                'lines': [1, 0, 'text', _render("col2 or ''")],
                },
            'col3': {
                'lines': [1, 0, 'text', _render("col3 or ''")],
                },
            'col4': {
                'lines': [1, 0, 'text', _render("col4 or ''")],
                },
            'col5': {
                'lines': [1, 0, 'text', _render("col5 or ''")],
                },
            'col6': {
                'lines': [1, 0, 'text', _render("col6 or ''")],
                },
            'col7': {
                'lines': [1, 0, 'text', _render("col7 or ''")],
                },
            'col8': {
                'lines': [1, 0, 'text', _render("col8 or ''")],
                },
            'col9': {
                'lines': [1, 0, 'text', _render("col9 or ''")],
                },
            'col10': {
                'lines': [1, 0, 'text', _render("col10 or ''")],
                },
            'col11': {
                'lines': [1, 0, 'text', _render("col11 or ''")],
                },
            'col12': {
                'lines': [1, 0, 'text', _render("col12 or ''")],
                },
            'col13': {
                'lines': [1, 0, 'text', _render("col13 or ''")],
                },
        }
        
    def generate_xls_report(self, _p, _xs, data, objects, wb):

        wanted_list = _p.wanted_list
        self.col_specs_template.update(_p.template_changes)
        _ = _p._
        row_pos = 0 
        limit=False
        for line in data['foglio']:
            if line['col0'] in ('INCASSI-FATTURE','INCASSI-ORDINI','PAGAMENTI-FATTURE','PAGAMENTI-ORDINI','ALTRE SCADENZE','TOTALI'):
                ws = wb.add_sheet(line['col0'])
                ws.panes_frozen = True
                ws.remove_splits = True
                ws.portrait = 0  # Landscape
                ws.fit_width_to_pages = 10
                row_pos = 0  
                limit=2
                if line['col0']=='TOTALI':
                    limit=1
            if all(cell=='' for cell in line):
                row_pos+=1
            else:
                col0=line['col0']
                col1=line['col1']
                col2=line['col2']
                col3=line['col3']
                col4=line['col4']
                col5=line['col5']
                col6=line['col6']
                col7=line['col7']
                col8=line['col8']
                col9=line['col9']
                col10=line['col10']
                col11=line['col11']
                col12=line['col12']
                col13=line['col13']
                c_specs = map(
                    lambda x: self.render(x, self.col_specs_template, 'lines'),
                    wanted_list)
                #per le celle numeriche sostituisco il formato numerico
                for s in c_specs:
                    if type(s[4])==float or type(s[4])==int:
                        s[3]='number'
                row_data = self.xls_row_template(c_specs, wanted_list)
                row_pos = self.xls_write_row(
                        ws, row_pos, row_data, row_style=self.aml_cell_style)  
            if row_pos==limit:
                ws.set_horz_split_pos(row_pos)                        

cq_cashflow_xls('report.cq.cashflow.xls','previsione.in.out',parser=cq_cashflow_xls_parser)
