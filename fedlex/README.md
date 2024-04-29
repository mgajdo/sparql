# SPARQL Abfragen auf Fedlex

## Tutorial

Das Tutorial funktioniert auch ganz ohne Installation (siehe Tutorial)[TUTORIAL.md]. Die Samples des Schweizerischen Bundeskanzlei sind für Testingzwecke als `.sparqlbook` Datei gespeichert. Sie bfeindet sich im Ordner `/tutorial`. 

You can run any `.sparqlbook` file in VS Code:
- First install [Sparql Notebook Extension](https://marketplace.visualstudio.com/items?itemName=Zazuko.sparql-notebook) (Documentation)
- Connect to a remote server by clicking the + button in the SPARQL Connections panel in the VS Code extension. 
- Fedlex Endpoint: Fill in the server URL and optional credentials: https://fedlex.data.admin.ch/sparqlendpoint
- Run the cell: Click on the traingle left of a cell inside the editor.
- This connection is used throughout the entire notebook, except when a cell defines its own endpoint.
- Right click a `.sparqlbook`file and select Export to Markdown.

## Samples

Die Originaldatei der Schweizerischen Bundeskanzlei mit Beispielen ist unter `fedlex_WIP.ipynb` gespeichert und lässt sich in Jupyter Lab anzeigen. `version_link.ipynb` enthält ein Tutorial zu **version.link Schema** und dem Anwendungsfall des historisierten Gemeindeverzeichnisses. Sie bfeindet sich im Ordner `/samples`. 

Zur Installation und Ausführung von Jupyter Lab siehe `sparql/README.md`. Zusätzlich wird `kglab` installiert.

## Documentation

Die UTI Patterns und weitere Informationen zum Gesetzgebungsprozess sind im Ordner `doc`abgespeichert.

## Data

Die Jolux Ontologie ist in `dat` abgespeichert.