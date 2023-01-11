# Portfolio

This Flask application serves as my portfoliio and is currently hosted on Heroku.com


## New Deployment


### Login to Heroku
```
nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `heroku login`
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/3e9f26e3-c014-43c9-8035-a3d4fb742093?requestor=SFMyNTY.g2gDbQAAAAw0Ny4zOS4xNDcuMTluBgBQqxyihQFiAAFRgA.W1XESGkTSiuLy9JNB-YLXs_yGB5Jgl2wvSrfsYHN_OY
 ›   Warning: Cannot open browser.
Logging in... done
Logged in as _nicholas.spell@fiserv.com_
nick@DESKTOP-A7K2DC1:~/projects/portfolio$
nick@DESKTOP-A7K2DC1:~/projects/portfolio$

```
### Heroku Configuration
```
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `heroku git:remote -a portfolio-v1`
set git remote heroku to https://git.heroku.com/portfolio-v1.git
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `heroku buildpacks:clear`
Buildpacks cleared. Next release on portfolio-v1 will detect buildpacks normally.
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git`
Buildpack added. Next release on portfolio-v1 will use https://github.com/moneymeets/python-poetry-buildpack.git.
Run git push heroku main to create a new release using this buildpack.
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `heroku buildpacks:add heroku/python`
Buildpack added. Next release on portfolio-v1 will use:
  1. https://github.com/moneymeets/python-poetry-buildpack.git
  2. heroku/python
Run git push heroku main to create a new release using these buildpacks.
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `git add .`
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `git commit -am 'updates app'`
```

### Deployment
```
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$ `git push heroku master`
Enumerating objects: 86, done.
Counting objects: 100% (85/85), done.
Delta compression using up to 4 threads
Compressing objects: 100% (61/61), done.
Writing objects: 100% (76/76), 29.77 KiB | 29.77 MiB/s, done.
Total 76 (delta 15), reused 70 (delta 12), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-22 stack
remote: -----> Using buildpacks:
remote:        1. https://github.com/moneymeets/python-poetry-buildpack.git
remote:        2. heroku/python
remote: -----> Python Poetry app detected
remote: -----> No Poetry version specified in POETRY_VERSION config var. Defaulting to 1.2.0.
remote: -----> Generate requirements.txt with Poetry
remote: -----> Install Poetry
remote:        Retrieving Poetry metadata
remote:        
remote:        # Welcome to Poetry!
remote:        
remote:        This will download and install the latest version of Poetry,
remote:        a dependency and package manager for Python.
remote:        
remote:        It will add the `poetry` command to Poetry's bin directory, located at:
remote:        
remote:        /app/.local/bin
remote:        
remote:        You can uninstall at any time by executing this script with the --uninstall option,
remote:        and these changes will be reverted.
remote:        
remote:        Installing Poetry (1.2.0)
remote:        Installing Poetry (1.2.0): Creating environment
remote:        Installing Poetry (1.2.0): Installing Poetry
remote:        Installing Poetry (1.2.0): Creating script
remote:        Installing Poetry (1.2.0): Done
remote:        
remote:        Poetry (1.2.0) is installed now. Great!
remote:        
remote:        To get started you need Poetry's bin directory (/app/.local/bin) in your `PATH`
remote:        environment variable.
remote:        
remote:        Add `export PATH="/app/.local/bin:$PATH"` to your shell configuration file.
remote:        
remote:        Alternatively, you can call Poetry explicitly with `/app/.local/bin/poetry`.
remote:        
remote:        You can test that everything is set up by executing:
remote:        
remote:        `poetry --version`
remote:        
remote: -----> Add Poetry to the PATH
remote: -----> Force usage of active Python and disable creation of virtualenvs
remote: -----> Export requirements.txt from Poetry
remote: The currently activated Python version 3.10.6 is not supported by the project (3.10.4).
remote: Trying to find and use a compatible version. 
remote:        Skipping virtualenv creation, as specified in config file.
remote: -----> Export Python version from Poetry to Heroku runtime.txt file
remote: -----> Read Python version from poetry.lock
remote: -----> Write 3.10.4 into runtime.txt
remote: -----> Python app detected
remote: -----> Using Python version specified in runtime.txt
remote:  !     
remote:  !     A Python security update is available! Upgrade as soon as possible to: python-3.10.9
remote:  !     See: https://devcenter.heroku.com/articles/python-runtimes
remote:  !     
remote: -----> No change in requirements detected, installing from cache
remote: -----> Using cached install of python-3.10.4
remote: -----> Installing pip 22.3.1, setuptools 63.4.3 and wheel 0.37.1
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Ignoring colorama: markers 'platform_system == "Windows" and python_full_version == "3.10.4"' don't match your environment
remote:        Collecting setuptools==65.6.3
remote:          Downloading setuptools-65.6.3-py3-none-any.whl (1.2 MB)
remote:        Installing collected packages: setuptools
remote:          Attempting uninstall: setuptools
remote:            Found existing installation: setuptools 63.4.3
remote:            Uninstalling setuptools-63.4.3:
remote:              Successfully uninstalled setuptools-63.4.3
remote:        Successfully installed setuptools-65.6.3
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 53.8M
remote: -----> Launching...
remote:        Released v4
remote:        https://portfolio-v1.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/portfolio-v1.git
   72d3049..0fedea2  master -> master
(portfolio-py3.10) nick@DESKTOP-A7K2DC1:~/projects/portfolio$
```
