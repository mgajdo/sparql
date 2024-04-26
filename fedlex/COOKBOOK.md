
[Zurück zu SPARQL Einführung](README.md)

[Zurück zu Fedlex Einführung](fedlex/README.md)

Übernommen aus: [Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/)

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
