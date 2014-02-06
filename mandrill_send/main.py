import os
import credentials
from colorama import Fore
from prettytable import PrettyTable


def check_creds():
    path = os.path.join(os.environ['HOME'], '.mandrill_send')
    if os.path.isdir(path) is False:
        credentials.setup()


def list():
    """
    Return a table with your current mailchimp templates data.
    """
    check_creds()
    creds = credentials.read()
    table = PrettyTable([Fore.CYAN + "", Fore.CYAN + "credentials"])
    for key, value in creds.items():
        table.add_row([Fore.CYAN + key, Fore.CYAN + value])
    print table


def prompt_user(creds):
    choices = {'template_name': 'Template Name',
               'from_email': 'From Email Address', 'from_name': 'From Name',
               'to_email': 'To Email Address', 'to_name': 'To Name',
               'subject': 'Subject'}
    choices_lookup = {}
    print "" + Fore.CYAN
    table = PrettyTable([Fore.YELLOW + "Key", Fore.YELLOW + "Value"])
    for key, choice in choices.items():
        try:
            choices_lookup[key] = raw_input(choice + ' (' + creds[key] + '): ')
            if choices_lookup[key] == '':
                choices_lookup[key] = creds[key]
        except Exception:
            choices_lookup[key] = raw_input(choice + ': ')
        table.add_row([
            Fore.YELLOW + key,
            Fore.GREEN + choices_lookup[key]
        ])
    print "" + Fore.YELLOW
    print table
    return choices_lookup


def send():
    """
    Prompts the user for the template name, from email address, from name,
    to email address, to name, subject, and any variables that get
    passed to the template. Then sends the template.
    """
    check_creds()
    creds = credentials.read()
    result = prompt_user(creds)
    while result is None:
        result = prompt_user()
