from os import listdir
from os.path import isfile
import pytest
files = listdir('./')
for file in files:
    if isfile(file) and file.endswith('.ipynb'):
        print("Testing %s" % file)
        pytest.main(["../csc-448-student/tests/test_" + file[0:file.index('.ipynb')] + '.py'])