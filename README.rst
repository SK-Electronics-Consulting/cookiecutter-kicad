##################
Cookiecutter-kicad
##################

Usage
=====

To use, call cookiecutter direct from the command line:
`cookiecutter {path to this directory}`

The arguments it takes are the following:

* Name: Your common name.  Only used if local git repo settings are used.
* email: Your e-mail.  Only used if local git repo settings are used.
* project_name: Name of the project.  Can use plain English formatting.
* use_local_repo_credentials: Boolean (False).  If set to true, uses the Name and email fields to generate a `.git/config` file
* repo_name: auto-generated from project_name.  Though modified to use lower-case chars and remove white-spaces.

TODO:
=====
* Open and save PCB with gerber outputs.
* Add README within template.
* Update to KiCAD v7
