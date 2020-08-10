import click

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(filenames, count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    if filenames:
        click.echo("1")
    else:
        click.echo("2")
    click.echo(len(filenames))
    # for f in filenames:
        # click.echo(click.format_filename(f))
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
