import json
import base64
import os


def setup():
    """
    Prompts the user for their credentials and the saves them
    to a mandrill_send "dot" file.
    """
    username = raw_input("Mandrill username: ")
    apikey = raw_input("Mandrill apikey: ")
    from_email = raw_input("Default from email address: ")
    from_name = raw_input("Default from name: ")
    path = os.path.join(os.environ['HOME'], '.mandrill_send')
    if os.path.isdir(path) is False:
        os.mkdir(path)
    with open(os.path.join(path, '.config'), 'w') as f:
        data = json.dumps({"username": username, "apikey": apikey,
                          "from_email": from_email, "from_name": from_name})
        data = base64.encodestring(data)
        f.write(data)


def read():
    """
    Extracts credentials from a "dot" file

    Returns
    =======
    credentials: dict
        your credentials in form:
        {
         "username": "YOUR USERNAME",
         "apikey": "YOUR APKIKEY",
         "from_email": "YOUR DEFAULT FROM EMAIL ADDRESS",
         "from_name": "YOUR DEFAULT FROM NAME"
        }
    """
    data = open(os.path.join(os.environ['HOME'],
                '.mandrill_send', '.config')).read()
    return json.loads(base64.decodestring(data))
