from rdflib import Graph, URIRef

from periodo_umbrella_periods_cli.utilities import create_periodo_skolem_iri
from periodo_umbrella_periods_cli.graph.prepared_queries import get_create_new_period_collection_query


class UmbrellaPeriods(Graph):

    def __init__(self):

        self.id = URIRef(create_periodo_skolem_iri())

        super(UmbrellaPeriods, self).__init__(

            identifier=self.id

        )

        self.parse('http://n2t.net/ark:/99152/p0d.json', format='json-ld')

    def get_identifier(self):

        return self.id

    def prepare_query(self, iris):

        return get_create_new_period_collection_query(self.id, iris)
