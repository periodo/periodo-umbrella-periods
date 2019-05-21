def describe_skolem(skolem):
    """
    https://github.com/RDFLib/rdflib/issues/813
    :param skolem:
    :return:
    """
    return """
    CONSTRUCT {{ 
        ?s ?p ?o 
    }}
    WHERE {{ 
        ?s ?p ?o 
        FILTER (?s = <{s}>)
    }}
    """.format(s=skolem)


def insert_spatial_descriptions(skolem, derived_from):

    return """
    INSERT {{
        <{skolem}> dcterms:spatial ?where
    }}
    WHERE {{
        ?subject dcterms:spatial ?where
        FILTER( ?subject IN( <{filters}> ) )
    }}
    """.format(
        skolem=skolem,
        filters=">, <".join(derived_from)
    )


def insert_derived_from(skolem, derived_from):

    return """
    INSERT DATA {{
        <{skolem}> periodo:derivedFrom <{filters}>
    }}
    """.format(
        skolem=skolem,
        filters=">, <".join(derived_from)
    )


def insert_time_interval_bounds(skolem, derived_from):
    """
    Returns a prepared SPARQL INSERT statement that attaches maximum and minimum for a given PeriodCollection.
    :skolem:
    ::
    :returns: rdflib.plugins.sparql.preparedQuery object
    """

    return """
    INSERT {{
        <{skolem}> time:intervalStartedBy [
            time:hasDateTimeDescription [
                time:year ?minYear
            ]
        ] .
        <{skolem}> time:intervalFinishedBy [
            time:hasDateTimeDescription [
                time:year ?maxYear
            ]
        ] .
    }}
    WHERE {{
        SELECT (MIN(?startYear) AS ?minYear) (MAX(?endYear) AS ?maxYear)
        WHERE {{
            ?subject a skos:Concept ;
                time:intervalStartBy [
                    time:hasDateTimeDescription [
                        time:year ?startYear
                    ] 
                ];
                time:intervalFinishedBy [
                    time:hasDateTimeDescription [
                       time:year ?maxYear
                    ]
                ] .
            FILTER( ?subject IN( <{filters}> ) )
        }}
    }}
    """.format(

        filters=">, <".join(derived_from),
        skolem=skolem

    )
