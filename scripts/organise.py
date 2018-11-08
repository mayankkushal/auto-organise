#!/usr/bin/env python
import os
import click


class Sort(object):
    """docstring for Sort"""

    DOC = "Document"
    VIDEO = "Video"
    IMG = "Image"
    OTHERS = "Others"
    APP = "Application"

    files_type_list = [DOC, VIDEO, APP, OTHERS]

    file_type_dict = {
        'doc': DOC,
        'docx': DOC,
        'pdf': DOC,
        '3gp': VIDEO,
        'mp4': VIDEO,
        "deb": APP,
        "py": APP
    }

    def __init__(self, path):
        super(Sort, self).__init__()
        self.path = path

    def rename(self):
        for type, i in zip(self.files_type_list, range(len(self.files_type_list))):
            t = input(f"What do you want {type} to be called? [{type}]: ")
            if t:
                self.files_type_list[i] = t       
    
    def get_absolute_path(self, filename):
        return self.path + "/" + filename

    def create_directory(self, key=None, directory=None):
        if not directory:
            directory = self.path+"/"+key
        if not os.path.exists(directory):   
            os.makedirs(directory, exist_ok=True)
            click.echo(f"{directory}...Successfull")
        else:
            self.skipped += 1

    def create_all_directory(self):
        self.skipped = 0
        for key in self.files_type_list:
            self.create_directory(key)
        click.echo(f"Skipped {self.skipped}")

    def get_supported_formats(self):
        click.echo("Supported file formats:")
        for key in self.file_type_dict.keys():
            click.echo(key)

    def get_files(self):
        return next(os.walk(self.path))[2]

    def sort(self, verbose=False):
        files = self.get_files()
        for name in files:
            src = self.get_absolute_path(name)
            type = name.split('.')[-1]
            if type in self.file_type_dict.keys():
                dest = self.get_absolute_path(self.file_type_dict[type])
            else:
                dest = self.get_absolute_path(self.files_type_list[-1])
            if not os.path.exists(dest):
                click.echo(f"{dest} not found.")
                click.echo("Skipping...")
                continue
            if verbose:
                click.echo(f"Moving {name} to {dest}")
            os.system("mv" + " " + src + " " + dest)

    def run(self, verbose):
        self.create_all_directory()
        self.sort(verbose)


@click.command()
@click.option(
    "--path", "-p",
    help='path of directory you want to sort, DEFAULT: `.`'
)
@click.option(
    "--create-dir", "-d",
    is_flag=True,
    help='if you only want to create directories'
    )
@click.option(
    "--organise", "-o",
    is_flag=False,
    help='if you only want to organise'
    )
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help='lets you know about each step'
    )
@click.option(
    "--rename", "-r",
    is_flag=True,
    help='to rename the subdirectories, your way'
    )
def cli(path, create_dir, organise, verbose, rename):
    """
        A little tool that helps you organise your directory into meaningful 
        subdirectories.
    """

    def get_path(path):
        if path:
            return path
        return "."

    path = get_path(path)
    sort = Sort(path)

    if rename:
        sort.rename()

    if create_dir:
        sort.create_all_directory()
    elif organise:
        sort.sort(verbose)
    else:
        sort.run(verbose)


if __name__ == "__main__":
    cli()