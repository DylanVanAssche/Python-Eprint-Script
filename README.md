### HP EPrint Python Printer

#### Installation and usage

Download this repository as a .zip or clone the repository. Move the `src.py` file into your Users directory (any directory will work but users will be easiar to use).

open `src.py` with a text editor and change the following:

`sender_address = 'email@emailserver.com'`

`printer_address = 'yourPrinter@hpeprint.com'`

`mail = smptlib.SMPT('smpt.mail.yourEmailProvider.com', 587)`

examples include `smpt.mail.yahoo.com` or `smpt.mail.gmail.com`

`mail.login('yourEmailUsername', 'yourEmailPassword')`

to run on a Mac or Unix system cd into your user directory and run:

`$ python src.py [filepath]` to print the document located at filepath. The easiest way to get the filepath is to drag the file from your finder into terminal.

Let me know if you encounter any problems!