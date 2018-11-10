import json
import click

class ConfigHandelingMixin(object):
    """docstring for ConfigHandelingMixin"""

    def __init__(self):
        super(ConfigHandelingMixin, self).__init__()
        # self.validate_variables()

    # def validate_variables(self):
    #     # try:
    #     if files_type_list:
    #         global OTHERS
    #         try:
    #             if not OTHERS:
    #                 OTHERS = "Others"
    #         except NameError:
    #             OTHERS = "Others"
    #         files_type_list.append(OTHERS)
    #     # except NameError:
    #     #     click.echo("`file_type_list incorrectly configured")
    #     try:
    #         if file_type_dict:
    #             pass
    #     except NameError:
    #         click.echo("`file_type_dict incorrectly configured")