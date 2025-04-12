# /// script
# dependencies = [
#   "typer",
# ]
# ///


import os

import typer

app = typer.Typer()


@app.command()
def flatten_directory(
    root_dir: str = typer.Argument(help="Root directory to flatten"),
    output_file: str | None = typer.Option(None, "--output", help="Output file path"),
    ignore_dirs: list[str] = typer.Option(
        [],
        "--ignore",
        help="Directories or files to ignore",
    ),
) -> None:
    """Flatten the directory structure starting from the given root directory into a single text output.
    Args:
        root_dir (str): Root directory to flatten.
        output_file (str | None): Optional; Path to the output file where the flattened content will be saved.
        ignore_dirs (list[str]): List of directories or files to ignore during the flattening process.
    Returns:
        None

    The function traverses the directory tree starting from `root_dir`, reads the content of each file, and
    concatenates it into a single string. The content is wrapped with XML-like tags indicating the file path.
    If `output_file` is provided, the result is written to that file; otherwise, it is printed to the console.
    """

    if output_file is not None:
        ignore_dirs.append(output_file)

    res = ""

    for subdir, _, files in os.walk(root_dir):
        if any(ignored in subdir for ignored in ignore_dirs):
            continue
        for file in files:
            if file in ignore_dirs:
                continue
            file_path = os.path.join(subdir, file)
            relative_path = os.path.relpath(file_path, root_dir)
            res += f"<file path={relative_path}>\n"
            try:
                with open(file_path, "r") as infile:
                    res += infile.read()
            except UnicodeDecodeError:
                typer.echo(f"Warning: Skipping binary file {file_path}")
                continue
            res += "\n</file>\n\n"

    if output_file is None:
        typer.echo(res)
    else:
        with open(output_file, "w") as outfile:
            outfile.write(res)

    typer.echo(f"Successfully flattened directory to {output_file}")


if __name__ == "__main__":
    app()