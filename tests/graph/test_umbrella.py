from unittest import TestCase
from periodo_umbrella_periods_cli.graph.umbrella import UmbrellaPeriods


class TestUmbrella(TestCase):

    def test_skolem_identifier_generation(self):

        graph = UmbrellaPeriods()

        graph2 = UmbrellaPeriods()

        self.assertNotEqual(graph.get_skolem(), graph2.get_skolem())

    def test_create_umbrella(self):

        graph = UmbrellaPeriods(

            derived_from=[

                "http://n2t.net/ark:/99152/p03wskdvwkb",
                "http://n2t.net/ark:/99152/p03wskdbh6h"

            ]

        )

        graph.create_umbrella()

        self.assertTrue(True)
