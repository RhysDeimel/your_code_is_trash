# Scaffold
Basic python tox, pytest, & coverage project structure


## Installation
Simply clone, remove the `.git` folder (re-init if you like), and change any `your_code_is_trash` references to that of your
project name. EZPZ


## Usage
Slap your venv in the root dir, install the dev requirements with `pip install -e . --group dev`,
then run `pytest` or `tox` from the root dir to see the results. 
Tox will run through any specified python versions you put in the `env_list` 
in the relevant tox settings in `pyproject.toml`. 
For added bonus, I've thrown in coverage and markers for slow tests, and incremental tests.

Coverage will run every time you call `tox`, and it will also populate the htmlcov folder with
[jazz](https://www.youtube.com/watch?v=xuPSIbABYVU) so you can see how lazy you've been with your test coverage.
Feel free to check the `pyproject.toml` to see adjustable failure rates for coverage.
Additionally, coverage is aggregated across all the specified python versions,
so your body better be ready for that one.

With the slow test markers, tox will automatically run them. If you want to run pytest _in_ tox while skipping the
slow tests, use `tox -- -m "not slow"`. Keep in mind, this will mess with the coverage reporting.

If you only care about running the tests (and nothing else), you don't have to use tox. You can simply run `pytest`.
To run the slow tests, you will have to use the marker: `pytest --runslow`. 

> [!CAUTION]
> Depending on how you're importing packages, running pytest outside tox might fail.
> Relative vs absolute imports and all that nonsense.

We also have spellcheck enabled via [pyspelling](https://facelessuser.github.io/pyspelling/). 
It will read the configuration in `.pyspelling.yml` and ignore anything found in `.wordlist.txt`.
To check your spelling, run:
```
pyspelling
```


## Docs
This project uses [mkdocs](https://www.mkdocs.org/) with [material](https://squidfunk.github.io/mkdocs-material/) to
generate project documentation. In addition to what markdown files you explicitly write, this project also demonstrates
how to automatically generate docs from python docstrings. Neat!

Not only that, but pytest is also configured to run tests over any examples in said docstrings via [doctests](https://docs.pytest.org/en/latest/how-to/doctest.html).
How cool is that?

To see what docs are generated on your local, install the project, and then run the following command:
```
mkdocs serve
```

### Versions
This documentation is versioned using [mike](https://github.com/jimporter/mike). 
It is a utility integrated into mkdocs-material that makes it easy to deploy multiple versions of documentation.
It does so by pushing documentation to a branch (`gh-pages`) to a versioned folder,
and switches between these folders based on a dropdown option selected on the main documentation page.

As per the project:
> mike is built around the idea that once you've generated your docs for a particular version,
> you should never need to touch that version again. 
> This means you never have to worry about breaking changes in MkDocs,
> since your old docs (built with an old version of MkDocs) are already generated and sitting in your gh-pages branch.
> 
> While mike is flexible, it's optimised around putting your docs in a <major>.<minor> directory, 
> with optional aliases (e.g. latest or dev) to particularly notable versions. 
> This makes it easy to make permalinks to whatever version of the documentation you want to direct people to.

This can make viewing the documentation of past versions a little tricky. 
However, I believe the trade-off is worth it. 
I considered deploying WIP docs for changes in a branch, 
but there were too many potential edge cases around cleanup that made the idea unpalatable. 

Documentation deployments are fully automatic via GitHub workflows.
The only config you might need to do would be to navigate to the repository settings,
select `Pages`, change the branch to `gh-pages`, and add any custom domains and HTTPS settings. 

## Directory Structure
```
.
├── .pyspelling.yml  # spellcheck config
├── .wordlist.txt  # whitelist for spellcheck
├── Dockerfile
├── mkdocs.yml  # docs configuration
├── pyproject.toml  # project and tool settings
├── README.md
├── docs
│   └── markdown files for document generation
├── htmlcov
│   └── reporting html, css, and js files
├── src
│   ├── conftest.py
│   └── your_code_is_trash  # your actual project code
│       ├── __init__.py
│       ├── __main__.py
│       ├── calculator.py  # docstrings with doctest
│       └── foo.py
├── tests
│   ├── __init__.py
│   ├── conftest.py  # global fixtures
│   ├── functional
│   │   ├── __init__.py
│   │   ├── test_foo.py
│   │   └── test_step.py  # pytest incremental fixture 
│   ├── integration
│   │   ├── __init__.py
│   │   └── test_foo.py
│   └── unit
│       ├── __init__.py
│       └── test_foo.py
└── venv        
```
