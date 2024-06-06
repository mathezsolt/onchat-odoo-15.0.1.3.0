
from odoo import http
from odoo.http import request

class KitchenScreenBase(http.Controller):

    @http.route('/get/chatbot', type="json", auth="public")
    def _get_chatbot(self):
        onchat_settings = request.env['ir.config_parameter'].sudo()
        if onchat_settings.get_param('onchat.chatbot_id', False) and onchat_settings.get_param('onchat.show_chatbot', False):
            return {
                'id': onchat_settings.get_param('onchat.chatbot_id', False),
                'show_chatbot': onchat_settings.get_param('onchat.show_chatbot', False),
            }
        else:
            return False
