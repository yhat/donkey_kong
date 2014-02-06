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


def prompt_user():
    choices = ['Template Name', 'From Email Address', 'From Name',
               'To Email Address', 'To Name', 'Subject']
    choices_lookup = {}
    print "" + Fore.CYAN
    table = PrettyTable([Fore.YELLOW + "Key", Fore.YELLOW + "Value"])
    for i, choice in enumerate(choices):
        choices_lookup[str(i+1)] = raw_input(choice + ': ')
        table.add_row([
            Fore.YELLOW + choice,
            Fore.GREEN + choices_lookup[str(i+1)]
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
    # creds = credentials.read()
    result = prompt_user()
    while result is None:
        result = prompt_user()

    print result