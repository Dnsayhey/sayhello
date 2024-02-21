import click

from sayhello import app, db


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    "Init database."
    if drop:
        click.confirm("Are you sure?!", abort=True)
        db.drop_all()
        click.echo("Database deleted.")
    db.create_all()
    click.echo("Initialized database.")
