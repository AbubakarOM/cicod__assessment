# CICOD Automated Script

## Tools and Framework Used.
* Language: Python
* Language version: 2.7.6
* Selenium version: 3.141.0
* brew
* Webdriver: Chrome
* Framework: Behave
* Framework version: 1.2.6
* IDE: VScode
* OS: WINDOWS 10
## Installation and usage.
Installation and usage can be done via the terminal or used through the Pycharm IDE or VsCode.
### Using the Terminal
* Open terminal
* Install python by running _**"brew install python3"**_
* Install behave and selenium by running _**"pip3 install behave selenium"**_
* Install chromedriver by running _**"brew cask install chromedriver"**_
* Navigate to the folder cloned from git.
* run >behave ./features/addToCart.feature
### Using the IDE
#### Create a Python Virtual environment.
So you can have an isolated working directory of the Python environment so
as to keep the global Python free of installed dependencies. This ensures 
that the environment created only affects the project. This means the 
environment forms our project working directory.
> **STEPS:**
> * Open terminal
> * Check if **virtualenv** is installed on the system: virtualenv --version.
> * If it is not installed, install using _"pip3 install virtualenv"_.
> * If it is installed, go ahead and create a directory where the virtual
> environment will be located.
> * Navigate to the directory and create the new virtual environment. 
>by using the command _"virtualenv <name_of_environment>"_
> * Install selenium with _"pip install selenium"_
> * Install behave with _"pip install behave"_
> * Or you can specify the versions of these libraries in a requirements.txt file.
> * And install via the _txt_ file with _"pip install -r requirements.txt"_
> * Copy this project into the environment
> * Activate the virtual environment by using 
>_source <name_of_environment>\Scripts\Activate_
**NB:** To deactivate, just type _**deactivate**_ and hit enter

**For VsCode:**
> *  Install some extensions to enable behave framework and Python as well. They are:
* Behave Theme
* Behave Test Explorer
* Python
* Python Extension Pack

**IDE ALERT:** 
> * Except for the extension added on the VsCode, Pycharm (Community Edition) has a very similar setup.

#### Project Execution via Pycharm IDE
* Install Pycharm (Professional Edition).
* Open and navigate to the folder where this project has been copied 
and open it.
* Click the **Run** Tab and click add/edit configuration.
* Click the **+** and select **Behave**
* Name the config
* On the **Feature files or folders**, navigate to the Features folder of 
this project.
* Ensure the virtualenv is being used as the interpreter.
* Click **Apply** and **OK**.

### Project Execution for Pycharm or VsCode
>Navigate into the features folder and run **"behave"**

## What does this script do?

The Script launches the CICOD site and simulates the following processes
* SignUp
