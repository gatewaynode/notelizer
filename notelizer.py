#!/usr/bin/env python3

#
# This will be a simple script to open vim for a journal entry and write it to an organized journal directory.
#

import os
import sys
import tempfile
import subprocess
import datetime
import shlex
import json
import traceback
import logging
from pprint import pprint

journal_path = os.path.join(os.path.expanduser('~'), '.journal')
journal_date = datetime.datetime.today()
journal_dir = os.path.join(journal_path, str(journal_date.year), str(journal_date.month))

# Keep things organized by directory
def upsert_dir():
    if os.path.isdir(journal_dir) and os.path.isfile(os.path.join(journal_dir, str(journal_date.day))):
        print("Update")
        append_state = True
        return(append_state)
    elif os.path.isdir(journal_dir):
        append_state = False
        return(append_state)
    else:
        try:
            os.makedirs(journal_dir)
            append_state = False
            return(append_state)
        except Exception as e:
            logging.error(traceback.format_exc())

# Use VIM as the text entry editor
def edit_notes():
    # stamp = datetime.datetime()
    EDITOR = os.environ.get('EDITOR', 'vim')
    
    journal_entry = ""

    with tempfile.NamedTemporaryFile(suffix = '.tmp') as tf:
        subprocess.call([EDITOR, tf.name])
        
        # Read the temp file
        tf.seek(0)
        journal_entry = tf.read()
    if journal_entry:
        return(journal_entry.decode('utf-8'))
    else:
        sys.exit(0)

# Write or append with some context
def write_notes(journal_entry, append_state, prefix_data = "", suffix_data = ""):
    # Prepend and append some context
    if prefix_data and suffix_data:
        journal_entry = "{}\n---\n{}---\n{}\n".format(prefix_data, journal_entry, suffix_data)
    if prefix_data and not suffix_data:
        journal_entry = "{}\n---\n{}".format(prefix_data, journal_entry)
    if suffix_data and not prefix_data:
        journal_entry = "{}\n---\n{}\n".format(journal_entry, suffix_data)
    # No need to test final possible data state as we do nothing in that case anyways
    final_write_state = "---\n{}\n---\n{}".format(str(journal_date.time()), journal_entry)
    
    if append_state:
        try:
            with open(os.path.join(journal_dir, str(journal_date.day) + '.no'), 'a') as file:
                file.write(final_write_state)
        except Exception as e:
            logging.error(traceback.format_exc())
    else:
        try:
            with open(os.path.join(journal_dir, str(journal_date.day) + '.no'), 'w') as file:
                file.write(final_write_state)
        except Exception as e:
            logging.error(traceback.format_exc())

def tagging():
    prefix_data = shlex.split(input("Tags: "))
    if prefix_data:
        return(json.dumps(prefix_data))
    else:
        return(False)

def links():
    suffix_data = shlex.split(input("Links: "))
    if suffix_data:
        return(json.dumps(suffix_data))
    else:
        return(False)
    
def main():
    # Check that our journal dir exists
    if os.path.isdir(journal_path):
        append_state = upsert_dir()
        prefix_data = tagging()
        journal_entry = edit_notes()
        suffix_data = links()
        write_notes(journal_entry, append_state, prefix_data, suffix_data)
    else:
        setup = input("Journal files not found, do you want to create them? (Y/N): ")
        
        if setup == 'y' or setup == 'Y':
            os.makedirs(journal_path)
            print("Journal entrie will be stored in: {}".format(journal_path))
            input("Press any key to continue.", _)
            prefix_data = tagging()
            journal_entry = edit_notes()
            suffix_data = links()
            write_notes(journal_entry, False, prefix_data, suffix_data)
        else:
            print("Nothing else to do.  Exiting")
            sys.exit(0)
            
if __name__ == '__main__':
    main()
