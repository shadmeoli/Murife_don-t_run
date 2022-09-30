""" 
	When you execute this file directly it will throw an error
	[typer.run(main) , where main -> is not defined],
	
	To avoid this run through the setup from the redme to get it up and running
"""
import time
import emoji

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

hes_running = emoji.emojize(":person_running:")

# [TODO] -> This function is to print only five emojis per delay. I am to use Async await for this feature/ when I get some time today(friday/30)
def the_runner():
	nums = 1
	__runner = [hes_running]
	while nums < 5:
		if len(__runner) < 5:

			print(__runner)
			__runner.append(hes_running)
			nums += 1

		if len(__runner) == 5:
			__runner.clear()
			__runner.append(hes_running)

# the main entry function
def murife():
	while True:
	    with Progress(
	        SpinnerColumn(),
	        TextColumn("[progress.description]{task.description}"),
	        transient=True,
	    ) as progress:
	        progress.add_task(description=f"[green bold]Murife[/green bold] [red]don't run...[/red] {hes_running}", total=None)
	        time.sleep(2)
	    print("Murife!")

# this will be executed while runnign the CLI from its entry point "murife"
if __name__ == "__main__":
    typer.run(main)
