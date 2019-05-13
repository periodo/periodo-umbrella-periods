from unittest import TestCase
from periodo_umbrella_periods_cli.graph.umbrella import UmbrellaPeriods


class TestUmbrella(TestCase):

    def test_skolem_identifier_generation(self):

        graph = UmbrellaPeriods()

        query = graph.prepare_query(["https://example.com", "https://example.com"])

        result = graph.query(query)

        self.assertIsNotNone(result)
