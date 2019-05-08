from rdflib import Graph, URIRef

from periodo_umbrella_periods_cli.utilities import create_periodo_skolem_iri


class UmbrellaPeriods(Graph):

    def __init__(self, store="default", namespace_manager=None):

        identifier = URIRef(create_periodo_skolem_iri())

        super(UmbrellaPeriods, self).__init__(

            identifier=identifier,
            store=self._determine_store(store),
            namespace_manager=namespace_manager

        )

    def _determine_store(self, store):

        if self.store == "default":

            return "data/periodo.jsonld"

        else:

            return store

    def get_identifier(self):

        return self.identifier
