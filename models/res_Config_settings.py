from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    chatbot_id = fields.Char("Your OnChat chatbot ID", config_parameter="onchat.chatbot_id")
    show_chatbot = fields.Boolean("Show chatbot on your website", config_parameter="onchat.show_chatbot")
