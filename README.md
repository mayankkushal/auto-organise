[![Downloads](https://pepy.tech/badge/organise)](https://pepy.tech/project/organise)  [![Downloads](https://pepy.tech/badge/organise/month)](https://pepy.tech/project/organise/month)  [![Downloads](https://pepy.tech/badge/organise/week)](https://pepy.tech/project/organise/week)
# Auto Organise

 A little tool that helps you organise your directory into meaningful subdirectories.


## Installation

```
git clone https://github.com/mayankkushal/auto-organise.git
cd auto-organise
python setup.py install
```

or

`pip install Organise`

## Usage

`organise`

### Help
`organise --help`

For comprehensive details [Read the docs](https://mayankkushal.github.io/auto-organise/)

<br/><br/>

Version 2.0.0
* added support for selective filetypes to be organised.
* changed default behavior, where just calling `organise` creates only those directories for which there are valid files.
* changed use of `-o`, `--organise`, this now creates all the directories even if they do not have any files to put into it.
