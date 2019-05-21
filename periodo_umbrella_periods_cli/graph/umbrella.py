from rdflib import Graph, URIRef
from periodo_umbrella_periods_cli.graph.prepared_queries import *
from periodo_umbrella_periods_cli.graph.terms import PeriodONamespaceManager, create_bindings_dict
from periodo_umbrella_periods_cli.utilities import create_periodo_skolem_iri


class UmbrellaPeriods(Graph):

    def __init__(self, derived_from=None):

        self._skolem = URIRef(create_periodo_skolem_iri())
        self._derived_from = derived_from

        super(UmbrellaPeriods, self).__init__(

            identifier=self._skolem,
            namespace_manager=PeriodONamespaceManager()

        )

        # TODO: Implement ETag caching
        self.parse('http://n2t.net/ark:/99152/p0d.json', format='json-ld')

    def _insert_derived_from_data(self):

        self.update(

            insert_derived_from(

                self._skolem,
                self._derived_from

            )
        )

    def _insert_spatial_description_data(self):

        self.update(

            insert_spatial_descriptions(

                self._skolem,
                self._derived_from

            )
        )

    def _insert_time_interval_data(self):

        self.update(

            insert_time_interval_bounds(

                self._skolem,
                self._derived_from

            )
        )

    def create_umbrella(self):

        self._insert_derived_from_data()
        self._insert_spatial_description_data()
        self._insert_time_interval_data()

    def describe_skolem(self):

        return self.query(

            describe_skolem(self._skolem),
            initNs=create_bindings_dict()

        )

    def get_skolem(self):

        return self._skolem
