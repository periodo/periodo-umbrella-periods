from unittest import TestCase

from periodo_umbrella_periods_cli.utilities import create_periodo_skolem_iri


class TestUtilities(TestCase):

    def test_create_periodo_skolem_iri(self):

        trails = 10000
        cache = set()

        for trial in range(trails):

            cache.add(create_periodo_skolem_iri())

        self.assertEqual(trails, len(cache))
