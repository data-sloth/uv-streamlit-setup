## How to set up a repo like this from scratch, using VSCode - *instructions for dummies*!

1. Install uv (https://docs.astral.sh/uv/). Make sure this is done in/for a Python environment which is referenced in your system $PATH, otherwise you won't be able to call uv in terminal.
2. Create a new local directory and open it in VSCode.
3. Open a terminal window in VSCode (Windows hotkey: ``Ctrl + ` ``). 
4. Run `uv init` in the terminal. A bunch of files should be automatically added to the directory, and git is initialised.
5. Commit this state as an initial commit in git, and publish to Github. 
    * The repo will need to be public in order for it to be deployed to Streamlit Community Cloud.
    * If you create the repo via Github, initialise it empty (without a README file, for example).
6. Run `hello.py` in terminal using the command `uv run hello.py`.
    * This should create the environment using `uv`, including the creation of a `.venv` subdirectory (containing a newly created vitual environment for your project) and a `uv.lock` file in the root directory (which specifies your project's dependencies).
7.  Add `streamlit` to your virtual environment by running `uv add streamlit` in the terminal. Streamlit and its dependencies should all be added to the virtual environment, the `pyproject.toml` file and the `uv.lock` file. You can install other dependencies in this way as well (just like using `pip install`).
8. Check that everthing is working by:
    1. Modifying `hello.py` to use streamlit,
    2. Activating the virtual environment in terminal by running `.venv\Scripts\activate`.
    3. Running `hello.py` using streamlit in the terminal with the command `streamlit run hello.py`. The streamlit app should launch in you browser and display as expected. 
    4. To stop running the app, use `Ctrl + C` in the terminal. This will allow you to continue running other commands in terminal (you will have to close the webpage manually though).


