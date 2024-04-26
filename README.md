# SPARQL queries to Fedlex data
Adapted from [## Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/). Following the [instructions](https://github.com/mgajdo/sparql?tab=readme-ov-file#instructions) below will return a table in HTML.

## Instructions
1. Insert your SPARQL query inside `sparql_query.txt`.
2. (optional) Add you custom endpoint and assign a variable in `sparql_endpoints.txt`. Adapt the variable to your endpoint in `main.py` line 11. The default endpoint is `F=https://fedlex.data.admin.ch/sparqlendpoint`.
2. Run `python main.py` inside the shell at the root directory of the project to run the program.

## Files
`query.py` contains the logic

`display_result.py` renders the code as HTML

## Python setup
- Create new directory
- Clone repo to local directory `git clone https://github.com/mgajdo/spraql.git`
- cd into repo `cd ` to new directory
- Install Python and pip (install dependencies if the project is cloned) `python3 -m pip install --upgrade pip`. [Installation advice](https://packaging.python.org/en/latest/tutorials/managing-dependencies/) for Python projects.
- Initialize a Virtual Environment: `python -m venv myenv`. The dependencies will be installed in the /myenv directory
- Activate environment: `source myenv/bin/activate`
- Install the Requests and Pandas library `pip install requests pandas`. [Documentation](https://pandas.pydata.org/docs/index.html)