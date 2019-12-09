# -*- coding: utf-8 -*-

import json
import odoo.http as http
from odoo.http import request
from odoo.addons.web.controllers.main import ExcelExport


class ExcelExportView(ExcelExport):
    def __getattribute__(self, name):
        if name == 'fmt':
            raise AttributeError()
        return super(ExcelExportView, self).__getattribute__(name)

    @http.route('/web/export/xls_view', type='http', auth='user')
    def export_xls_view(self, data, token):
        data = json.loads(data)
        model = data.get('model', [])
        columns_headers = data.get('headers', [])
        rows = data.get('rows', [])

        if model == 'hd.setting':
            columns_headers = [
                u'定值号  \nSet Point \nNumber',
                '系统 \nSystem',
                '专业 \nProfession',
                '定值名称 \nSet Point Name',
                '设备代码 \nDevice Code',
                '参数代码 \nParameter\nCode',
                '设定装置 \nThe Setting\nDevice',
                '整定值 \nSet Point',
                '现场验证值 \nVerification\nvalue',
                '整定值范围 \nRange of\nset point',
                '功能说明 \nFunction \nDescription',
                '备注 \nRemark',
            ]
            rows_news = []
            for row in rows:
                    if row[4]:  # 定值名称
                        row[3] = row[3] + '\n' + row[4]

                    if row[12]:  # 功能说明
                        row[11] = row[11] + '\n' + row[12]

                    if row[14]: #合并备注
                        row[13] = row[13] + '\n' + row[14]

                    del row[4]  # 删除定值名称
                    del row[11]  # 删除英文功能说明
                    del row[12] #删除英文备注
                    del row[12] #删除状态
                    rows_news.append(row)
            rows = rows_news

        return request.make_response(
            self.from_data(columns_headers, rows),
            headers=[
                ('Content-Disposition', 'attachment; filename="%s"'
                 % self.filename(model)),
                ('Content-Type', self.content_type)
            ],
            cookies={'fileToken': token}
        )
