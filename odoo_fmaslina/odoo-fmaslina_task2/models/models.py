# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Odoo_fmaslina_task2(models.Model):
     _name = 'odoo_fmaslina_task2'
     file = fields.Binary(string="File", required=True)
     file_name = fields.Char(string="File name")