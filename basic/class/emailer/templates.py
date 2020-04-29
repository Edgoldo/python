"""
From 30 Days of Python tutorial, made by Coding Entrepreneurs.

Day 11 - Classes and State

Working with classes. To run this file, can use in interactive console:

> template = Templates(template_name='base_template.txt', context={'title': 'Title of template', 'content': 'Content of template'})
> template.get_template()
> template.render()
"""
import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

class Template:
    template_name = ""
    context = {}

    def __init__(self, *args, **kwargs):
        if "template_name" not in kwargs:
            raise Exception("template_name is required")
        if "context" not in kwargs:
            raise Exception("context is required")
        self.template_name = kwargs['template_name']
        self.context =kwargs['context']

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise Exception("This path does not exist")
        template_string = ""
        with open(template_path, 'r') as f:
            template_string = f.read()
        return template_string

    def render(self, context=None):
        render_ctx = context
        if self.context != None:
            render_ctx = self.context
        if not isinstance(render_ctx, dict):
            render_ctx = {}
        template_string = self.get_template()
        # The ** transform {"template_name": "Name"} in template_name="Name"
        return template_string.format(**render_ctx)
