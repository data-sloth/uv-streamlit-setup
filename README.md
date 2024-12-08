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
9. Now set up your repo as a Python package to make it easier to organise your code and call functions and classes from different subdirectories. It will be editable so it will stay up to date as you modify your repo going forward.
    * Create a `src` directory in your workspace, and add another subdirectory inside it with the name of your project (the name of this folder is going to be what you call the repo package from. Don't use any special characters in it.).
    * Add the following to the `pyproject.toml` file (replacing `myproject` with your chosen name`):

            [build-system]
            requires = ["setuptools>=42"]
            build-backend = "setuptools.build_meta"

            [tool.setuptools.packages.find]
            where = ['src']
            include = ['myproject*']

    * You can add further subdirectories and functions under `myproject` - see this repo for an example setup. Note how scripts in different directories of equal hierarchy can call each other. 
    * Add code to `hello.py` that calls functions under `myproject` - see how the import works in the code in this repo. In order to run the app smoothly in Streamlit Community Cloud, it is best to keep the main script to be run by streamlit at the root of your repo.
    * Install your package by adding it in terminal: `uv add --editable --dev {YOUR-PROJECT-NAME}`. Replace `{YOUR-PROJECT-NAME}` with the name of your project given in `pyproject.toml` (so in the case of this repo, the command would be `uv add --editable --dev uv-streamlit-setup`).
    * You can check that the install was successful by running the command `uv pip list` - your project package should show up in the list.
    * Run the updated `hello.py` using streamlit in the terminal with the command `streamlit run hello.py`. The streamlit app should launch in you browser and display expected outputs.
    * You can now try modifying your code in the package (e.g. add a new function in a module and call it in `hello.py`); rerunning the streamlit dashboard (which you can set to 'Always rerun' in the top right) you should find that these updates are reflected without having to reinstall the package.

10. Now you can deploy the app! First, make sure to commit and sync your latest code to your repo in Github. Then in the top right corner of your locally-running streamlit app you can click the 'Deploy' button and choose the option to 'Deploy now' to Streamlit Community Cloud. Confirm the repo url, branch and main file path that is shown on the subsequent form, come up with a url prefix for your app. If you do not yet have an account (or are not logged in), you will need to create/log in to your Streamlit account first. Hit the Deploy button and within a few seconds your app will be live!



