MSG_TEMPLATE = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
""" # .format(name="Your Name", website='yourwebsite.com')

def format_msg(my_name="Your Name", my_website="yourwebsite.com"):
    my_msg = MSG_TEMPLATE.format(name=my_name, website=my_website)
    return my_msg