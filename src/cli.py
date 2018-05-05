import click
from presentation import Presentation

@click.group()
def cli():
    pass

@click.command()
def status():
    presentation_obj.getRecentStatus()
    
cli.add_command(status)


if __name__=='__main__':
    presentation_obj = Presentation('/home/arun/Projects/bingoarun/folmon/sample-data')
    cli()