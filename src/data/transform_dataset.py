"""Transform dataset: select some columns."""
import click
import pandas as pd


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """Drop some columns from external dataset and write interim dataset.

    @param input_filepath: path to external dataset
    @param output_filepath: path to int
    """
    pass

if __name__ == "__main__":
    main()
