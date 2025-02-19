import os
import pytest

#func to count words in file
def count(filename):
    with open(filename, "r") as file:
        content = file.read()
    return len(content.split())



def create_test():
    #expected output of file name
    test_cases = {
        "task6_read_me.txt": 126
    }

    #use file name and expected count to create test
    for filename, expected_count in test_cases.items():
        test_name = f"test_word_count_{os.path.splitext(filename)[0]}"
        
        def test_func():
            assert count(filename) == expected_count
        
        globals()[test_name] = test_func


create_test()