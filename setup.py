import os
import subprocess
import shutil

# Create project directories if they don't exist
directories = [
    'data',
    'data/raw',
    'data/processed',
    'templates',
    'notebooks',
    'tests',
    'src'
]

for directory in directories:
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        print(f"Error creating directory: {directory}")
        print(f"Error message: {str(e)}")
        break

# Get the project name from the project folder
project_folder = os.path.basename(os.getcwd())


# Generate project structure tree
def generate_project_structure(directory):
    tree = ''
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            tree += f"- {item}/\n"
            tree += generate_project_structure(item_path)
        else:
            tree += f"- {item}\n"
    return tree


# .gitignore, README.md, LICENSE.md contents
gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
# Config file for Airtable, OpenAI and Linkedin account information and API keys
config.py
#virtual environment
myenv/
# C extensions
*.so
# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec
# Installer logs
pip-log.txt
pip-delete-this-directory.txt
# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/
# Translations
*.mo
*.pot
# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
# Flask stuff:
instance/
.webassets-cache
# Scrapy stuff:
.scrapy
# Sphinx documentation
docs/_build/
# PyBuilder
.pybuilder/
target/
# Jupyter Notebook
.ipynb_checkpoints
# IPython
profile_default/
ipython_config.py
# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version
# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock
# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml
# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/
# Celery stuff
celerybeat-schedule
celerybeat.pid
# SageMath parsed files
*.sage.py
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
# Spyder project settings
.spyderproject
.spyproject
# Rope project settings
.ropeproject
# mkdocs documentation
/site
# mypy
.mypy_cache/
.dmypy.json
dmypy.json
# Pyre type checker
.pyre/
# pytype static type analyzer
.pytype/
# Cython debug symbols
cython_debug/
# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
"""
license_content = """
MIT License
Copyright (c) 2023 Orhan Baran
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
readme_content = f"""# {project_folder}

Description: Description will go here

## Project Structure

The structure of the project is as follows:

{generate_project_structure('.')}
"""

try:
    # Check if virtual environment exists
    if not os.path.exists('venv'):
        # Create virtual environment
        subprocess.run(['python', '-m', 'venv', 'venv'])

    # Check if .gitignore exists in venv directory
    venv_gitignore_path = os.path.join('venv', '.gitignore')
    if os.path.exists(venv_gitignore_path):
        # Edit .gitignore in main directory
        with open(venv_gitignore_path, 'a') as gitignore_file:
            # Add or modify your desired content in the .gitignore file
            gitignore_file.write(gitignore_content)
    else:
        # Create .gitignore in main directory
        with open(venv_gitignore_path, 'w') as gitignore_file:
            # Add your desired content to the .gitignore file
            gitignore_file.write(gitignore_content)

    # Activate virtual environment
    activate_script = os.path.join('venv', 'bin', 'activate')
    activate_command = f'source {activate_script}'
    subprocess.run(activate_command, shell=True)

    # Create README.md file in main directory if it doesn't exist
    if not os.path.exists('README.md'):
        with open('README.md', 'w') as readme_file:
            readme_file.write(readme_content)

    # Create LICENSE.md file in main directory if it doesn't exist
    if not os.path.exists('LICENSE.md'):
        with open('LICENSE.md', 'w') as license_file:
            license_file.write(license_content)

    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w') as requirements_file:
            requirements_file.write('')



except Exception as e:
    print(f"An error occurred: {e}")
    raise SystemExit(1)

print("Setup completed successfully.")

# Initialize Git repository
subprocess.run(['git', 'init'])

# Add all files
subprocess.run(['git', 'checkout', '-b', 'main'])

# change local branch name from 'main' to 'version1'
subprocess.run(['git', 'branch', '-M', 'version1'])

# Add all files
subprocess.run(['git', 'add', '.'])

# Perform initial commit
subprocess.run(['git', 'commit', '-m', 'Initial commit'])

# Connect to remote GitHub repository
repository_url = f"git@github.com:orhanbaran/{project_folder}.git"
subprocess.run(['git', 'remote', 'add', 'origin', repository_url])

# Push to remote GitHub repository
subprocess.run(['git', 'push', '-u', 'origin', 'version1'])
