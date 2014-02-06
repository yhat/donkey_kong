import os
import credentials
import mandrill
import codecs

from colorama import Fore
from prettytable import PrettyTable

from HTMLParser import HTMLParser

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'mc:edit':
                self.data.append(attr[1])

parser = MyHTMLParser()


def check_creds():
    path = os.path.join(os.environ['HOME'], '.donkey_kong')
    if os.path.isdir(path) is False:
        credentials.setup()


def list():
    """
    Return a table with your current mailchimp templates data.
    """
    check_creds()
    creds = credentials.read()
    # Get the remplates from mandrill api
    try:
        mandrill_client = mandrill.Mandrill(creds['apikey'])
        templates = mandrill_client.templates.list()
        table = PrettyTable([Fore.GREEN + "Template", "'mc:edit' fields"])
        for template in templates:
            parser.data = []
            parser.reset()
            parser.feed(template['code'])
            table.add_row([Fore.CYAN + template['publish_name'],
                           ', '.join(parser.data)])
        print table

    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)


def prompt_user(creds, choices):
    choices_lookup = []
    choices_options = {}
    print "" + Fore.CYAN
    table = PrettyTable([Fore.YELLOW + "Key", Fore.YELLOW + "Value"])
    for key, choice in choices.items():
        try:
            user_response = raw_input(choice + ' (' + creds[key] + '): ')
            if user_response == '':
                user_response = creds[key]
        except Exception:
            user_response = raw_input(choice + ': ')
        choices_lookup.append({'name': key, 'content': user_response})
        choices_options[key] = user_response
        table.add_row([
            Fore.YELLOW + key,
            Fore.GREEN + user_response
        ])
    print "" + Fore.YELLOW
    print table
    return [choices_lookup, choices_options]


def send(template_name):
    """
    Prompts the user for the template name, from email address, from name,
    to email address, to name, subject, and any variables that get
    passed to the template. Then sends the template.
    """
    check_creds()
    creds = credentials.read()

    try:
        mandrill_client = mandrill.Mandrill(creds['apikey'])
        template = mandrill_client.templates.info(name=template_name)

        parser.data = []
        parser.reset()
        parser.feed(template['code'])

        choices = {'from_email': 'From Email Address',
                   'from_name': 'From Name', 'to_email': 'To Email Address',
                   'subject': 'Subject'}
        for data in parser.data:
            choices[data] = 'Template Option-> ' + data

        template_content = prompt_user(creds, choices)
        while template_content is None:
            template_content = prompt_user()

        t_c = template_content[0]
        t_o = template_content[1]
        r_t = mandrill_client.templates.render(template_name=template_name,
                                               template_content=t_c)

        msg = MIMEMultipart('alternative')

        msg['Subject'] = t_o['subject']
        msg['From'] = t_o['from_name']+' <'+t_o['from_email']+'>'
        msg['To'] = t_o['to_email']

        content = r_t['html'].encode('ascii', 'xmlcharrefreplace')
        html = MIMEText(content, 'html')

        username = creds['username']
        password = creds['apikey']

        msg.attach(html)

        s = smtplib.SMTP('smtp.mandrillapp.com', 587)

        s.login(username, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())

        s.quit()

        print "" + Fore.MAGENTA + 'Email Sent!!'

    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
