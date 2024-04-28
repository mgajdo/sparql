# Fedlex Tutorial

Das folgende Beispiel wurde übernommen aus: [Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/)

Siehe auch [SPARQL Playground](https://fedlex.data.admin.ch/de-CH/sparql) von Casemates mit mehr Beispielen für **Fedlex**. Mehr Tutorials zu Linked Data aus der Schweiz: auch hier: https://zazuko.com/get-started/.

## Erste Schritte

## Metadaten-Explorer

Die URI bzw. die URL der Bundesverfassung `https://fedlex.data.admin.ch/eli/cc/1999/404` verweist auf den Gesetzestext. Im [Metadaten-Explorer](https://fedlex.data.admin.ch/de-CH/metadata) kann man die damit verknüpften Linked Data Triples durchsuchen. 

Eine Abfrage der Linked Data Triples der Bundesverfassung über den Metadaten-Explorers weist stets folgende URL auf:
- die Sprache als path `/de-CH` 
- der Gesetzestext als Parameter: `/metadata?value=`

Die zusammengesetzte URL: https://fedlex.data.admin.ch/de-CH/metadata?value=https://fedlex.data.admin.ch/eli/cc/1999/404

## Fedlex SPARQL API

Die API von Fedlex ist auch über einen SPARQL Endpoint verfügbar:
- [API Endpoint](https://fedlex.data.admin.ch/sparqlendpoint)
- [Web-Interface](https://fedlex.data.admin.ch/de-CH/sparql) für Testzwecke 

Die Website https://fedlex.admin.ch und alle dort angzeigten Daten sind in Form von **Linked Data**, d.h. Triples im Datenformat RDF (Resource Description Framework) in einem Triple Store gespeichert und mit Hilfe des SPARQL Endpoints  maschinenlesbar. Im Gegensatz zu relationalen Datenbanken werden die Daten in Triple Stores als  **Triples** (daher mit Tabellen nicht visualisierbar) gespeichert. 

Eine SPARQL Abfrage ist nichts anderes als ein POST-Request an den entsprechenden Triple Store Datenbank Server. Wir benutzen dazu das Web-Interface:

**Web-Interface**: https://fedlex.data.admin.ch/sparqlendpoint)

![Virtuoso SPARQL Query Editor abrufbar unter: https://fedlex.data.admin.ch/sparqlendpoint](<Screenshot 2024-04-27 at 14.04.54.png>) (Web-Interface)

## SPARQL Patterns
SPARQL Queries folgen einem grundlegenden Aufbau, der immer gleich lautet:

```
SELECT * WHERE 
{
    ?subject ?predicate ?object.   
}
```

Triples folgen der grammatikalischen Struktur **Subjekt -> Prädikat -> Objekt**.  Einzelne Positionen der Triples können bewusst undefiniert gelassen und mit der Variable `?`bezeichnet werden. Mehr Informationen zu SPARQL:
- [SPARQL-Tutorial 1](https://jena.apache.org/tutorials/sparql.html) 
- [SPARQL Tutorial 2](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) from Wikidata

Das Ziel unserer ersten Query in der Bundesverfassung ist es Triples suchen, in denen die Bundesverfassung als **Subjekt** erscheint. Alle Triples müssen dieses Muster erfüllen:

```
SELECT DISTINCT ?Prädikat ?Objekt WHERE {
    
    <https://fedlex.data.admin.ch/eli/cc/1999/404> ?Prädikat ?Objekt .
} 
```

In SPARQL ist die `URI der Bundesverfassung` das **Subjekt** der SPARQL-Abfrage. Wir setzen das `Prädikat` und `Objekt` als Variablen ein (`?`). `SELECT` beschreibt welche Variablen zurückgegeben werden sollen und mit `DISTINCT` werden doppelte Ergebnisse aussortiert. Die Aussage endet mit einem Punkt und die Abfrage gibt alle Elemente zurück, die das definierte Pattern erfüllen. 

Eine ausführliche Anleitung zum Pattern Matching ist [hier](https://programminghistorian.org/en/lessons/retired/graph-databases-and-SPARQL#rdf-in-brief) zu finden. 

Das Ergebnis ist eine Tabelle mit allen Prädikaten und den entsprechenden Objekten (unsere Variabeln), die in allen abgespeicherten Triples mit der Bundesverfassung als Subjekt vorkommen.

![alt text](<Screenshot 2024-04-27 at 14.17.45.png>)

Die Bundesverfassung ist vom Typ `rdf:type` `jolux:ConsolidationAbstract` (**Objekt**), der einen SR-Eintrag (Gesetz auf abstrakter Ebene) darstellt. 

Als **Objekte** sehen wir URIs (Objekte die dereferenzierbar und ihrerseits mit Prädikaten beschrieben sind) und **Literals** (Strings die eine bestimmte Information (z.B. Datum) transportieren).

Das **Prädikat** `classifiedByTaxonomyEntry` im  [Vokabular](https://fedlex.data.admin.ch/vocabularies/de/) (Begriffsverzeichnis) der Bundeskanzlei beschreibt der SR-Eintrag. Es ist die zuverlässigste Quelle zum Abfragen der SR-Nummer eines SR-Eintrags.

## Der Fedlex Namespace

Die URIs von Fedlex werden nach einer `Convention` beschrieben: 

[URIs Templates for Legal Resources in Switzerland](https://fedlex.data.admin.ch/de-CH/home/convention)

"Switzerland publishes several collections of legal resources available in German, French and Italian and in some cases translated to Romanish or English. Most of the information published are documents, but some are just information about a legislative event, such as the starting date of a consultation published in the Federal gazette, or information about consultation events. 

Alle URIs des `fedlex` Namespace (u.a. für AS und SR Einträge) beginnen mit `https://fedlex.data.admin.ch/eli/`.

Beispiele:
- Die Einträge für die AS beginnen mit https://fedlex.data.admin.ch/eli/oc/ 
- Die Einträge für die SR beginnen mit https://fedlex.data.admin.ch/eli/cc/

Die URIs von Fedlex richten sich nach dem europäischen ELI-Standard (European Legislation Identifier) zur Bezwichnung von Rechtstexten. The [European Legislation Identifier (ELI)](https://eur-lex.europa.eu/eli-register/about.html) is a system to make legislation available online in a standardised format, so that it can be accessed, exchanged and reused across borders.

### Datenmodell

Das von Fedlex verwendete Datenmodell heisst [JOLux](https://fedlex.data.admin.ch/de-CH/home/models). `jolux` ist ein eigener Namespace für das JOLux Datenmodell basierend auf dem [FRBR-Standard](https://de.wikipedia.org/wiki/Functional_Requirements_for_Bibliographic_Records) (Functional Requirements for Bibliographic Records), einem Entity-Relationship-Modell zur Beschreibung bibliographischer Daten, das für die Beschreibung von Rechtstexten adaptiert wurde. Ursprünglich aus Luxemburg stammend wird das Datenmodell inzwischen von der Schweiz und Luxemburg gemeinsam weiterentwickelt.

[Download Jolux Ontology](https://fedlex.data.admin.ch/filestore/resources/jolux_ontology.zip) (.zip file)

Andere wichtige Namespaces, die mit Jolux verknüpft sind:
* `skos` : [SKOS Vokabular](http://www.w3.org/2004/02/skos/core#)
* `rdf` : [RDF Vokabular](http://www.w3.org/1999/02/22-rdf-syntax-ns#)

### Metadaten (Sprachversionen)

Die URL in der SPRQL-Abfrage (`https://fedlex.data.admin.ch/eli/cc/1999/404`) führt im Broswer zum Gesetzestext der Bundesverfassung in der Systematischen Rechtssammlung. (Der Path `/cc` steht für Classified Compilation). Die URI der deutschen Sprachversion `https://fedlex.data.admin.ch/eli/cc/1999/404/de` hingegen beschreibt nicht etwa den deutschen Text der eigentlichen Bundesverfassung sondern repräsentiert nur die "Kopfdaten", also Titel und Abkürzung auf Deutsch. (Die Metadaten lassen sich im Metadaten-Explorer anzeigen). 

Im Datenmodell von JoLux existieren innerhalb eines `jolux:ConsolidationAbstract` verschiedene **Sprachversionen**. Diese sind vom `rdf:type` `jolux:Expression` und sind durch die Eigenschaft `jolux:isRealizedBy` mit dem sprachübergreifenden Eintrag des `jolux:ConsolidationAbstract` verknüpft. 

Der eigentliche Inhalt der Gesetzestexte ist über die "Consolidations-Versionen" der SR Einträge angebunden.

### Publikationsarten

Gemäss `Convention` ([URIs Templates for Legal Resources in Switzerland](https://fedlex.data.admin.ch/de-CH/home/convention)) gibt es die untenstehenden Publikationsarten. Diese sollten dem Bundesgesetz über die Sammlungen des Bundesrechts und das Bundesblatt [(Publikationsgesetz, PublG)](https://www.fedlex.admin.ch/eli/cc/2004/745/de) entsprechen. 

Template:

https://fedlex.data.admin.ch/eli/{collection}

Possible values for `{collection}`:

* `fga` for the Federal gazette
* `oc` for the Official compilation
* `cc` for the Classified compilation
* `cons` for the publication of consultation procedures
* `treaty` for the publication of international treaties
* `fgae` for documents published as “reference” in texts published in the fga
* `oce` for documents published as “reference” in texts published in the oc
* `cce` for documents published as "reference” in texts published in the cc
* `oe` for reports about ordonnances
* `mog` for documents published in the Militäramtsblatt (MA) / Feuille officielle militaire (FOM) / Foglio ufficiale militare (FUM)
* `ogc` for documents published in the Swiss Official Gazette of Commerce (SOGC)
* `oldcc` for documents published in the Revised Compilation of Federal Acts and Ordinances 1848-1947 (BS)
* `ob` for documents published in the Official Bulletin of the Federal Assembly
* `cmog` for documents published in the Sammelband des Militäramtsblattes (SMA) / Recueil de la Feuille officielle militaire (RFM) / Raccolta del Foglio ufficiale militare (RFM)

### Texte der Amtlichen Sammlung

{collection} = oc

Template:

https://fedlex.data.admin.ch/eli/oc/{year}/{natural identifier}


Example:

https://fedlex.data.admin.ch/eli/oc/2020/759

Der {natural identifier} in diesem Fall ist die chronologisch fortlaufende Nummer des Erlasses in der AS. Für Texte vor 2000 ist das {volume} optional wie in diesem Fall. Die Verordnung über die Massnahmen im Kulturbereich gemäss Covid-19-Gesetz (Covid-19-Kulturverordnung) erschien in Band 127 der AS (Amtliche Sammlung > Ausgaben der AS > 2020 > Oktober > **127** > AS 2020 4147)

#### Vor 1999
Bei älteren Erlassen (vor 1999) ist der {natural identifier} zusammengesetzt aus {volume} und {page}. Aufgrund mehrerer Sprachversionen ist der {natural identifier} Kombination `{year}/{volume}”_”{page-de}”_”{page-fr}”_”{page-it}`.

Template:
```
https://fedlex.data.admin.ch/eli/{collection}/{year}/{volume}”_”{page-de}”_”{page-fr}”_”{page-it}
```

Example:

https://fedlex.data.admin.ch/eli/fga/1994/2_1_1_1

Die Endung `2_1_1_1` deutet auf "aligned language versions" für den Eintrag BBl 1994 II S. 1 hin.

Wenn 2_1_1_1 nicht "aligned" wäre, ergibt dich die Seitennummer aus der Scanreihenfolge durch das Schweizerische Bundesarchiv (gescannte Dokumentversion). Es wird dabei nur die vorliegende Sprachversion indiziert

BBl 1994 I 569, Jahresbericht des Bundesrates über die Tätigkeiten der Schweiz im Europarat 1993 vom 19. Januar 1994:

https://fedlex.data.admin.ch/eli/fga/1994/1_569__

BBl vom 3.Oktober 1940, S. 1083 (auf Französisch):

https://fedlex.data.admin.ch/eli/fga/1940/1__1083_

Remark: the language of the text is indicated in the metadata jolux:langage in the related Expression.


#### For all texts of oc between 1948 and 1999

Template:

https://fedlex.data.admin.ch/eli/oc/{year}/{page-de}”_”{page-fr}”_”{page-it}

Example: AS 1996 1506, Verordnung vom 22. Mai 1996 über Finanzhilfen nach dem Gleichstellungsgesetz

https://fedlex.data.admin.ch/eli/oc/1996/1506_1506_1506

Die Texte sind verfügbar auf der [Webseite des Schweizerischen Bundesarchivs](https://www.amtsdruckschriften.bar.admin.ch/setLanguage.do?lang=DE&currWebPage=searchHome).

#### For all texts of oc between 1848 and 1947

Template:

https://fedlex.data.admin.ch/eli/{collection}/{volume-number}”_”{page-de}”_”{page-fr}”_”{page-it}

Examples:
https://fedlex.data.admin.ch/eli/oc/VII/342_337_325 (From 1848 to 1874 the volume is indicated with Roman numbers)
https://fedlex.data.admin.ch/eli/oc/III/183_182_182 (From 1874 to 1947 the volume is indicated with Arabic numbers)

### URIs für legal resources des Bundesblatts (fga)

{collection} = fga

#### For all texts since 2000
Template:
```
https://fedlex.data.admin.ch/eli/fga/{year}/{natural identifier}
```

Example :

https://fedlex.data.admin.ch/eli/fga/2020/1

#### For all texts before 2000
See oc.

### Other Link patterns
Other link patterns are in the URI template

## Fedlex Vokabular

Das Fedlex Vokabular auf Deutsch ist unter https://fedlex.data.admin.ch/vocabularies/de/

Alle URIs des kontrollierten Vokabulars sind unter dem Pfad `/vocabulary` gebildet. 

Template:

https://fedlex.data.admin.ch/vocabulary/{vocabulary-name}


#### URI of the controlled vocabulary which describes legal institutions

https://fedlex.data.admin.ch/vocabulary/legal-institution

URI for a all legal institutions in the vocabulary of legal institutions.

#### URI for a concept of a vocabulary

https://fedlex.data.admin.ch/vocabulary/legal-institution/D19

URI for a concept **(skos:Concept)** in the vocabulary of legal institutions, the Swiss national bank (Bundesnahe Betriebe > Schweizerische Nationalbank): 

Template:
https://fedlex.data.admin.ch/vocabulary/{vocabulary-name}/{concept}
