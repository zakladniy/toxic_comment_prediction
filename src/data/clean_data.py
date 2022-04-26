"""Clean data: drop trash symbols."""
import click
import pandas as pd
from loguru import logger
from tqdm import tqdm

from src.data.text_preprocessing import text_preprocessing

tqdm.pandas()


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """Clean data: drop thrash symbols from csv-file.

    @param input_filepath: path to processed csv file
    @param output_filepath: path to clean data
    """
    df = pd.read_csv(input_filepath)
    df['text'] = df['text'].progress_apply(text_preprocessing)
    df.to_csv(output_filepath, index=False)
    logger.info("Write DataFrame with clean data to csv-file")


if __name__ == "__main__":
    main()
