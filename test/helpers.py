import tempfile
import os
from shutil import copy
from typing import List, Dict


def copy_to_tmp(package: List[str] = None, renames: Dict[str, str] = None) -> str:
    """Copy test files into a temporary package directory

    :param package: files to go into the temporary package directory
    :param renames: dictionary of files to be renamed when copied, mapping old name to new
    :return: temporary package directory
    """
    # make a temporary package directory
    if package is None:
        package = []
    if renames is None:
        renames = {}
    tmp_dir = tempfile.mkdtemp()
    tmp_sub = os.path.join(tmp_dir, 'test_package')
    os.mkdir(tmp_sub)
    # copy all of the relevant files
    test_dir = os.path.dirname(os.path.realpath(__file__))
    for f in package:
        copy(os.path.join(test_dir, 'test_files', f), tmp_sub)
    for old_f, new_f in renames.items():
        copy(os.path.join(test_dir, 'test_files', old_f), os.path.join(tmp_sub, new_f))
    return tmp_sub
