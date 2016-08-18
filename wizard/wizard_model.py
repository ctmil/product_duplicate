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
		product_tmpl = self.env['product.template'].browse(active_id)
		if picking:
			vals = {
				'name': self.name,
				'purchase_ok': product_tmpl.purchase_ok,
				'sale_ok': product_tmpl.sale_ok,
				'active': product_tmpl.active,
				'categ_id': product_tmpl.categ_id.id,
				'company_id': product_tmpl.company_id.id,
				'default_code': product_tmpl.default_code,
				'description': product_tmpl.description,
				'description_sale': product_tmpl.description_sale,
				'description_purchase': product_tmpl.description_purchase,
				'list_price': product_tmpl.list_price,
				'lst_price': product_tmpl.lst_price,
				'standard_price': product_tmpl.standard_price,
				'taxes_id': [(6,0,product_tmpl.taxes_id.ids)],
				}
			product_tmpl_id = self.env['product.template'].create(vals)
		return None
