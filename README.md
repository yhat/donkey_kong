mandrill_send
============

Send mandrill templates from the command line.


```
Usage:
    mandrill_send <command> [params]

Options:
    mandrill_send --help
    mandrill_send --version

Commands:
    setup:
        Prompts the user for their credentials and the saves them
        to a mandrill_send "dot" file.

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
