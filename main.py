# Importing Modules
import sqlite3 as sql
import click

# Sqlite Copnnections
db = sql.connect("main.db")
cur = db.cursor()

# Creates sqlite table to save data to
cur.execute("CREATE TABLE IF NOT EXISTS data(title TEXT, main TEXT)")

db.commit()
db.close()

# Creating Click Commands
@click.command()
@click.option("--c", "--command", type=str, default="nil")
def main(c):
    if c == "log":
        # User Input
        title = input("Enter Log Title: ")
        main = input("Enter Log Text: ")

        # Connecting To Sqlite
        db = sql.connect("main.db")
        cur = db.cursor()

        data = (
            (title, main)
        )

        cur.execute("INSERT INTO data VALUES(?,?)", data)

        db.commit()
        db.close()

    elif c == "save":
        db = sql.connect("main.db")
        cur = db.cursor()

        cur.execute(f"SELECT * FROM data")

        data = cur.fetchall()

        f = open("text.txt", "w")
        for i in data:
            f.write(f"Title: {i[0]} : Log: {i[1]}")
            f.close()

        click.secho("Logged Data To : Text.txt", fg="blue", bold=True)

    else:
        click.secho(f"{datetime.datetime.now()}", fg="blue", bold=True)
        click.secho("Error: Unknown Command : Typo?", fg="red", bold=True, blink=True)

if __name__ == "__main__":
    main()
