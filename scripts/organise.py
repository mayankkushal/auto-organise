#!/usr/bin/env python
import os
import sys
import click
import re
from tqdm import tqdm

if sys.version_info[0] < 3 and sys.version_info[1] < 6:
    raise Exception("You must be using Python 3.6 or greater")


class Sort(object):
    """ This is a simple tool which helps to organise your cluttered directory
    into meaningful subdirectories.

    **Example**:

        We are going to move the files into directories of their respective kinds, and if there are no files of that kind, a directory will not be
        created.

            $ organise -o
            or
            $ organise --organise

    Check out `organise --help` for complete list of options
    
    *Todo*:

        * Create configuration files, for easier handeling of settings
        * Handle console messages gracefully
        * Make it OS agnostic
    
    """
    verbose = False

    DOC = "Document"
    VIDEO = "Video"
    IMG = "Image"
    OTHERS = "Others"
    APP = "Application"

    # Keep `OTHERS` at the end
    files_type_list = [DOC, VIDEO, APP, IMG] + [OTHERS,]

    file_type_dict = {
        'doc': DOC,
        'docx': DOC,
        'ppt': DOC,
        'pptx': DOC,
        'pdf': DOC,
        'txt': DOC,
        '3gp': VIDEO,
        'mp4': VIDEO,
        'jpeg': IMG,
        'png': IMG,
        'gif': IMG,
        'jpg': IMG,
        "deb": APP,
        "py": APP
    }

    def __init__(self, path):
        super(Sort, self).__init__()
        self.path = path

    def rename(self):
        """
            Function used to rename the directories to user defined names
        """
        for type, i in zip(self.files_type_list, range(len(self.files_type_list))):
            t = input("What do you want {} to be called? [{}]: ".format(type, type))
            if t:
                self.files_type_list[i] = t

    def get_supported_formats(self):
        """
            Used to dispaly all the supported formats, ie which will be sorted into respective directories
        """
        click.echo("Supported formats:")
        i = 0
        for key, value in self.file_type_dict.items():
            i += 1
            click.echo("\t{}) {} --> {}".format(i, key, value))
        click.echo("\tMore coming soon")
        click.echo('Other file formats will be stored under Others')

    def get_absolute_path(self, filename):
        """Creates the complete path name and returns for the file

        Args:

            filename (str): Expects the name of the file

        Returns:

            str: The absolute path of the file

        """
        return self.path + "/" + filename

    def create_directory(self, key=None, directory=None):
        """Creates a directory, if it does not exist.

        Args:

            key (str): [optional] This is the name of the file
            directory (str): [optional] This is the complete path of the file

        **Note**: One of the, Args are to be passed.

        """
        if not directory:
            directory = self.path+"/"+key
        if not os.path.exists(directory):   
            os.makedirs(directory, exist_ok=True)
            if self.verbose:
                click.echo("Creating --> {} --> Successfull".format(directory.split("/")[-1]))
        else:
            self.skipped += 1

    def create_all_directory(self):
        """Creates all the types of directories."""
        self.skipped = 0
        for key in self.files_type_list:
            self.create_directory(key)
        if self.verbose:
            click.echo("Skipped {}".format(self.skipped))

    def get_files(self):
        """Function used to generate a list of all the files in the current directory"""
        return next(os.walk(self.path))[2]

    def sort(self, verbose=False):
        """Main function which is used to organise the files into different directories.
        Args:

            verbose (bool): [optional] If `True`, displays all the steps to the user
        """
        self.verbose = verbose
        files = self.get_files()
        for name in tqdm(files, disable=self.verbose):
            src = self.get_absolute_path(name)
            type = name.split('.')[-1]
            if type in self.file_type_dict.keys():
                dest = self.get_absolute_path(self.file_type_dict[type])
            else:
                dest = self.get_absolute_path(self.files_type_list[-1])
            if not os.path.exists(dest):
                self.create_directory(dest)
            if self.verbose:
                click.echo("Moving {} to {}".format(name, dest))
            os.system("mv" + " " + re.escape(src) + " " + dest)

    def run(self, verbose):
        self.verbose = verbose
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
    is_flag=True,
    help='do not create empty directory, ie. create directory only when relevent file exists.'
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
@click.option(
    "--formats", "-f",
    is_flag=True,
    help='display all the supported formats'
    )
def cli(path, create_dir, organise, verbose, rename, formats):
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
    elif formats:
        sort.get_supported_formats()
    else:
        sort.run(verbose)


if __name__ == "__main__":
    cli()