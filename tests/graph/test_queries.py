from unittest import TestCase
from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import RDF, SKOS
from rdflib.plugins.sparql import prepareQuery
from periodo_umbrella_periods_cli.graph.prepared_queries import *


class TestSPARQLQueries(TestCase):

    def test_check_for_iri_exists(self):

        graph = Graph()
        graph.add((
           URIRef('http://example.com'), RDF['type'], SKOS['Concept']
        ))

        query = get_check_for_iri_query('http://example.com')

        self.assertTrue(graph.query(query))

    def test_check_for_iri_does_not_exist(self):

        graph = Graph()
        graph.add((
            URIRef('http://example.com/1'), RDF['type'], SKOS['Concept']
        ))

        query = get_check_for_iri_query('http://example.com')

        self.assertFalse(graph.query(query))

    def test_get_concept_iris(self):

        graph = Graph()
        graph.add((
            URIRef('http://example.com/1'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/2'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/3'), RDF['type'], SKOS['Concept']
        ))

        query = get_concept_iris_query()
        uris = graph.query(query)

        self.assertTrue(len(uris) == 3)

    def test_get_concept_iris_mixed(self):

        graph = Graph()
        graph.add((
            URIRef('http://example.com/1'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/2'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/3'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/4'), RDF['type'], SKOS['NotAConcept']
        ))

        query = get_concept_iris_query()
        uris = graph.query(query)

        self.assertTrue(len(uris) == 3)

    def test_get_maximum_finish_interval_query(self):

        graph = Graph()
        graph.add((
            URIRef('http://example.com/1'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/1'), URIRef('http://www.w3.org/2006/time#intervalFinishedBy'), BNode('_:test_1')
        ))
        graph.add((
            BNode('_:test_1'), URIRef('http://www.w3.org/2006/time#hasDateTimeDescription'), BNode('_:test_2')
        ))
        graph.add((
            BNode('_:test_2'), URIRef('http://www.w3.org/2006/time#year'), Literal(2000)
        ))

        query = get_maximum_finishing_interval_query()
        actual = graph.query(query)

        self.assertTrue(int(list(actual)[0]['max']) == 2000)

    def test_get_minimum_starting_interval_query(self):

        graph = Graph()
        graph.add((
            URIRef('http://example.com/1'), RDF['type'], SKOS['Concept']
        ))
        graph.add((
            URIRef('http://example.com/1'), URIRef('http://www.w3.org/2006/time#intervalStartedBy'), BNode('_:test_1')
        ))
        graph.add((
            BNode('_:test_1'), URIRef('http://www.w3.org/2006/time#hasDateTimeDescription'), BNode('_:test_2')
        ))
        graph.add((
            BNode('_:test_2'), URIRef('http://www.w3.org/2006/time#year'), Literal(2000)
        ))

        query = get_minimum_starting_interval_query()
        actual = graph.query(query)

        self.assertTrue(int(list(actual)[0]['min']) == 2000)

    def test_get_minimum_starting_interval_query_mock(self):
        graph = Graph()
        graph.parse(
            "/Users/maxwell/Code/periodo-umbrella-periods/scripts/data/periodo-data.ttl",
            format="turtle"
        )

        query = get_minimum_starting_interval_query()
        actual = graph.query(query)

        actual_list = list(actual)
        actual_int = actual_list[0]
        actual_min = actual_int[
            actual_int['labels']['min']
        ]

        self.assertTrue(int(list(actual)[0]['min']) == 2000)
