donkey_kong
============

Send mandrill templates from the command line.

### Installation

```
$ pip install donkey_kong
```

```
Usage:
    donkey_kong <command> [params]

Options:
    donkey_kong --help
    donkey_kong --version

Commands:
    setup:
        Prompts the user for their credentials and the saves them
        to a donkey_kong "dot" file.

    config:
        Returns the users configurations.

    list:
        Return a table with your current mailchimp templates data,
        and any custom variables you have.

    send <template_name>:
        Prompts the user for the template name, from email address, from name,
        to email address, to name, subject, and any variables that get
        passed to the template. Then sends the template. 
```
