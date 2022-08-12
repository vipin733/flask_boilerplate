from flask.cli import FlaskGroup
from project import create_app, db
from  project.database.seeder import seedDB
app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.session.remove()
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    print(1)
    seedDB()

if __name__ == "__main__":
    cli()