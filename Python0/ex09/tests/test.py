from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0

# dist/  << emty folder for build
# ├── LICENSE
# ├── pyproject.toml
# ├── README.md
# ├── src/
# │   └── example_package_YOUR_USERNAME_HERE/  << ft_package
# │       ├── __init__.py
# │       └── example.py  << ft_package.py
# └── tests/
#     └── test.py  << i put my test.py here
# tar -czvf ft_package-0.0.1.tar.gz ./dist/ft_package # wrong way
# python3 -m pip install --upgrade build
# run "python3 -m build" from the same directory
# where pyproject.toml is located:
# pip install ./dist/ft_package-0.0.1.tar.gz
# if build issue check .toml and erro message# can remode the url stuff
# will auto build dist >> *.egg-info
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
