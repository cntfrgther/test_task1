import pytest
import tempfile
import os
from src.tree import create_tree


class TestTree:
    @pytest.mark.parametrize(
        "levels, path",
        [
            ( 5,    "tree.txt"),
            (-1,    "tree.t"),
        ]
    )
    #correct creation of file
    def test_file_creation(self, levels, path):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, path)
            create_tree(levels, file_path)
            assert os.path.isfile(file_path)

    @pytest.mark.parametrize(
        "levels, path",
        [
            (10, "tree.txt"),
        ]
    )
    #correct file content
    def test_file_content(self, levels, path):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, path)
            create_tree(levels, file_path)

            with open(file_path, "r") as f:
                with open("templates/tree_level10.txt", "r") as expected_result:
                    assert f.read() == expected_result.read()
