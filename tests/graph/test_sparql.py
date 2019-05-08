from unittest import TestCase
from rdflib import URIRef, RDF, Literal

from periodo_umbrella_periods_cli.graph.sparql import *


class TestSPARQLStatements(TestCase):

    def test_max_sparql(self):
        expected = "(MAX(?x) AS ?max)"

        actual = max_sparql('x', 'max')

        self.assertEqual(actual, expected)

    def test_min_sparql(self):
        expected = "(MIN(?x) AS ?min)"

        actual = min_sparql('x', 'min')

        self.assertEqual(actual, expected)

    def test_set_sparql_uris(self):

        expected = "(<http://example.com>)"

        actual = set_sparql([URIRef('http://example.com')])

        self.assertEqual(actual, expected)

    def test_set_sparql_multiple_uris(self):

        expected = "(<http://example.com/1>, <http://example.com/2>, <http://example.com/3>)"

        actual = set_sparql([

            URIRef('http://example.com/1'),
            URIRef('http://example.com/2'),
            URIRef('http://example.com/3')

        ])

        self.assertEqual(actual, expected)

    def test_set_sparql_multiple_all_types(self):

        expected = '(<http://example.com>, {a}, "example.com")'.format(a=RDF['type'].n3())

        actual = set_sparql([

            URIRef('http://example.com'),
            RDF['type'],
            Literal("example.com")

        ])

        self.assertEqual(actual, expected)