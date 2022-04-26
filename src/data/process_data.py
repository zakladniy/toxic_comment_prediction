"""Process data: create csv file with comments and targets from
raw txt-data."""
import click
import pandas as pd
from loguru import logger


def open_text(path: str) -> list[str]:
    """Open data from .txt file

    @param path: path to txt-data
    @return: data from txt-file
    """
    with open(path) as f:
        data_txt = f.readlines()
        data_txt = [item.strip() for item in data_txt]
    logger.info("Create data from txt-file")
    return data_txt


def separate_target_and_value(data_list: list) -> pd.DataFrame:
    """Separate target and values in dataset and create pandas DataFrame.

    @param data_list: data from txt-file
    @return: separated data
    """
    result = []
    for row in data_list:
        splitted_row = row.split(" ", 1)
        d = {}
        target = splitted_row[0].replace('__label__', '')
        d['target'] = 0 if target == 'NORMAL' else 1
        d['text'] = splitted_row[1]
        result.append(d)
    logger.info("Create pandas DataFrame")
    return pd.DataFrame(result)


@click.command()
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(input_filepath: str, output_filepath: str) -> None:
    """Create csv file with comments and targets from raw txt-data.

    @param input_filepath: path to txt-data
    @param output_filepath: path to csv-data
    """
    data_txt = open_text(path=input_filepath)
    df = separate_target_and_value(data_list=data_txt)
    df.to_csv(output_filepath, index=False)
    logger.info("Write DataFrame to csv-file")


if __name__ == "__main__":
    main()
