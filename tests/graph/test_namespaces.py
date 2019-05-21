from unittest import TestCase
from periodo_umbrella_periods_cli.graph.terms import PeriodONamespaceManager


class TestUmbrellaNamespaces(TestCase):

    def test__init__(self):

        ns = PeriodONamespaceManager()
        self.assertIsNotNone(ns)
