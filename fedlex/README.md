# SPARQL Abfragen auf Fedlex

## Tutorial

Das Tutorial funktioniert ohne Installation. Für Testingzwecke wird jedoch die Sparql Notebook Extension empfohlen (siehe )

## Eigene Samples

Eigene Samples sind im Sparql Notebook gespeichert. Diese können als Markdown Datei expoertiert werden.

### Sparql Notebook Setup

You can raun any `.sparqlbook` file in VS Code:
- First install [Sparql Notebook Extension](https://marketplace.visualstudio.com/items?itemName=Zazuko.sparql-notebook) (Documentation)
- Connect to a remote server by clicking the + button in the SPARQL Connections panel in the VS Code extension. 
- Fedlex Endpoint: Fill in the server URL and optional credentials: https://fedlex.data.admin.ch/sparqlendpoint
- Run the cell: Click on the traingle left of a cell inside the editor.

This connection is used throughout the entire notebook, except when a cell defines its own endpoint.

### Export as Markdown

Right click a `.sparqlbook`file and select Export to Markdown.