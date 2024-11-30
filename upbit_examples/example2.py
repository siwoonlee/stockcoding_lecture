import pyupbit
from pyupbit import WebSocketManager


def run_websocket(target_tickers_list=[]):
    wm = WebSocketManager("ticker", target_tickers_list, qsize=100000)
    for i in range(10):  # 무한히 가져오려면 while True:
        data = wm.get()
        print(data)
    wm.terminate()


if __name__ == '__main__':
    # run_websocket(["KRW-XRP", "KRW-BTC"])  # 리플, 비트코인 실시간 시세 등록
    all_tickers_list = pyupbit.get_tickers()
    run_websocket(all_tickers_list)  # 전종목 실시간 시세 등록
