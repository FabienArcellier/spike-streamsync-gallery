import alfred

@alfred.command("run", help="execute the application")
def run():
    """
    execute the application

    >>> $ alfred run
    """
    alfred.run("streamsync run src/app")

@alfred.command("edit", help="execute the application")
def edit():
    """
    execute the application

    >>> $ alfred run
    """
    alfred.run("streamsync edit src/app")
