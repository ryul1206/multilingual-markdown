import os
import importlib.util
import pytest


# Collect all the examples from the `examples` folder.
_current_dir = os.path.dirname(os.path.realpath(__file__))
_example_dir = os.path.abspath(os.path.join(_current_dir, "..", "examples", "api-examples"))
_file_list = os.listdir(_example_dir)

# Filter out the non-python files.
examples = [file for file in _file_list if file.endswith(".py")]


@pytest.mark.parametrize("example_fname", examples)
def test_examples(example_fname):
    """Test the examples in the `examples` folder."""
    # Import the example.
    ex = os.path.join(_example_dir, example_fname)
    spec = importlib.util.spec_from_file_location(example_fname, ex)
    module = importlib.util.module_from_spec(spec)
    # Execute the example.
    spec.loader.exec_module(module)
    main = module.main
    main()


if __name__ == "__main__":
    pytest.main()
