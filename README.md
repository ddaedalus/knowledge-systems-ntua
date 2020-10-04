## Knowledge Systems NTUA Project
In this project a Semantic Web Database is developed in Protégé and some SPARQL queries are executed in Virtuoso.   
Techologies used: OWL, RDF, SPARQL.  
   
## Ontology
This was implemented in Protégé, which create ontologies in .owl file extension. An ontology is a vocabulary defining the concepts and relationships used to describe an area of concern. Here, we describe Athens Transport Network ([oasa](http://geodata.gov.gr/el/dataset/oasa)). It's composed of:

- Classes (e.g. Bus, Trip etc) to represent a concept.
- Data Properties (e.g. hasTrip) to represent relation between concepts.
- Object Properties - Rules (e.g. hasStopTime).   

Ontologies can be created for every area of concern and by everyone using RDF (Resource Description Framework), RDFS (RDF Schema) and OWL (Web Ontology Language).  

## RDF
We use the Turtle format to write down the RDF graphs. Terse RDF Triple Language (Turtle) is a syntax and file format for expressing data in the Resource Description Framework (RDF) data model. Turtle syntax is similar to that of SPARQL, an RDF query language. It is a common data format for storing RDF data, along with N-Triples, JSON-LD and RDF/XML.  

## SPARQL 
We write down our queries in Virtuoso using SPARQL. SPARQL is an RDF query language—that is, a semantic query language for databases—able to retrieve and manipulate data stored in Resource Description Framework (RDF) format.
