# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    rent_tax_first_value = fields.Float('Lower value on the rent range tax', digits=(10,2), help='Indicate the first value on the Rent Tax Range',default=799000)

    @api.model
    def get_default_rent_tax_first_value(self, cr, uid, fields, context=None):
        rent_tax_first_value=self.env['ir.config_parameter'].get_param('rent_tax_first_value', False)
        irconfigparam = self.env['ir.config_parameter']
        return{
                'rent_tax_first_value': rent_tax_first_value
        }

    @api.model
    def set_default_rent_tax_first_value(self, cr, uid, ids, context=None):
        self.ensure_one()
        irconfigparam = self.env['ir.config_parameter']
        irconfigparam.set_param('rent_tax_first_value', self.rent_tax_first_value)

    rent_tax_second_value = fields.Float('Second value on the rent range tax', digits=(10,2), help='Indicate the second value on the Rent Tax Range',default=1199000)

    @api.model
    def get_default_rent_tax_second_value(self, cr, uid, fields, context=None):
        rent_tax_second_value=self.env['ir.config_parameter'].get_param('rent_tax_second_value', False)
        irconfigparam = self.env['ir.config_parameter']
        return{
                'rent_tax_second_value': rent_tax_second_value
        }

    @api.model
    def set_default_rent_tax_second_value(self, cr, uid, ids, context=None):
        self.ensure_one()
        irconfigparam = self.env['ir.config_parameter']
        irconfigparam.set_param('rent_tax_second_value', self.rent_tax_second_value)
    
    child_monthly_exoneration_value = fields.Float('Amount exonerate for each child on the rent tax', digits=(10,2), help='Indicate the samount exonerated for each child on the Rent Tax',default=1500)

    @api.model
    def get_default_child_monthly_exoneration_value(self, cr, uid, fields, context=None):
        child_monthly_exoneration_value=self.env['ir.config_parameter'].get_param('child_monthly_exoneration_value', False)
        irconfigparam = self.env['ir.config_parameter']
        return{
                'child_monthly_exoneration_value': child_monthly_exoneration_value
        }

    @api.model
    def set_default_child_monthly_exoneration_value(self, cr, uid, ids, context=None):
        self.ensure_one()
        irconfigparam = self.env['ir.config_parameter']
        irconfigparam.set_param('child_monthly_exoneration_value', self.child_monthly_exoneration_value)

    spouse_monthly_exoneration_value = fields.Float('Amount exonerated for spouse on the rent tax', digits=(10,2), help='Indicate the amount exonerated for spouse on the Rent Tax',default=2240)

    @api.model
    def get_default_spouse_monthly_exoneration_value(self, cr, uid, fields, context=None):
        spouse_monthly_exoneration_value=self.env['ir.config_parameter'].get_param('spouse_monthly_exoneration_value', False)
        irconfigparam = self.env['ir.config_parameter']
        return{
                'spouse_monthly_exoneration_value': spouse_monthly_exoneration_value
        }

    @api.model
    def set_default_spouse_monthly_exoneration_value(self, cr, uid, ids, context=None):
        self.ensure_one()
        irconfigparam = self.env['ir.config_parameter']
        irconfigparam.set_param('spouse_monthly_exoneration_value', self.spouse_monthly_exoneration_value)
