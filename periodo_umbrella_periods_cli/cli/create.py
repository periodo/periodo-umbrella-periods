import click

from periodo_umbrella_periods_cli.graph import UmbrellaPeriods
from periodo_umbrella_periods_cli.cli.types import IRIParamType


@click.command()
@click.argument('iris', nargs=-1, default=None, type=IRIParamType())
@click.option('--src', '-s', multiple=True, type=click.Path(exists=True))
@click.pass_context
def create(context, iris, src="default"):
    """Creates a new 'umbrella' PeriodO Authority from the given PeriodO Period URIs."""

    umbrella = UmbrellaPeriods()

    query = umbrella.prepare_query(iris)

    result = umbrella.query(query)

    click.echo(result.serialize(format='n3'))
