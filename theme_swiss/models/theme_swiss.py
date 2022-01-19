from odoo import models

class ThemeSwiss(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_swiss_post_copy(self, mod):
        self.enable_view('website.template_footer_descriptive')