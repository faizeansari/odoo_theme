# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class MyAccountHub(http.Controller):

    @http.route('/my/hub/category', type='http', auth="public", website=True)
    def get_categories(self, **kw):
        categories = request.env['product.category'].sudo().search([])
        category_list = []
        for category in categories:
            data = {
                'id': category.id,
                'name': category.name
            }
            category_list.append(data)
        res = {
            'data': category_list
        }
        return json.dumps(res)
