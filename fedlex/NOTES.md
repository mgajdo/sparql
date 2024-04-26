# SPARQL Abfragen auf Fedlex

[## Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/)


## Fedlex URIs

### URIs und Vokabular

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

#### Amtliche Sammlung

In der **Amtlichen Sammlung (AS)** (Englisch: Official Compilation (OC)) des Bundesrechts werden die neuen und geänderten Erlasse, Verträge und Beschlüsse chronologisch veröffentlicht. 

Typischerweise haben Beschlüsse die Form eines Mantelerlasses, in denen sowohl neue Gesetze erlassen werden, als auch schon bestehende geändert oder aufgehoben werden können. 

Jede Veröffentlichung in der amtlichen Sammlung erhält eine eindeutige AS-Nummer (z.B. [AS 2021 654](https://www.fedlex.admin.ch/eli/oc/2021/654)). 

Weitere Erläuterungen zur amtlichen Sammlung sind [hier](https://www.fedlex.admin.ch/de/oc/explanations-oc) zu finden.

#### Systematische Rechtssammlung

Die **Systematische Rechtssammlung (SR)** (Englisch: Consolidated Compilation (CC)) des Bundesrechts stellt die konsolidierte Fassung des aktuell gültigen Rechts basierend auf der amtlichen Sammlung dar. 

Jeder Gesetzestext bekommt eine SR-Nummer (z.B. [SR 101](https://www.fedlex.admin.ch/eli/cc/1999/404) für die Bundesverfassung), welche sich nicht auf eine bestimmte Version eines Gesetzes bezieht, sondern auf das Gesetz im Allgemeinen. 

Erscheint ein neuer Erlass in der AS der Teile des entsprechenden Gesetzes revidiert (z.B. Teile der Bundesverfassung durch [AS 2022 241](https://www.fedlex.admin.ch/eli/oc/2022/241)), so werden diese Änderungen in der systematischen Rechtssammlung konsolidiert und unter gleichbleibender SR-Nummer veröffentlicht (im Beispiel weiterhin SR 101). 

Eine SR-Nummer ist innerhalb des geltenden Rechts eindeutig. In Fällen in denen ein Gesetz im gesamten aufgehoben und von einem neuen Gesetz abgelöst wird (z.B. bei einer Totalrevision), kann es vorkommen, dass die SR-Nummer vom Vorgängegesetz übernommen wird. So teilt sich beispielsweise die geltende Bundesverfassung, als Ergebnis der Totalrevision von [1999](https://www.fedlex.admin.ch/eli/cc/1999/404), die SR-Nummer 101 mit ihrer Vorgängerversion von [1878](https://www.fedlex.admin.ch/eli/cc/1/1_1_1). 

Weitere Erläuterungen zur systematischen Rechtssammlung sind [hier](https://www.fedlex.admin.ch/de/cc/explanations-cc) zu finden.

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

Die Aussage beginnt mit der `URI der Bundesverfassung` als Subjekt. Wir setzen das `Prädikat` und `Objekt` als Variablen ein (`?`). `SELECT` beschreibt welche Variablen zurückgegeben werden sollen. Mit `DISTINCT` werden doppelte Ergebnisse aussortiert. Die Aussage endet mit einem Punkt und die Abfrage gibt alle Elemente zurück, die das definierte Pattern erfüllen. Eine ausführliche Anleitung zum Pattern Matching ist [hier](https://programminghistorian.org/en/lessons/retired/graph-databases-and-SPARQL#rdf-in-brief) zu finden. 

Das Ergebnis ist eine Tabelle mit allen Prädikaten und den entsprechenden Objekten (unsere Variabeln), die in allen abgespeicherten Triples mit der Bundesverfassung als Subjekt vorkommen:

[**Hier Klicken für Darstellung**](https://fedlex.data.admin.ch/sparqlendpoint?default-graph-uri=&query=SELECT+DISTINCT+%3FPr%C3%A4dikat+%3FObjekt+WHERE+%7B%0D%0A++++%0D%0A++++%3Chttps%3A%2F%2Ffedlex.data.admin.ch%2Feli%2Fcc%2F1999%2F404%3E+%3FPr%C3%A4dikat+%3FObjekt+.%0D%0A%7D+&format=text%2Fhtml&timeout=0&signal_void=on&signal_unconnected=on&run=+Run+Query+)

Als **Objekte** finden wir URIs (Objekte die dereferenzierbar und ihrerseits mit Prädikaten beschrieben sind) und **Literals** (Strings die eine bestimmte Information (z.B. Datum) transportieren). Beispielsweise sieht man hier:
- In der Spalte **Objekt**: Die Bundesverfassung ist vom Typ `rdf:type` `jolux:ConsolidationAbstract`, der einen SR-Eintrag (Gesetz auf abstrakter Ebene) darstellt. 
- Das **Prädikat** `classifiedByTaxonomyEntry` im  [Vokabular](https://fedlex.data.admin.ch/vocabularies/de/) (Begriffsverzeichnis) der Bundeskanzlei beschreibt der SR-Eintrag. Es ist die zuverlässigste Quelle zum Abfragen der SR-Nummer eines SR-Eintrags, denn jeder SR-Eintrag (inikl. Bundesverfassung) hat 

Innerhalb eines `jolux:ConsolidationAbstract` existieren verschiedene Sprachversionen. Diese sind vom `rdf:type` `jolux:Expression` und sind durch die Eigenschaft `jolux:isRealizedBy` mit dem sprachübergreifenden Eintrag des `jolux:ConsolidationAbstract` verknüpft.

Mit einem Klick auf die URI der deutschen Sprachversion https://fedlex.data.admin.ch/eli/cc/1999/404/de sehen wir, dass wir hier sowohl den Titel als auch die Abkürzung auf deutsch finden. Diese URI beschreibt nicht den deutschen Text der eigentlichen Bundesverfassung sondern repräsentiert nur die "Kopfdaten" der Bundesverfassung, also Titel und Abkürzung. 

Der eigentliche Inhalt ist über die "Consolidations-Versionen-der-SR-Einträge" angebunden.

#### Abfrage von SR-Nummer, Titel und Abkürzung der Bundesverfassung

Ausgehend von der URI der Bundesverfassung sowie dem Wissen über TaxonomyEntries und Expressions können wir nun die Information über SR-Nummer, Titel und Abkürzung der Bundesverfassung abfragen.

```
df = await query("""

# 0
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?SR_Nummer ?Titel ?Abkürzung WHERE {
    
    # 1
    <https://fedlex.data.admin.ch/eli/cc/1999/404> jolux:classifiedByTaxonomyEntry ?TaxonomyEntry .

    # 2 
    ?TaxonomyEntry skos:notation ?SR_Nummer .
    
    # 3
    <https://fedlex.data.admin.ch/eli/cc/1999/404> jolux:isRealizedBy ?Expression .
    
    # 4
    ?Expression jolux:language <http://publications.europa.eu/resource/authority/language/DEU> .
    
    # 5
    ?Expression jolux:title ?Titel ;
                jolux:titleShort ?Abkürzung .
} 

""", "F")

display_result(df)
```
0. Definition der Prefixes zur besseren Lesbarkeit
1. Die erste Aussage wählt den TaxonomyEntry der Bundesverfassung aus.
2. Vom TaxonomyEntry bekommen wir die SR-Nummer
3. Als nächstes wählen wir alle Expressions (Sprachversionen) aus die durch jolux:isRealizedBy mit der Bundesverfassung verknüpft sind.
4. Dann grenzen wir die Expressions auf diejenige mit der Sprache Deutsch ein.
5. Die nächsten Aussagen fragen die gewünschen Daten ab, jeweils mit der Expression als Subjekt (möglich durch das Beenden der Aussage mit ; anstatt .)

#### Liste aller SR-Einträge

Basierend auf dem was wir bereits gelernt haben können wir nun ganz einfach eine Liste aller SR-Einträge und die dazugehörigen Metadaten abfragen, indem wir die URI der Bundesverfassung durch eine Variable ersetzen die vom rdf:type jolux:ConsolidationAbstract sein soll (also einen SR Eintrag darstellt):

```
df = await query("""

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?SR_Nummer ?Titel ?Abkürzung ?SR_URI WHERE {
    
    # 1
    ?SR_URI rdf:type jolux:ConsolidationAbstract .
    
    # 2
    ?SR_URI jolux:classifiedByTaxonomyEntry ?TaxonomyEntry ;
            jolux:isRealizedBy ?Expression .
    
    ?TaxonomyEntry skos:notation ?SR_Nummer .
    
    ?Expression jolux:language <http://publications.europa.eu/resource/authority/language/DEU> .
    
    ?Expression jolux:title ?Titel ;
                jolux:titleShort ?Abkürzung .
} 

# 3
LIMIT 10

""", "F")

display_result(df)
```

1. Alle Objekte vom Typ ConsolidationAbstract auswählen
2. Alle TaxonomyEntries und Expressions der SR-Einträge auswählen
3. Wir beschränken die Ausgabe auf die ersten 10 Einträge

#### Durchsuchen der SR-Einträge nach Abkürzung

Falls nach SR-Einträgen mit einer bestimmten Abkürzung gesucht werden soll, ist das mit einer kleinen Anpassung der vorherigen Abfrage möglich. Dazu muss lediglich die Variable `?Abkürzung` durch den gesuchten Wert (z.B. "BankV" für die Bankenverordnung) ersetzt werden. Da der gesuchte Wert ein Literal ist, muss er in Anführungszeichen gesetzt werden:

```
df = await query("""

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?SR_Nummer ?Titel ?Abkürzung ?SR_URI WHERE {
    
    # 1
    ?SR_URI rdf:type jolux:ConsolidationAbstract .
    
    # 2
    ?SR_URI jolux:classifiedByTaxonomyEntry ?TaxonomyEntry ;
            jolux:isRealizedBy ?Expression .
    
    ?TaxonomyEntry skos:notation ?SR_Nummer .
    
    ?Expression jolux:language <http://publications.europa.eu/resource/authority/language/DEU> .
    
    ?Expression jolux:title ?Titel ;
                jolux:titleShort "BankV" .
} 

# Wir beschränken die Ausgabe auf die ersten 10 Einträge
LIMIT 10

""", "F")

display_result(df)
```

1. Alle Objekte vom Typ ConsolidationAbstract auswählen
2. Alle TaxonomyEntries und Expressions der SR-Einträge auswählen

Die Suche nach "BankV" ergibt zwei Gesetze die sich sowohl die Abkürzung, als auch die SR-Nummer teilen. In diesem Fall wurde die Bankenverordung 2014 einer Totalrevision unterzogen. Im Gegensatz zur Änderung einzelner Abschnitte, hat hier also ein neues Gesetz das gesamte alte Gesetz von 1972 abgelöst.

#### Filtern nach geltendem Recht

In der vorherigen Abfrage haben wir gesehen, dass die Datenbank sowohl geltendes Recht, als auch aufgehobenes Recht beinhaltet. Das Datum des erstmaligen Inkraftretens ist mit `jolux:dateEntryInForce` mit dem SR-Eintrag verknüpft. Einträge die nicht mehr in Kraft sind, haben ein zusätzliches Attribut `jolux:dateNoLongerInForce`, das das Datum der Aufhebung des Gesetzes beschreibt.

Wollen wir unsere Abfrage der SR-Einträge auf das aktuell geltende Recht beschränken, können wir die Ergebnisse entsprechend filtern:

```
df = await query("""

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?SR_Nummer ?Titel ?Abkürzung ?SR_URI WHERE {
    
    ?SR_URI rdf:type jolux:ConsolidationAbstract .
    
    # 1
    ?SR_URI jolux:dateEntryInForce ?datumInKraft .

    # 2
    FILTER( ( xsd:date(?datumInKraft) <= xsd:date(now()) ) )
    
    # 3
    OPTIONAL { ?SR_URI jolux:dateNoLongerInForce ?datumAufhebung . }

    # 4
    FILTER( !bound(?datumAufhebung) || xsd:date(?datumAufhebung) >= xsd:date(now()) )
    
    ?SR_URI jolux:classifiedByTaxonomyEntry ?TaxonomyEntry ;
            jolux:isRealizedBy ?Expression .
    
    ?TaxonomyEntry skos:notation ?SR_Nummer .
    
    ?Expression jolux:language <http://publications.europa.eu/resource/authority/language/DEU> .
    
    ?Expression jolux:title ?Titel ;
                jolux:titleShort ?Abkürzung .
} 

# 5
ORDER BY ASC(?datumInKraft)

LIMIT 10

""", "F")

display_result(df)
```
1. Auswählen des Datums des Inkrafttretens
2. Auswählen der SR-Einträge die vor dem heutigen Datum in Kraft getreten sind
3. Auswählen des Aufhebungsdatums, falls vorhanden
4. Auswälen der SR-Einträge die entweder kein Aufhebungsdatum haben, oder bei denen es noch in der Zukunft liegt
5. Wir sortieren die Einträge nach Datum des Inkrafttretens in aufsteigender Reihenfolge (älteste zuerst)
