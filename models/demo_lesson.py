# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools


class Course(models.Model):
    _name = "demo.demo"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "N-Dev. demo lesson."

    name = fields.Char(string='Name', default=lambda self: self.env['ir.sequence'].next_by_code('account.reconcile'))
    customer = fields.Char(string='Customer', required=True)
    done_date = fields.Date(default=fields.Date.today)
    lead = fields.Char(string='Lead')
    saleperson = fields.Char(string='Sale Person')
    demo_count = fields.Integer(string='Demo Count')
    state = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='planned')
    demo_ids = fields.One2many('demo.related', 'demo_related', string='Demo ids', store="True")

    def button_demo_count(self):
        return {
            'name': ('DemoCount'),
            'domain': [('demo_related', '=', self.id)],
            'view_type': 'form',
            'res_model': 'demo.related',
            'view_id': False,
            'view_mode': 'form,list',
            'type': 'ir.actions.act_window',
        }


class DemoRelated(models.Model):
    _name = "demo.related"

    demo_related = fields.Many2one('demo.demo', string='Demo Related')

