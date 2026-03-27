import kis_auth as ka
from ccnl_krx import ccnl_krx
import os
from datetime import datetime

print("1. 시작")

#1. 웹소켓 인증 (Approval Key 발급)
ka.auth_ws(svr="vps")  # 모의투자
print("2. 인증 완료")

#2. 웹소켓 객체 생성
ws = ka.KISWebSocket(api_url="/ws")
print("3. 웹소켓 객체 생성")

#3. Data 폴더 생성 (없으면 자동 생성)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")
os.makedirs(DATA_DIR, exist_ok=True)

#4. 저장 파일 경로
CSV_PATH = os.path.join(DATA_DIR, f"ccnl_005930_{datetime.today().strftime('%Y%m%d')}.csv")

#5. 데이터 수신 콜백
def on_data(ws, tr_id, df, meta):
    print("==== 실시간 데이터 ====")
    print(df.tail())

    # 파일이 없으면 헤더 포함, 있으면 헤더 없이 추가
    write_header = not os.path.exists(CSV_PATH)
    df.to_csv(CSV_PATH, mode='a', header=write_header, index=False, encoding='utf-8-sig')

#6. 구독 (삼성전자 체결)
ka.KISWebSocket.subscribe(
    ccnl_krx,
    "005930",
    {"env_dv": "demo"}  # 모의투자 필수
)

print("4. 구독 완료")

#7. 웹소켓 시작
ws.start(on_data)

print("❗ 이 메시지 나오면 비정상 종료")