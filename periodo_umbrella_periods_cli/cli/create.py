import click

from ..graph.prepared_queries import get_create_new_period_collection_query
from ..graph.umbrella import UmbrellaPeriods
from .types import IRIParamType


@click.command()
@click.argument('iris', nargs=-1, default=None, type=IRIParamType())
@click.option('--src', '-s', multiple=True, type=click.Path(exists=True))
@click.pass_context
def create(context, iris, src="default"):
    """Creates a new 'umbrella' PeriodO Authority from the given PeriodO Period URIs."""

    umbrella = UmbrellaPeriods(store=src)

    query = get_create_new_period_collection_query(umbrella.get_identifier(), iris)

    result = umbrella.query(query)

    click.echo(result.serialize(format='n3'))
