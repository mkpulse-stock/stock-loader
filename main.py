from flask import Flask
from waitress import serve
from app.yahoo import get_ticker_detail, get_symbols
from app.tool import upload_gcs_file, save_file
import os

app = Flask(__name__)

@app.route("/")
def health_check():
    return "ok"

@app.route("/symbols")
def all_symbols():
    bucket_name = os.environ['BUCKET_NAME']
    all_symbols = get_symbols()
    ### save all_symbols file in local
    filepath = os.path.join('.', 'all_symbols.json')
    save_file(filepath, all_symbols)
    ### upload to gcs
    upload_gcs_file(bucket_name, filepath, os.path.join('us', 'all_symbols.json'))
    return "ok"

@app.route("/<ticker>/detail")
def ticker_detail(ticker):
    return get_ticker_detail(ticker)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)