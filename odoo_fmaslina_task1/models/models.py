# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from random import randint
import json


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order' 

    """Решение с default, не самое лучшее, но не сделав это,
    record.custom_field = randint(1, 1000) из onchange 
    не использовался бы при создании, а при реализации всего этого через
    computed field я никак не смог найти, как сделать сохранение значения введенного вручную"""
    custom_field = fields.Char(string='Test', store=True, default=randint(1, 1000), readonly=True,
    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})

    @api.onchange('tax_totals_json', 'date_order')
    def _onchage_test(self):
        for record in self:
            if int(json.loads(record.tax_totals_json)['amount_total']) != 0:
                record.custom_field = f"{json.loads(record.tax_totals_json)['amount_total']} - {record.date_order}"

    
    @api.constrains('custom_field')
    def _check_cf_len(self):
        for record in self:
            if len(record.custom_field) > 50:
                raise ValidationError("Length of field cant be more than 50 chars!")


    #@api.depends('tax_totals_json', 'date_order')  # Первая попытка, которая не окончилась успехом
    #def _compute_test(self):
        #for record in self:
            #if int(json.loads(record.tax_totals_json)['amount_total']) == 0:
                #record.custom_field = randint(1, 1000)
            #else:
                #record.custom_field = f"{json.loads(record.tax_totals_json)['amount_total']} - {record.date_order}"

    #def _inverse_compute_test(self):
        #for record in self:
            #record.custom_field = record.custom_field.fields_get()