import kis_auth as ka
from ccnl_krx import ccnl_krx

print("1. 시작")

#1. 웹소켓 인증 (Approval Key 발급)
ka.auth_ws(svr="vps")  # 모의투자
print("2. 인증 완료")

#2. 웹소켓 객체 생성 (api_url 넣지 않는게 핵심)
ws = ka.KISWebSocket(api_url="/ws")
print("3. 웹소켓 객체 생성")

#3. 데이터 수신 콜백
def on_data(ws, tr_id, df, meta):
    print("==== 실시간 데이터 ====")
    print(df.tail())

#4. 구독 (삼성전자 체결)
ka.KISWebSocket.subscribe(
    ccnl_krx,
    "005930",
    {"env_dv": "demo"}  # 모의투자 필수
)

print("4. 구독 완료")

#5. 웹소켓 시작 (여기서 멈추는게 정상)
ws.start(on_data)

print("❗ 이 메시지 나오면 비정상 종료")