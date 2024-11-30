import time
import random

from loguru import logger
import pyupbit
from pyupbit import WebSocketManager


def main(upbit_api, target_ticker_list):
    wm = WebSocketManager("ticker", target_ticker_list, qsize=100000)
    ticker_to_last_chart_req_unix_time_map = {ticker: time.time() for ticker in target_ticker_list}
    while True:
        data = wm.get()
        # print(data)
        ticker = data["code"]
        trade_price = data["trade_price"]
        current_unix_time = time.time()
        if current_unix_time - ticker_to_last_chart_req_unix_time_map[ticker] < 1:  # 각 코인별 1초에 한번만 요청
            continue
        ticker_to_last_chart_req_unix_time_map[ticker] = current_unix_time
        df = pyupbit.get_ohlcv(data["code"])
        # print(ticker, df)
        # 트레이딩 로직 적용
        is_buy_signal = random.choice([True, False])
        is_sell_signal = random.choice([True, False])

        if is_buy_signal:
            res = upbit_api.buy_market_order(ticker, 10_000)  # 1만원 만큼 코인 시장가 매수 주문
            logger.info(f"코인: {ticker} 시장가 매수 주문 결과: {res}")
        if is_sell_signal and ticker == "KRW-XRP":
            res = upbit_api.sell_market_order(ticker, 5)  # 코인 5개 시장가 매도 주문
            logger.info(f"코인: {ticker} 시장가 매도 주문 결과: {res}")


if __name__ == '__main__':
    api_key = '2hxnaiQmKZgAAdzTMyA5POmTTJDuxaTxK41nmUKy'
    api_secret = 'Ye8qKIuEdxtvJmcKtG51VxfjnZYC9D44KhlTvKxq'
    upbit_api = pyupbit.Upbit(api_key, api_secret)
    target_ticker_list = ["KRW-BTC", "KRW-ETH", "KRW-SOL", "KRW-XRP"]
    main(upbit_api, target_ticker_list)
