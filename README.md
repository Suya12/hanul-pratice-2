FastAPI CRUD Assignment

본 프로젝트는 FastAPI를 이용하여 과제 요구사항(POST/GET/PUT/DELETE 각 2개씩 총 8개 API, 미들웨어, 다양한 응답 코드 사용, 공통 응답 포맷 적용)을 충족하는 예제 백엔드 서버입니다.

📌 1. 프로젝트 구조

```bash
📁 project-root
 └── main.py    # FastAPI 서버 코드
```

📌 2. API 설명 (8개)
✅ POST (2개)
1) 아이템 생성

```POST /items```

201 Created

Request Body:
```json
{ "name": "item1", "price": 1000 }
```

Response:
```json
{
  "status": "success",
  "data": { "id": 1, "name": "item1", "price": 1000 }
}
```

2) 의도된 400 에러

```POST /items/error```

- 400 Bad Request

✅ GET (2개)

3) 특정 아이템 조회

GET /items/{item_id}

200 OK

404 Not Found (존재하지 않는 경우)

4) 전체 아이템 조회

GET /items

200 OK

현재 저장된 모든 데이터 반환

✅ PUT (2개)
5) 아이템 수정

PUT /items/{item_id}

200 OK

404 Not Found

6) 의도된 서버 에러

PUT /items/error

500 Internal Server Error

✅ DELETE (2개)
7) 아이템 삭제

DELETE /items/{item_id}

200 OK

404 Not Found

8) 전체 삭제

DELETE /items

204 No Content

내용 없음 반환

📌 7. 미들웨어 기능

서버의 모든 요청을 출력하는 로깅 미들웨어 포함:

예시 출력:

```csharp
[Request] GET http://127.0.0.1:8000/items
[Response] status=200
```

📌 9. 테스트 화면 (Screenshots)

해당 섹션은 과제 제출 시 직접 실행한 Swagger / Postman / Terminal 등 캡처 이미지 넣으면 됨.

예:

서버 실행 화면

Swagger로 POST/GET/PUT/DELETE 테스트한 스크린샷

로그 미들웨어 출력 화면