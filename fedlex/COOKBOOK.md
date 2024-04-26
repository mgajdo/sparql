
[Zurück zu SPARQL](/README.md)

[Zurück zu Fedlex](fedlex/README.md)

# Cookbook

Beispiele übernommen aus: [Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/)

https://zazuko.com/get-started/sparql-query/

## Fedlex Tutorial

### URIs und Vokabular

[## Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/)

[Fedlex Vokabular](https://fedlex.data.admin.ch/de-CH/home/convention) (URIs Templates for Legal Resources in Switzerland)

Die [URIs von Fedlex](https://fedlex.data.admin.ch/de-CH/home/convention) werden nach einer `Convention` beschrieben: "Switzerland publishes several collections of legal resources available in German, French and Italian and in some cases translated to Romanish or English. Most of the information published are documents, but some are just information about a legislative event, such as the starting date of a consultation published in the Federal gazette, or information about consultation events. 

The various publications are: 
- **Federal Gazette (BBl - Bundesblatt)** - publication of announcements and messages
- **Official Compilation (AS - Amtliche Sammlung)** - publication of the law
- **Classified Compilation (SR -Systematische Sammlung)** - publication of the consolidated version of the law
- **Consultation procedures (Vernehmlassungen)** - publication of information about coming, present and future consultation
- **Register of sectoral agreements with the European Union** - publication of European texts, which are applicable to Switzerland because of sectoral agreements with the EU
- **Treaty** - publication of additional data on all agreements governed by international law that are in force for Switzerland or that Switzerland has signed, as well as information about major legally binding agreements and non-binding texts"

Alle URIs beginnen mit https://fedlex.data.admin.ch/eli/:
- Die Einträge für die AS beginnen mit https://fedlex.data.admin.ch/eli/oc/ 
- Die Einträge für die SR beginnen mit https://fedlex.data.admin.ch/eli/cc/

[Mehr zur Publikation von "legal resources" in der Schweiz](https://www.fedlex.admin.ch/eli/cc/2004/745/de)

Die URIs von Fedlex richten sich nach dem europäischen ELI-Standard (European Legislation Identifier) zur Bezwichnung von Rechtstexten. The [European Legislation Identifier (ELI)](https://eur-lex.europa.eu/eli-register/about.html) is a system to make legislation available online in a standardised format, so that it can be accessed, exchanged and reused across borders.

[Datenmodell JOLux](https://fedlex.data.admin.ch/de-CH/home/models)

Das von Fedlex verwendete Datenmodell heisst **JOLux**. Es basiert auf dem [FRBR-Standard](https://de.wikipedia.org/wiki/Functional_Requirements_for_Bibliographic_Records) (Functional Requirements for Bibliographic Records), einem Entity-Relationship-Modell zur Beschreibung bibliographischer Daten, das für die Beschreibung von Rechtstexten adaptiert wurde. Ursprünglich aus Luxemburg stammend wird es inzwischen von der Schweiz und Luxemburg gemeinsam weiterentwickelt.

Wichtige Namespaces:
* `fedlex`: [Namespace für AS und SR Einträge](https://fedlex.data.admin.ch/eli/)
* `jolux` : [Vokabular für das JOLux Datenmodell](http://data.legilux.public.lu/resource/ontology/jolux#)
* `skos` : [SKOS Vokabular](http://www.w3.org/2004/02/skos/core#)
* `rdf` : [RDF Vokabular](http://www.w3.org/1999/02/22-rdf-syntax-ns#)

### Metadaten-Explorer

Die URI bzw. die URL der Bundesverfassung `https://fedlex.data.admin.ch/eli/cc/1999/404` verweist auf den Gesetzestext. Im [Metadaten-Explorer](https://fedlex.data.admin.ch/de-CH/metadata) kann man die damit verknüpften Linked Data Triples durchsuchen. 

Eine Abfrage der Linked Data Triples der Bundesverfassung über den Metadaten-Explorers weist stets folgende URL auf:
- die Sprache als path `/de-CH` 
- der Gesetzestext als Parameter: `/metadata?value=`

Die zusammengesetzte URL: https://fedlex.data.admin.ch/de-CH/metadata?value=https://fedlex.data.admin.ch/eli/cc/1999/404

### Fedlex SPAQL API

Die API von Fedlex ist auch über einen SPARQL Endpoint verfügbar:
- [API Endpoint](https://fedlex.data.admin.ch/sparqlendpoint)
- [Web-Interface](https://fedlex.data.admin.ch/de-CH/sparql) für Testzwecke 

Die Website https://fedlex.admin.ch und alle dort angzeigten Daten sind in Form von **Linked Data**, d.h. Triples im Datenformat RDF (Resource Description Framework) in einem Triple Store gespeichert und mit Hilfe des SPARQL Endpoints  maschinenlesbar. Im Gegensatz zu relationalen Datenbanken werden die Daten in Triple Stores als  **Triples** (daher mit Tabellen nicht visualisierbar) gespeichert. 

Mehr Informationen zu SPARQL:
- [SPARQL-Tutorial 1](https://jena.apache.org/tutorials/sparql.html) 
- [SPARQL Tutorial 2](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) from Wikidata

Eine SPARQL Abfrage ist nichts anderes als ein POST-Request an den entsprechenden Triple Store Datenbank Server. Wir benutzen dazu das Web-Interface:

[**Web-Interface**](https://fedlex.data.admin.ch/sparqlendpoint)

SPARQL Queries folgen einem grundlegenden Aufbau, der immer gleich lautet:

```
SELECT * WHERE 
{
    ?subject ?predicate ?object.   
}
```

Triples folgen der grammatikalischen Struktur **Subjekt -> Prädikat -> Objekt**.  Einzelne Positionen der Triples können bewusst undefiniert gelassen und mit der Variable `?`bezeichnet werden.

Das Ziel unserer ersten Query in der Bundesverfassung ist es Triples suchen, in denen die Bundesverfassung als **Subjekt** erscheint. Alle Triples müssen dieses Muster erfüllen:

```
SELECT DISTINCT ?Prädikat ?Objekt WHERE {
    
    <https://fedlex.data.admin.ch/eli/cc/1999/404> ?Prädikat ?Objekt .
} 
```

Die eingefügte URL führt zum Gesetzestext der Bundesverfassung in der Systematischen Rechtssammlung. (Der Path `/cc` führt zur Classified Compilation):

https://fedlex.data.admin.ch/eli/cc/1999/404

Die URI der deutschen Sprachversion https://fedlex.data.admin.ch/eli/cc/1999/404/de führt uns zu den Metadaten der Bundesverfassung. Wir sehen sowohl den Titel als auch die Abkürzung auf Deutsch. 

https://fedlex.data.admin.ch/eli/cc/1999/404/de 

Diese URI beschreibt nicht den deutschen Text der eigentlichen Bundesverfassung sondern repräsentiert nur die "Kopfdaten" der Bundesverfassung, also Titel und Abkürzung auf Deutsch. Der eigentliche Inhalt der Gesetzestexte ist über die "Consolidations-Versionen" der SR Einträge angebunden im Datenmodell von JoLux existieren Innerhalb eines `jolux:ConsolidationAbstract` verschiedene Sprachversionen. Diese sind vom `rdf:type` `jolux:Expression` und sind durch die Eigenschaft `jolux:isRealizedBy` mit dem sprachübergreifenden Eintrag des `jolux:ConsolidationAbstract` verknüpft. 

In SPARQL ist die `URI der Bundesverfassung` das **Subjekt** der SPARQL-Abfrage. Wir setzen das `Prädikat` und `Objekt` als Variablen ein (`?`). `SELECT` beschreibt welche Variablen zurückgegeben werden sollen und mit `DISTINCT` werden doppelte Ergebnisse aussortiert. Die Aussage endet mit einem Punkt und die Abfrage gibt alle Elemente zurück, die das definierte Pattern erfüllen. Eine ausführliche Anleitung zum Pattern Matching ist [hier](https://programminghistorian.org/en/lessons/retired/graph-databases-and-SPARQL#rdf-in-brief) zu finden. 

Das Ergebnis ist eine Tabelle mit allen Prädikaten und den entsprechenden Objekten (unsere Variabeln), die in allen abgespeicherten Triples mit der Bundesverfassung als Subjekt vorkommen. Als **Objekte** finden wir URIs (Objekte die dereferenzierbar und ihrerseits mit Prädikaten beschrieben sind) und **Literals** (Strings die eine bestimmte Information (z.B. Datum) transportieren).

Bemerkungen:
Die Bundesverfassung ist vom Typ `rdf:type` `jolux:ConsolidationAbstract` (**Objekt**), der einen SR-Eintrag (Gesetz auf abstrakter Ebene) darstellt. 
Das **Prädikat** `classifiedByTaxonomyEntry` im  [Vokabular](https://fedlex.data.admin.ch/vocabularies/de/) (Begriffsverzeichnis) der Bundeskanzlei beschreibt der SR-Eintrag. Es ist die zuverlässigste Quelle zum Abfragen der SR-Nummer eines SR-Eintrags.