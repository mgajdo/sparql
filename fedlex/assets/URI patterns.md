# URI patterns
From the `Convention`: 

## URI for classified compilation (Consolidation)
URI for a Classified compilation of a basic act published in the Official compilation
The URI is made of the URI of the basic act published in the Official compilation; the collection identifier is changed from “oc” to “cc”

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier}

Example:

When the URI of a basic act in the Official compilation is:

https://fedlex.data.admin.ch/eli/oc/2020/759

the URI of its compilation in the Classified compilation is:

https://fedlex.data.admin.ch/eli/cc/2020/759

In some cases, several Classified compilations derive from the same basic act published in the Official compilation; in these cases, the first Classified compilation mentioned in the Official compilation is considered the main act and will have an URI based on the URI of the basic act published in the Official compilation. The other Classified compilations will have the same URI followed by a sequential number.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier}“-”{order number starting at 2}

Examples:

URI of the basic act in the Official compilation:

https://fedlex.data.admin.ch/eli/oc/2004/25

URI of the first mentioned Classified compilation:

https://fedlex.data.admin.ch/eli/cc/2004/25

URI of the following Classified compilations:

https://fedlex.data.admin.ch/eli/cc/2004/25-2

URI of a Classified compilation when the basic act has been published in another collection than “Official compilation”
If the basic act of the Classified compilation has been published in another collection than the Official compilation, the collection of the basic act is indicated at the end of the URI.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{natural identifier} “_”

{collection of the basic act}

Example:

https://fedlex.data.admin.ch/eli/cc/2004/232_fga

URI of a Classified compilation when the basic act was not published
In some cases, the basic act of a Classified compilation has not been published.

Template:

https://fedlex.data.admin.ch/eli/cc/{year}/{historicaldossierID}-cc

Example:

https://fedlex.data.admin.ch/eli/cc/1929/0029_cc

URI for a Classified compilation with indication of the version
{point in time} = date of the version of the Classified compilation as YYYYMMDD.

Template:

URI of the Classified compilation/{point in time}

Example of URI for the version of a classified compilation on the 1/11/2015:

https://fedlex.data.admin.ch/eli/cc/2015/659/20151101

URIs for linguistic versions of LegalResource (Expression)
{language} = iso code (ISO-639-1) of the language: “de”, “fr”, “it”, “rm”, “en”

## The URIs of linguistic versions of a legal resource are based on a concatenation of the URI of the legal resource and the iso code of the language.

Template:

{URI of the legal resource}/{language}

Example of URI for the German version of the legal resource published in the Official compilation:

https://fedlex.data.admin.ch/eli/oc/2007/928/de
Example of URI for the German version of a Classified compilation:

https://fedlex.data.admin.ch/eli/cc/2007/928/de

## URI for a linguistic version of a legal resource in a specific file format (Manifestation)
{user-format}: code of the functional format of the file.

