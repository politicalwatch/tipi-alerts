import sparkpost
from jinja2 import Template
from .config import SPARKPOST_API, DEBUG, FROM_EMAIL


sp = sparkpost.SparkPost(SPARKPOST_API)


def sparkpost_email(recipients, subject, template, context={}):
    sp.transmissions.send(
        recipients=recipients,
        from_email=FROM_EMAIL,
        subject=subject,
        html=template,
        substitution_data=context,
    )


def debug_email(recipients, subject, template, context={}):
    print("New email:")
    print("from: {}".format(FROM_EMAIL))
    print("to: {}".format(recipients))
    print("subject: {}".format(subject))
    template = Template(template)
    print(template.render(**context))


def send_email(*args, **kwargs):
    if DEBUG:
        return debug_email(*args, **kwargs)
    return sparkpost_email(*args, **kwargs)