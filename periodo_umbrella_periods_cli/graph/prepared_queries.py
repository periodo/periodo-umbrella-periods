from rdflib import URIRef
from rdflib.namespace import SKOS
from rdflib.plugins.sparql import prepareQuery
from .sparql import *


def get_check_for_iri_query(iri):
    """
    Returns a prepared SPARQL ASK statement that checks whether the given IRI is of rdf:type skos:Concept
    :returns: rdflib.plugins.sparql.preparedQuery object
    """

    return prepareQuery(

        "ASK {{ {0} a skos:Concept .}}".format(URIRef(iri).n3()),
        initNs={'skos': SKOS}
    )


def get_concept_iris_query():
    """
    Returns a prepared SPARQL SELECT statement that returns subjects IRIs that are of rdf:type skos:Concept.
    :returns: rdflib.plugins.sparql.preparedQuery object
    """

    return prepareQuery(

        "SELECT ?uri WHERE {{ {0} }}".format(
            "?uri a skos:Concept"
        ),
        initNs={'skos': SKOS}

    )


def get_iris_of_type_dc_spatial():
    """
    Returns a prepared SPARQL SELECT statement that returns the subjects IRIs that are of rdf:type dc:spatial.
    :returns: rdflib.plugins.sparql.preparedQuery object

    TODO: WIP - Check this query structure against the Periodo dataset to make sure everything is in the right place.
    """

    return prepareQuery(

        "SELECT ?uri WHERE {{ {0} }}".format(
            "?uri a dcterms:spatial"
        ),
        initNs={'skos': SKOS}

    )


def get_maximum_finishing_interval_query(filters=""):
    """
    Returns a prepared SPARQL SELECT statement that returns the maximum value from the set of all object literals
    with a predicate of time:intervalFinishedBy.
    :returns: rdflib.plugins.sparql.preparedQuery object
    """

    return prepareQuery(

        "SELECT {m} WHERE {{ {w} {f} }}".format(

            m=max_sparql('year'),
            w='?x time:intervalFinishedBy [ time:hasDateTimeDescription [ time:year ?year ] ] .',
            f=filters

        ),
        initNs={'time': URIRef('http://www.w3.org/2006/time#')}

    )


def get_minimum_starting_interval_query(filters=""):
    """
    Returns a prepared SPARQL SELECT statement that returns the minimum value from the set of all object literals
    with a predicate of time:intervalStartedBy.
    :returns: rdflib.plugins.sparql.preparedQuery object
    """

    return prepareQuery(

        "SELECT {m} WHERE {{ {w} {f} }}".format(

            m=min_sparql('year'),
            w='?x time:intervalStartedBy [ time:hasDateTimeDescription [ time:year ?year ] ] .',
            f=filters

        ),
        initNs={'time': URIRef('http://www.w3.org/2006/time#')}
    )


def get_create_new_period_collection_query(skolem, iris):
    """
    Returns a prepared SPARQL CONSTRUCT statement that returns a graph containing new Period Collection.
    :returns: rdflib.plugins.sparql.preparedQuery object
    """
    return prepareQuery(

        """
        CONSTRUCT {
            <{iri}> a skos:Concept ;
            periodo:spatialCoverageDescription ?spatialDescription ;
            derivedFrom ?cList ;
            time:intervalStartedBy [ 
                time:hasDateTimeDescription [ 
                    time:year ?startYear 
                ] 
            ] ;
            time:intervalFinishedBy [
                time:hasDateTimeDescription [
                    time:year ?endYear
                ] 
            ] .
                
        } 
        WHERE {
            {
                SELECT DISTINCT (MIN(?startYear) AS ?minYear) (MAX(?endYear) AS ?maxYear)
                WHERE {
                    ?subject a skos:Concept ;
                    time:intervalStartedBy [ 
                        time:hasDateTimeDescription [ 
                            time:year ?startYear 
                        ] 
                    ] ;
                    time:intervalFinishedBy [
                        time:hasDateTimeDescription [
                            time:year ?endYear
                        ] 
                    ] .
                }
                FILTER( ?subject IN( <{filters}> ) )
            }
            ?subject dcterms:spatial ?scList .
            FILTER( ?subject IN( <{filters}> ) )
        
        }
        """.format(

            iri=skolem,
            filters=">, <".join(iris)

        ),
        initNs={

            'dcterms': URIRef('http://purl.org/dc/terms/'),
            'skos': URIRef('http://www.w3.org/2004/02/skos/core#'),
            'time': URIRef('http://www.w3.org/2006/time#')
        }
    )
