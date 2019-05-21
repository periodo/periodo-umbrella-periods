from unittest import TestCase
from periodo_umbrella_periods_cli.graph.prepared_queries import *


class TestPreparedQueries(TestCase):

    def test_can_create_queries_without_throwing_error(self):

        skolem = "http://example.com/collection/9000"
        derived_from = [

            "http://example.com/collection/4",
            "http://example.com/collection/5",

        ]

        insert_time_interval_bounds(skolem, derived_from)
        insert_derived_from(skolem, derived_from)
        insert_spatial_descriptions(skolem, derived_from)

        self.assertTrue(True)
