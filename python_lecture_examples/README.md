# python 에서 텔레그램으로 메시지 보내는 방법

## pip install python-telegram-bot==13.12

### API KEY 발급
1. BotFather 검색
2. /newbot 채팅
3. 봇이름 설정
4. API KEY 발급 완료

### Chat ID 발급
1. 위에서 만든 봇이름을 검색
2. START 버튼 누르고 아무 메시지 보냄
3. 아래 주소에서 <bot_id>를 API KEY로 대체하여 크롬으로 접속 
- https://api.telegram.org/bot<bot_id>/getUpdates
4. Chat ID가 뜨지 않을 경우 다시 아무 메시지 보냄
5. Chat ID 발급 완료

