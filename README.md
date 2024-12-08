## How to set up a repo like this from scratch, using VSCode

1. Install uv (https://docs.astral.sh/uv/). make sure this is done in/for a Python environment which is referenced in your system $PATH.
2. Create a new local directory and open it in VSCode.
3. Open a terminal window in VSCode (Windows hotkey: ``Ctrl + ` ``). 
4. Run `uv init` in the terminal. A bunch of files should be automatically added to the directory, and git is initialised.
5. Commit this state as an initial commit in git, and publish to Github. 
    * The repo will need to be public in order for it to be deployed to Streamlit Community Cloud.
    * If you create the repo via Github, initialise it empty (without a README file, for example).
6. Run `hello.py` in terminal using the command `uv run hello.py`.
    * This should create the environment using `uv`, including the creation of a `.venv` subdirectory (containing a newly created vitual environment for your project) and a `uv.lock` file in the root directory (which specifies your project's dependencies).
7.  Add `streamlit` to your virtual environment by running `uv add streamlit` in the terminal. Streamlit and its dependencies should all be added to the virtual environment, the `pyproject.toml` file and the `uv.lock` file.
    * Check that everthing is working by runn
