from odoo import api, fields, models, _, tools


class Course(models.Model):
    _name = "demo.demo"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "N-Dev. demo lesson."

    name = fields.Char(string='Name', default=lambda self: self.env['ir.sequence'].next_by_code('account.reconcile'))
    customer = fields.Char(string='Customer', required=True)  # lead = customer
    done_date = fields.Date(default=fields.Date.today)
    lead = fields.Char(string='Lead')
    saleperson = fields.Char(string='Sale Person')
    state = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='planned')
    demo_ids = fields.One2many(compute="demo_count")


    @api.depends('customer')
    def demo_count(self):
        for id in self:
            id.customer_count = len(id.customer)

    @api.model
    def form_view_auto_fill(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'context': {
                'customer': 'Demo',
                'saleperson': 'Demo',
            }
        }

