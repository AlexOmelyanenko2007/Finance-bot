from alpha_vantage.timeseries import TimeSeries
import mplfinance as mpf


api_key = ""

ts = TimeSeries(key=api_key, output_format='pandas')

company = 'AMD'
interval_time = '60min'
data, meta_data = ts.get_intraday(symbol=company, interval=interval_time, outputsize='compact')
# print(data)
data.to_excel("output.xlsx") # создание excel-файла

data.rename(columns={
    "1. open": "Open",
    "2. high": "High",
    "3. low": "Low",
    "4. close": "Close",
    "5. volume": "Volume",
}, inplace=True)

mpf.plot(data, type='candle', mav=(3, 6, 9)) # отображение графика акций
