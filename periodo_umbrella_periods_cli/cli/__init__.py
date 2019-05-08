import click

from .create import create


@click.group()
@click.option('--verbose', '-v', is_flag=False)
@click.pass_context
def root(context, verbose):
    context.ensure_object(dict)
    context.obj['VERBOSE'] = verbose


root.add_command(create)

if __name__ == '__main__':

    root(obj={})
