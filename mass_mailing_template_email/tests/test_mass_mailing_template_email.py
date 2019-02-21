# -*- coding: utf-8 -*-
# Copyright 2019 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp.tests.common import HttpCase


class TestMassMailingTemplateEmail(HttpCase):

    post_install = True
    at_install = False

    def test_mass_mailing_template_email(self):
        """
        Our process here is the following:
        1)  Create a mail.mass_mailing record. Verify that no templates are
            shown
        2)  Create a template with the with the model mail.mass_mailing and
            another one with res.users, verify that only the first one is
            shown on the mail.mass_mailing record.
        3)  Go ahead and send that mail.mass_mailing record. Check the body and
            verify it contains the proper template body.
        """
        mass_mailing = self.env['mail.mass_mailing']
        mail_template = self.env['mail.template']
        mass_mail = mass_mailing.create({'name': 'test'})
        self.assertFalse(mass_mail.body_html)

        template1 = mail_template.create({
            'name': 'template1',
            'model_id': self.env.ref(
                'mass_mailing.model_mail_mass_mailing').id,
            'subject': 'test1',
            'body_html': '<p>test1</p>',
        })
        template2 = mail_template.create({
            'name': 'template2',
            'model_id': self.env.ref('mail.model_mail_mail').id,
            'subject': 'test',
            'body_html': '<p>test2</p>',
        })
        self.url_open('/mass_mailing/snippets')
