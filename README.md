## How to set up a repo like this from scratch, using VSCode

1. Install uv (https://docs.astral.sh/uv/). make sure this is done in/for a Python environment which is referenced in your system $PATH.
2. Create a new local directory and open it in VSCode.
3. Open a terminal window in VSCode (Windows hotkey: ``Ctrl + ` ``). 
4. Run `uv init` in the terminal. A bunch of files should be automatically added to the directory, and git is initialised.
5. Commit this state as an initial commit in git, and publish to Github. 
    * The repo will need to be public in order for it to be deployed to Streamlit Community Cloud.
    * If you create the repo via Github, initialise it empty (without a README file, for example).
