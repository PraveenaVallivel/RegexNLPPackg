import click

debug_logging = False;

def debug(str):
    if debug_logging :
        click.secho((str))

def enable_debug(): 
    global debug_logging 
    debug_logging = True
   
def log(str):  
    click.echo(click.style(str, fg='green', bold=True))