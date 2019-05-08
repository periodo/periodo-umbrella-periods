from rdflib import Namespace, URIRef
from rdflib.namespace import SKOS

AS = Namespace('https://www.w3.org/ns/activitystreams#')
BASE = Namespace('http://n2t.net/ark:/99152/')
BIBO = Namespace('http://purl.org/ontology/bibo/')
LEXVO = Namespace('http://lexvo.org/ontology#')
PERIODO = Namespace('http://n2t.net/ark:/99152/p0v#')
PROV = Namespace('http://www.w3.org/ns/prov#')
TIME = Namespace('http://www.w3.org/2006/time#')

AUTHORITY = URIRef(SKOS['ConceptScheme'])
COMMENT = URIRef(AS['Note'])
PERIOD = URIRef(SKOS['Concept'])

CONTEXT_LD = {
    "@base": "http://n2t.net/ark:/99152/",
    "Authority": "skos:ConceptScheme",
    "Comment": "as:Note",
    "Period": "skos:Concept",
    "abstract": "dcterms:abstract",
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "all": {
      "@id": "as:items",
      "@type": "@id"
    },
    "as": "https://www.w3.org/ns/activitystreams#",
    "author": {
      "@id": "as:attributedTo",
      "@type": "@id"
    },
    "authorities": {
      "@container": "@index",
      "@id": "rdfs:member"
    },
    "authority": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "bibo": "http://purl.org/ontology/bibo/",
    "broader": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "by": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "changes": {
      "@id": "dcterms:provenance",
      "@type": "@id"
    },
    "comments": {
      "@id": "as:replies",
      "@type": "@id"
    },
    "contributors": {
      "@container": "@set",
      "@id": "dcterms:contributor"
    },
    "count": {
      "@id": "as:totalItems",
      "@type": "xsd:nonNegativeInteger"
    },
    "creator": {
      "@id": "dcterms:creator",
      "@type": "@id"
    },
    "creators": {
      "@container": "@set",
      "@id": "dcterms:creator"
    },
    "dateAccessed": {
      "@id": "dcterms:date",
      "@type": "xsd:date"
    },
    "dcelements": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "earliestYear": {
      "@id": "periodo:earliestYear",
      "@type": "xsd:gYear"
    },
    "editorialNote": "skos:editorialNote",
    "first": {
      "@id": "as:first",
      "@type": "@id"
    },
    "foaf": "http://xmlns.com/foaf/0.1/",
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "history": "@graph",
    "id": "@id",
    "in": "time:hasDateTimeDescription",
    "inDataset": {
      "@id": "void:inDataset",
      "@type": "@id"
    },
    "initialDataLoad": {
      "@id": "rdf:first",
      "@type": "@id"
    },
    "items": {
      "@container": "@index",
      "@id": "rdfs:member"
    },
    "label": "skos:prefLabel",
    "language": {
      "@id": "dcterms:language",
      "@type": "@id"
    },
    "languageTag": "dcelements:language",
    "last": {
      "@id": "as:last",
      "@type": "@id"
    },
    "latestYear": {
      "@id": "periodo:latestYear",
      "@type": "xsd:gYear"
    },
    "lexvo": "http://lexvo.org/ontology#",
    "localizedLabels": {
      "@container": "@language",
      "@id": "skos:altLabel"
    },
    "locator": "bibo:locator",
    "mediaType": "as:mediaType",
    "mergedAt": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "mergedPatches": {
      "@id": "rdf:rest"
    },
    "message": "as:content",
    "name": "foaf:name",
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "note": "skos:note",
    "owl": "http://www.w3.org/2002/07/owl#",
    "partOf": {
      "@id": "dcterms:isPartOf",
      "@type": "@id"
    },
    "periodo": "http://n2t.net/ark:/99152/p0v#",
    "periods": {
      "@container": "@index",
      "@reverse": "skos:inScheme"
    },
    "postedAt": {
      "@id": "as:published",
      "@type": "xsd:dateTime"
    },
    "primaryTopicOf": {
      "@id": "foaf:isPrimaryTopicOf",
      "@type": "@id"
    },
    "prov": "http://www.w3.org/ns/prov#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "role": {
      "@id": "prov:hadRole",
      "@type": "@id"
    },
    "roles": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "sameAs": {
      "@id": "owl:sameAs",
      "@type": "@id"
    },
    "script": {
      "@id": "lexvo:inScript",
      "@type": "@id"
    },
    "seeAlso": {
      "@id": "rdfs:seeAlso",
      "@type": "@id"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "source": "dcterms:source",
    "spatialCoverage": {
      "@container": "@set",
      "@id": "dcterms:spatial"
    },
    "spatialCoverageDescription": "periodo:spatialCoverageDescription",
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "start": "time:intervalStartedBy",
    "stop": "time:intervalFinishedBy",
    "submittedAt": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "time": "http://www.w3.org/2006/time#",
    "title": "dcterms:title",
    "type": "@type",
    "url": {
      "@id": "foaf:page",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "void": "http://rdfs.org/ns/void#",
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "year": {
      "@id": "time:year",
      "@type": "xsd:gYear"
    },
    "yearPublished": {
      "@id": "dcterms:issued",
      "@type": "xsd:gYear"
    }
}