Format can have the following values: “html”, “pdf-x”, “pdf-a”, “pdf-a-an”, “docx”, “docx-an” where “an” stands for “anonymized version”, “x” stands for “print version” and “a” for “display version” (see the property skos:notation of the controlled vocabulary for more details https://fedlex.data.admin.ch/vocabulary/user-format).

The URI of legal resource in a specific linguistic version and a specific format is the concatenation of the URI of the linguistic version followed by the code of the format of the publication.

Template:

{work uri}/{language}/{user-format}

Example of URI for the **html** publication of the German version the basic act on legal publications:

https://fedlex.data.admin.ch/eli/oc/2007/928/de

Example of URI for the signed **pdf** of the German version of a consolidated compilation:

https://fedlex.data.admin.ch/eli/oc/2007/928/de/pdf-a

## URI for a version of a Manifestation
If there is a need to change a file described by a Manifestation, for traceability reason, the former document will be related to the Manifestation through the property `jolux#wasExemplifiedBy`, when the newest version will be related to the Manifestation through the property `jolux#isExemplifiedBy` (is vs.was).

Use cases: a new version of provisional consolidation is published. The description of the consolidation (Consolidation) and the description of the linguistic versions (Expression) and files (Manifestation) are unchanged, the former version of the provisional consolidation now related with the property jolux#wasExemplifiedBy to the Manifestation.

See an example with the Manifestation:

https://fedlex.data.admin.ch/eli/cc/27/317_321_377/20210501/fr/pdf-a

## URI for appendices, annexes or parts of a legal resource (LegalResource)
{part} = The code “app” is used for each part of the document, except the main part.

Template:

{work uri}/{part type}/{order number}

Example of URI for annex 2 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2017/663/annex/2

URI for subdivision of a legal resource (`LegalResourceSubdivision`) {subdivision type}: The subdivision types are the same as the ones used in the `xml/AkomaNtoso` document. 

See the property skos:notation of the controlled vocabulary https://fedlex.data.admin.ch/vocabulary/subdivision-type to have the codes for the subdivision types.

See also the website of the Federal Chencellery (Bundeskanzlei) with a [Documentation for the propoer publication](https://www.bk.admin.ch/bk/de/home/dokumentation/begleitende-rechtssetzung/dokumentation-rechtsetzungsbegleitung.html) of laws for useful background information.

Two types of subdivision hierarchies can be described for the same text:

1. a hierarchy of articles and sub-elements of articles,

2. a hierarchy of documents made of chapters, sections, titles…

The two hierarchies are independent from each other which allows to insert new sections in a document without impact on the identification of the articles and their sub-levels and reciprocally.

### Subdivision: articles and subdivisions of articles
Template:

{work uri}/{subdivision type}”_”{id of the subdivision}/{subdivision type}”_”{id of the subdivision}

Examples of URI for the article 1 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2021/137/art_1

### Subdivisions: chapters, titles, sections:
The code “tit” is used on each of the levels, which can be chapters, sections, titles…

Template:

{work uri}/{subdivision type}”_”{id of the level section}/{subdivision type}”_”{id of the level section}/

Example of URI for the level 1 of a legal resource:

https://fedlex.data.admin.ch/eli/oc/2021/153/lvl_I
Texts available at the national archives

For pre-1999 texts these are only available in the national archives. For the Federal gazette there is one scanned text for each legislative resource. For the Official compilation there is one scanned text for each weekly publication of the official journal. For the Official compilation the scanned version of the text has been structured as an XML document.

## URI for collections, edition, language and format

To display whole collections, we add the path `collection` inbetween `eli` and `{collection}`. After that `{year}/{edition number}` and `{language}` (optional).

Template:

https://fedlex.data.admin.ch/eli/collection/{collection}/{year}/{edition number}/{language}

Example: URI of the Official **compilation** of 2010:

https://fedlex.data.admin.ch/eli/collection/oc/2010

Example: URI of the edition of the Official compilation in week 23 from year 2010 (edition of a collection (Memorial)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23

Example: URI of the Italian edition of the official compilation in week 23 from year 2010 (linguistic version of an edition (Expression)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23/it

Example: URI of the Italian edition of the official compilation in week 23 from the year 2018 in the language Italian with the file format PDF (a specific file format (Manifestation)):

https://fedlex.data.admin.ch/eli/collection/oc/2010/23/it/pdf-a

## URI for edition of the complete legislation
Edition abstract
URI for the edition family (EditionAbstract)
https://fedlex.data.admin.ch/eli/edition/{edition type}

{edition type} : “national” or “international”

Examples :

https://fedlex.data.admin.ch/eli/edition/national
https://fedlex.data.admin.ch/eli/edition/international
Edition
## URI for the edition (Edition)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302 https://fedlex.data.admin.ch/eli/edition/international/20220302
URI for the expression of an edition (Expression)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{language}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de https://fedlex.data.admin.ch/eli/edition/international/20220302/fr
URI for the manifestation of an edition (Manifestation)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{language}/{format}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/pdf-a https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/pdf-a
Remark: indicate “pdf-a” format even if the pdf is in a zip file.

### Binder
URI for a binder in a given language (Edition)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3 https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2
URI for the expression of a binder (Expression)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}/{language}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3/de https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2/fr
URI for the manifestation of a binder (Manifestation)
https://fedlex.data.admin.ch/eli/edition/{edition type}/{point in time}/{edition language}/{binder number}/{language}/{format}

Examples :

https://fedlex.data.admin.ch/eli/edition/national/20220302/de/3/de/pdf-a https://fedlex.data.admin.ch/eli/edition/international/20220302/fr/2/fr/pdf-a
URI for the compendium (Compendium)

### Compendium is an ad-hoc compilation of legal resources.
Template:

https://fedlex.data.admin.ch/{collection}/{compendium}/{year}{serial number}

Example:

https://fedlex.data.admin.ch/fga/compendium/2021/1
URI for the linguistic version of a compendium with indication of the language (Expression)
Template:

https://fedlex.data.admin.ch/eli/compendium/{year}/{serial number}/{language}

Example of the German version of a compendium:

https://fedlex.data.admin.ch/fga/compendium/2021/1/de
URI for the linguistic version of a compendium in a specific file format (Manifestation)
Template:

https://fedlex.data.admin.ch/eli/compendium/{year}/{serial number}/{language}/{user format}

Example:

https://fedlex.data.admin.ch/fga/compendium/2021/1/de/pdf-x

## URI for legal analysis (LegalAnalysis)
The URI of the legal resource analysis is based on the URI of the legal resource which is analysed. Legal resource impact describes the legal impact of a legal resource on another legal resource (initial version or consolidated version). 

Before 1/1/2021, the legal impacts are described from text to text with a comment on the impacted articles. Since 1/1/2021, the legal impacts are described from `articles` or `titles` of legal resources to articles or titles of the impacted legal resource.

Template:

{uri the legal resource which is analysed}/legal-analysis

Example: Analysis of the legal impact of a legislation:

https://fedlex.data.admin.ch/eli/oc/2021/115/legal-analysis

AS 2021 115 Verordnung 3 über Massnahmen zur Bekämpfung des Coronavirus (Covid-19) (Covid-19-Verordnung 3) (Liste der Erkrankungen, die Personen zu besonders gefährdeten Personen machen) has one URI for legal resource impact (LegalResourceImpact): Anhang 7 der Covid-19-Verordnung 3 vom 19. Juni 2020 wird gemäss Beilage gestützt auf Artikel 27a Absatz 12 der Covid-19-Verordnung 3 geändert." 

The URI of the impact is based on the URI of the legal analysis of the legal resource:

Template:

{uri of the legal analysis of the legal resource}/LegalResourceImpact/{impact number}

Example of the URI for a legal impact of a legislation:

https://fedlex.data.admin.ch/eli/oc/2021/115/legal-analysis/LegalResourceImpact/1


## URI for citation (Citation)
Citation describes the citation from legal resource to another legal resource. Before 1/1/2021, the citations are described from text to text with a comment on the cited article. Since 1/1/2021, the citations are described from articles of legal resource to articles of the cited legal resource.

The URI of the citation is based on the URI of the version of legislation which cites.

Template:

{uri of the subdivision of the legal resource which cites}/{point in time}/citation/{citation number}

Example of the URI of a citation made from the version of the 1/1/2020 of a consolidated text:

https://fedlex.data.admin.ch/eli/cc/2002/452/text/20180701/citation/10
URI for treaty (TreatyProcess)
Starting from January 1st, 2021
Template:

https://fedlex.data.admin.ch/eli/treaty/{year}/{treaty number - 4 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/2021/0242
Before January 1st, 2021

Before 1/1/2021 the existing treaty identifiers will be reused adding a “/” before the treaty number. Identifier as 2018234 becomes 2018/0234, identifier as 99992335 will become 9999/2335.

Example 1:

https://fedlex.data.admin.ch/eli/treaty/2018/1072
Example 2:

https://fedlex.data.admin.ch/eli/treaty/9999/6088
URI of treaties considered as annexes:
Template:

{uri of the parent treaty}1{annex number - 3 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/1978/00261001
URI of treaties considered as modifications:
Template:

{uri of the parent treaty}2{modification number - 3 digits}

Example:

https://fedlex.data.admin.ch/eli/treaty/1923/00112012
URI of treaties based on European conventions:
Template:

https://fedlex.data.admin.ch/eli/treaty/1234/{convention number}

Example:

https://fedlex.data.admin.ch/eli/treaty/1234/18037
Creation of new treaties from decision of joint committee:
Template:

https://fedlex.data.admin.ch/eli/treaty/1357/{decision number}

Example:

https://fedlex.data.admin.ch/eli/treaty/1357/18424

## URI for draft legislation
### URI for Legislative Project (InitialDraft)
Legislative projects make it possible to group the various tasks and publications that mark the process of publishing a law. This type of resource does not exist today, it should be created based on the migrated publication dossiers. The linked publication dossiers will all be attached to a single legislative project. Consultations will also be related to the legislative project.

Template:

https://fedlex.data.admin.ch/eli/dl/proj/{year}/{legislative_process_identifier}

Example:

https://fedlex.data.admin.ch/eli/dl/proj/2022/15

### URI for the tasks of Legislative Project (LegislativeTask and their sub-classes)
The stage of the process that take place throughout the creation of a new law (consultation, parliament...) have the URI of the legislative project in which they register followed by a number.

{task type}: for the possible values see the property skos:notation of the vocabulary https://fedlex.data.admin.ch/vocabulary/type-projet

Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{task type}”_”{sequence of the task}

Remark: {sequence of the task} is facultative if the task opens only once.

Example for a consultation:

https://fedlex.data.admin.ch/eli/dl/proj/6020/6/cons_1
Example for the subtask of a consultation, the publication of position statements:

https://fedlex.data.admin.ch/eli/dl/proj/6020/6/cons_1/cons-open

### URI for the text of a legislative project (DraftDocument)
Uri for the abstract of the text of a legislative project (DraftDocumentAbstract).
Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{document identifier}

Example:

https://fedlex.data.admin.ch/eli/dl/proj/6020/34/cons_1/doc_1

### URI for the document related to the text of a legislative task (DraftRelatedDocument)
For the abstract of a document related to a legislative task (DraftRelatedDocumentAbstract)
Template:

{URI of the legislative project}/{task type}”_”{sequence of the task}/{document identifier}

Example of a document provided for a consultation.

https://fedlex.data.admin.ch/eli/dl/proj/6020/34/cons_1/doc_2