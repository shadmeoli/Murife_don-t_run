import time
import emoji

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

hes_running = emoji.emojize(":person_running:")


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


if __name__ == "__main__":
    typer.run(main)
