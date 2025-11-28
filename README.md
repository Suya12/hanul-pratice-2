FastAPI CRUD Assignment

본 프로젝트는 FastAPI를 이용하여 과제 요구사항(POST/GET/PUT/DELETE 각 2개씩 총 8개 API, 미들웨어, 다양한 응답 코드 사용, 공통 응답 포맷 적용)을 충족하는 예제 백엔드 서버입니다.

<img width="3296" height="1788" alt="13" src="https://github.com/user-attachments/assets/3a39eb02-1112-4c1b-99d3-4836aeb052ce" />


📌 1. 프로젝트 구조

```bash
📁 project-root
 └── main.py    # FastAPI 서버 코드
```

📌 2. API 설명 (8개)

✅ POST (2개)
1) 아이템 생성 

`POST /items`

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

- 201 Created

<img width="3195" height="1478" alt="image" src="https://github.com/user-attachments/assets/190cc0e7-535a-4b56-bc0c-5d59c756c2dc" />


2) 의도된 400 에러 

`POST /items/error`

- 400 Bad Request

<img width="3217" height="1359" alt="image" src="https://github.com/user-attachments/assets/cefa2dad-05b2-48c5-a4be-98ce25bff6d3" />


✅ GET (2개)


3) 특정 아이템 조회

`GET /items/{item_id}`

- 200 OK (아이템 존재)

<img width="3186" height="1311" alt="image" src="https://github.com/user-attachments/assets/3be66f5b-a7d0-4d76-a171-41ed9d858bf2" />


- 404 Not Found (존재하지 않는 경우)

<img width="3201" height="1284" alt="image" src="https://github.com/user-attachments/assets/c586bda9-f60a-4b41-ad31-b653329ef31e" />



4) 전체 아이템 조회

`GET /items`

- 200 OK

현재 저장된 모든 데이터 반환

<img width="3201" height="1579" alt="image" src="https://github.com/user-attachments/assets/35cbbbe6-3b64-4f34-8fa9-004b7801c861" />


✅ PUT (2개)
5) 아이템 수정

`PUT /items/{item_id}`

- 200 OK

<img width="3181" height="1498" alt="image" src="https://github.com/user-attachments/assets/e15b4f59-d529-4185-a2e1-c4e37064e84e" />


- 404 Not Found

<img width="3168" height="1257" alt="image" src="https://github.com/user-attachments/assets/eb58a9a3-120b-4e7a-b284-981277b8e0a2" />



6) 의도된 서버 에러

`PUT /items/error`

- 500 Internal Server Error


✅ DELETE (2개)
7) 아이템 삭제

`DELETE /items/{item_id}`

- 200 OK (삭제 성공)

- 404 Not Found (존재하지 않은 아이템)


8) 전체 삭제

`DELETE /items`

- 204 No Content

내용 없음 반환


📌 3. 미들웨어 기능

서버의 모든 요청을 출력하는 로깅 미들웨어 포함:

예시 출력:

```csharp
[Request] GET http://127.0.0.1:8000/items
[Response] status=200
```


📌 4. 테스트 화면 (Screenshots)

Swagger 화면

예:

서버 실행 화면

Swagger로 POST/GET/PUT/DELETE 테스트한 스크린샷

로그 미들웨어 출력 화면
