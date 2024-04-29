# SPARQL queries to Fedlex data
Adapted from [## Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/). Following the instructions below will return a table in HTML.

## Setup

- Create new directory
- Clone repo to local directory `git clone https://github.com/mgajdo/spraql.git`
- cd into repo `cd ` to new directory

### Python setup (SPARQL Tutorial)

- Install Python and pip (install dependencies if the project is cloned) `python3 -m pip install --upgrade pip`. [Installation advice](https://packaging.python.org/en/latest/tutorials/managing-dependencies/) for Python projects.
- Initialize a Virtual Environment: `python -m venv myenv`. The dependencies will be installed in the /myenv directory
- Activate environment: `source myenv/bin/activate`
- Install the Requests and Pandas library `pip install requests pandas`. [Documentation](https://pandas.pydata.org/docs/index.html)

Following the instructions below will return the (meta-)data of the Federal Constitution of the Swiss Confederation from the Fedlex SPARQL Endpoint in HTML format as a result of a query. Inside the `fedlex/tutorial`directory:

1. Insert your SPARQL query inside `sparql_query.txt`.
2. (optional) Add you custom endpoint and assign a variable in `sparql_endpoints.txt`. Adapt the variable to your endpoint in `main.py` line 11. The default endpoint is `F=https://fedlex.data.admin.ch/sparqlendpoint`.
4. Run `python main.py` inside the shell at the root directory of the project to run the program.

Files:
- `query.py` contains the logic
- `display_result.py` renders the code as HTML
- `sparql_endpoints.txt` input file containing available SPARQL Endpoints. (Default is set to Fedlex.)
- `sparql_query.txt` input file containing the SPARQL query to the endpoint in question.

## Jupyter setup (KG Lab)

The **kglab** library provides a simple abstraction layer in Python 3.7+ for building knowledge graphs, leveraging Pandas, NetworkX, RAPIDS, RDFLib, Morph-KGC, pythonPSL, and many more. From to *Graph Data Science*: <https://derwen.ai/docs/kgl/>

- Install the Jupyter `pip install jupyterlab`. [Documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- Start Jupyter Lab using `jupyter lab`. If your notebook files are not in the current directory, you can pass your working directory path as argument when starting JupyterLab, e.g. `jupyter lab kglab/fedlex`. JupyterLab will open automatically in your browser. To shut down press `ctrl + C` (MacOS).


### Using `kglab` as a library for your Python project

Using pip or pipenv:
```bash
python3 -m pip install kglab
```

Or, install from source:

Install from pip wheel ([Build Wheel archives for your requirements and dependencies](https://pip.pypa.io/en/stable/cli/pip_wheel/))
```bash
python3 -m pip install -U pip wheel 
```
The -r flag specifies the installs from the given requirements file. (https://pip.pypa.io/en/stable/topics/repeatable-installs/#using-a-wheelhouse-aka-installation-bundles) 
```bash
python3 -m pip install -r requirements.txt
```

*w[Why you should not use setup.py.](https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install?rq=3)*

### Usage

See the **tutorial notebooks** in the `examples` subdirectory for sample code and patterns to use in integrating **kglab** with other graph libraries in Python: <https://derwen.ai/docs/kgl/tutorial/>

To run some simple uses of this library:

```python
import kglab

# create a KnowledgeGraph object
kg = kglab.KnowledgeGraph()

# load RDF from a URL
kg.load_rdf("http://bigasterisk.com/foaf.rdf", format="xml")

# measure the graph
measure = kglab.Measure()
measure.measure_graph(kg)

print("edges: {}\n".format(measure.get_edge_count()))
print("nodes: {}\n".format(measure.get_node_count()))

# serialize as a string in "Turtle" TTL format
ttl = kg.save_rdf_text()
print(ttl)
```
### Build and Docker

Note: unless you are contributing code and updates,
in most use cases won't need to build this package locally.

To set up the build environment locally, see the 
["Build Instructions"](https://derwen.ai/docs/kgl/build/)
section of the online documentation.

Using Docker: 
For a simple approach to running the tutorials, see use of _docker compose_:
<https://derwen.ai/docs/kgl/tutorial/#use-docker-compose>

Also, container images for each release are available on DockerHub:
<https://hub.docker.com/repository/docker/derwenai/kglab>

To build a container image and run it for the tutorials:

```bash
docker build --pull --rm -f "docker/Dockerfile" -t kglab:latest .
docker run -p 8888:8888 -it kglab
```

To build and run a container image for testing:

```bash
docker build --pull --rm -f "docker/testsuite.Dockerfile" -t kglabtest:latest .
docker run --rm -it kglabtest
```
