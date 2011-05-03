Overview
-------------
This is an early proof of concept.
Currently this is VERY hardcoded, but I thought it would be worth releasing:
The merge-csv.py file requires a file called 'data.csv'

If you're comfortable with python and the commandline you should be able to find your way around.

Preparation:
--------------
The script expects a 'data.csv' file and 'content4.xml.tmpl' file in the same directory

You will need to install Jinja::

   easy_install Jinja2

Usage
----------
While in the directory with the 'data.csv' and 'content4.xml.tmpl' run the following::

   python merge-csv.py > content.xml

The result will be an ODT (openoffice style) content.xml file

This can be added to an unzipped an openoffice document (ODT) to replace the content.xml, then rezip and rename to ODT. The resulting document will contain your merged output.

