from openerp import models, fields, api, _
from openerp.exceptions import except_orm
from openerp.osv import osv
import urllib2, httplib, urlparse, gzip, requests, json
from StringIO import StringIO
import openerp.addons.decimal_precision as dp
from datetime import date
import logging
import ast
from openerp import exceptions
from openerp.exceptions import ValidationError

#Get the logger
_logger = logging.getLogger(__name__)

class product_template_duplicate(models.TransientModel):
        _name = 'product.template.duplicate'

	name = fields.Char(string='Nuevo nombre',required=True)

	@api.multi
	def confirm_name(self):
		active_id = self.env.context['active_id']
		import pdb;pdb.set_trace()
		product_tmpl = self.env['product.template'].browse(active_id)
		if picking:
			vals = {
				'name': self.name
				}
			return_id = picking.write(vals)
		return None
