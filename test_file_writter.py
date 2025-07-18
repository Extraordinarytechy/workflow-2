import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from file_writter import write_to_file

def test_write_to_file():
    test_filename = "test_output.txt"
    test_content = "Test Content for CI"

    write_to_file(test_filename, test_content)

    assert os.path.exists(test_filename), "File was not created"

    with open(test_filename, "r") as f:
        content = f.read()
        assert content == test_content, "File content does not match"

