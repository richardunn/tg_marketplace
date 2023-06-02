# Create files for handlers in this folder.
import re
from .admin import admin_user
from .spam_command import anti_spam
from .user import any_user
from .start import start
from .language import show_language, set_language
from .balances import balance
from .deposits import deposit, promo
from .menu import menu
from .transactions import transaction
from .callback_answer import callback_answer
from .withdrawal import withdrawal
from tgbot.filters.admin_filter import AdminFilter


def register_handlers(bot):
    bot.register_message_handler(
        admin_user, commands=['startadmin'], admin=True, pass_bot=True)
    bot.register_message_handler(
        any_user, commands=['starttest'], pass_bot=True)
    bot.register_message_handler(
        anti_spam, commands=['spam'], pass_bot=True)
    bot.register_message_handler(
        start, commands=['start'], pass_bot=True)
    
    bot.register_message_handler(
        set_language,
        func=lambda message: message.content_type == "text"
        and re.search(r"^(English|Italiano)", message.text),
        pass_bot=True
    )

    bot.register_message_handler(
        show_language,
        func=lambda message: message.content_type == "text"
        and any(re.search(pattern, message.text, re.IGNORECASE) for pattern in ['^.+language', '^.+linguaggio', '^/lang', '^/language']),
        pass_bot=True
    )

    bot.register_message_handler(
        balance,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'^balance', message.text.split()[0], re.IGNORECASE)) or
            bool(re.search(r'^bilance',
                 message.text.split()[0], re.IGNORECASE))
        ),
        pass_bot=True
    )

    bot.register_message_handler(
        deposit,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'deposit$', message.text, re.IGNORECASE)) or
            bool(re.search(r'Depositare$', message.text, re.IGNORECASE))
        ),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        promo,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'^PROMO', message.text, re.IGNORECASE))
        ),
        admin=False, pass_bot=True
    )

    bot.register_message_handler(
        menu,
        func=lambda message: message.content_type == "text"
        and (
            bool(re.search(r'Menu$', message.text, re.IGNORECASE))
        ),
        pass_bot=True
    )

    bot.register_callback_query_handler(
        callback_answer, func=lambda call: True, pass_bot=True)

   