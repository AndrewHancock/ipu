import yfinance as yf
import click
import os


@click.group()
def ipu():
    pass


@ipu.command()
@click.option('--symbol', help='Ticker symbol to export', required=True)
@click.option('--output_path', help='The location to save a CSV file containing the ticker symbol history.', required=True)
def export_price_history(symbol: str, output_path: str):
    hist = yf.Ticker(symbol).history(period="max")

    hist.to_csv(output_path)


def main():
    if not os.path.exists('../data'):
        os.mkdir('../data')

    export_price_history('VTI', f'../data/vti.csv')


if __name__ == '__main__':
    main()
