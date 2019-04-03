//Copyright 2019 Therp BV <https://therp.nl>
//License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

odoo.define('mail_archive', function(require) {
    var core = require('web.core');
    var _lt = core._lt;
    var chat_client_action = require('mail.chat_client_action');
    var ChatAction = core.action_registry.get('mail.chat.instant_messaging');
    var chat_manager = require('mail.chat_manager');
    var channel_archive = chat_manager.make_channel(
        {
            id: 'channel_archive',
            name: _lt('Archive'),
            type: 'static',
        },
        {display_needactions: false}
    );
    chat_manager.bus.trigger('new_channel', channel_archive);
    ChatAction.include({
        events: _.extend(
            {},
            ChatAction.prototype.events,
            {
                'click .o_mail_chat_channel_archive': function (event){
                    event.preventDefault();
                    var channel_id = this.$(event.currentTarget).data('channel-id');
                    return this.set_channel(
                        chat_manager.get_channel(channel_id));
                }
            })
    });
});
