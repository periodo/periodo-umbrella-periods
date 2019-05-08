from unittest import TestCase
from periodo_umbrella_periods_cli.graph import UmbrellaAuthority
from periodo_umbrella_periods_cli.graph.terms import CONTEXT_LD


class TestUmbrellaAuthority(TestCase):

    def test_skolem_identifier_generation(self):

        graph = UmbrellaAuthority()

        self.assertIsNotNone(graph)

    def test_serialize(self):

        graph = UmbrellaAuthority()

        output = str(graph.serialize(format="json-ld", context=CONTEXT_LD, indent=4))

        self.assertEqual(output, "")
