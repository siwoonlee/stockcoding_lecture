import pyupbit

api_key = '2hxnaiQmKZgAAdzTMyA5POmTTJDuxaTxK41nmUKy'
api_secret = 'Ye8qKIuEdxtvJmcKtG51VxfjnZYC9D44KhlTvKxq'
upbit_api = pyupbit.Upbit(api_key, api_secret)

# 모든 코인 티커 리스트
all_tickers_list = pyupbit.get_tickers()
print(all_tickers_list)

# 특정 코인/원화 잔고 조회  (미체결 제외)
res = upbit_api.get_balance(ticker="KRW")

# 특정 코인/원화 잔고 조회  (미체결 포함)
res = upbit_api.get_balance_t(ticker="KRW")

# 계좌 전체 현황 조회
res_list = upbit_api.get_balances()
for per_coin_info in res_list:
    currency = per_coin_info["currency"]
    if "KRW" in currency:
        continue
    coin_full_name = "KRW-" + per_coin_info["currency"]  # 코인명
    carry_amount = float(per_coin_info["locked"]) + float(per_coin_info["balance"])  # 보유 수량
    print(coin_full_name, carry_amount)

# 특정 코인 현재가 조회
pyupbit.get_current_price("KRW-XRP")

# 각종 주문
res = upbit_api.buy_market_order("KRW-XRP", 10_000)  # 1만원 만큼 리플 코인 시장가 매수 주문
res = upbit_api.buy_limit_order("KRW-XRP", 2000, 10)  # 리플 코인 2000원에 10개 지정가 매수 주문
res = upbit_api.sell_market_order("KRW-XRP", 5)  # 리플 코인 5개 시장가 매도 주문
res = upbit_api.sell_limit_order("KRW-XRP", 3000, 10)  # 리플 코인 3000원에 10개 지정가 매도 주문

unsupervised_order = upbit_api.get_order("KRW-XRP")  # 리플 코인 미체결 조회
for order_info_dict in unsupervised_order:
    res = upbit_api.cancel_order(order_info_dict["uuid"])  # 미체결 취소 주문
    print(f"취소 주문 결과: {res}")

# 리플 코인 일봉 차트 데이터 조회
df = pyupbit.get_ohlcv("KRW-XRP", count=600, period=0.2)
print(df)

# 리플 코인 3분봉 차트 데이터 조회
df = pyupbit.get_ohlcv("KRW-XRP", interval="minute3", count=600, period=0.2)
print(df)
