Notelizer v0.1
================
This is a note taking tool that leverages VIM for editing.  Functionality is just to add time stamped text entries to an organized journal space in your home directory through a simple CLI command.  It is designed around simplicity and portability.

Requirements
------------
* [Vim](https://www.vim.org/) is the text editor used, it must be installed first. 
* [Python 3](https://www.python.org/downloads/) is necessary if there is not a prebuilt binary.

Install
-------
Currently tested in Linux.

```bash
make virtualenv
make build
make install
```
This will setup the virtual environment and dependencies, build a standalone executable and place it in the `~/.local/bin` directory as a file named "jo".  The build and install steps aren't really necessary if you'd rather just run it from the virtual environment.

If you don't have a `~/.local` dir and the bin folder is not in your path you'll need to create `~/.local/bin` and add the following line to the end of your .bashrc or .bash_profile files to  include the path.

```bash
export PATH=~/.local/bin:$PATH
```

An alternative install is just to symlink the `notelizer.py` file to `/usr/local/bin` if your local default Python environment has the necessary dependencies, which currently it should as the only dependency outside the standard library is PyInstaller which is really just to package things up nicely in non-python3 environments.

Usage
-----
It's pretty straight forward with the default install, just type `jo` and it will setup the journal directories if needed and add a new entry for the day or append an existing entry with a timestamp.  Text is entered using vim

Roadmap
-------
* Build cross platform binaries
* Add a local config file in ~/.local/etc/
* Tests
