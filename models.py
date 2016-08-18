# -*- coding: utf-8 -*-
from openerp import models, api, fields, exceptions
from openerp.exceptions import ValidationError
from datetime import date

class product_template(models.Model):
	_inherit = "product.template"

	@api.multi
	def action_duplicate(self):
                return {'type': 'ir.actions.act_window',
                        'name': 'Duplicar',
                        'res_model': 'product.template.duplicate',
			#'res_id': wizard_id.id,
                        'view_type': 'form',
                        'view_mode': 'form',
                        'target': 'new',
                        'nodestroy': True,
                        }
