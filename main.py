from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# -----------------------
# 공통 응답 포맷 함수
# -----------------------
def response(status: str, data=None, message: str = None):
    return {
        "status": status,
        "data": data,
        "message": message
    }

# -----------------------
# 미들웨어 (요청 로깅)
# -----------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"[Request] {request.method} {request.url}")

    try:
        response = await call_next(request)
    except Exception as e:
        # 500 에러 발생 시 처리
        return JSONResponse(
            status_code=500,
            content=response("error", message="Internal Server Error")
        )

    print(f"[Response] status={response.status_code}")
    return response


# -----------------------
# 데이터 저장용 메모리 DB (예시)
# -----------------------
fake_db = {}
next_id = 1

# -----------------------
# Request Body Model
# -----------------------
class Item(BaseModel):
    name: str
    price: int


# =======================================================
#                  POST (2개)
# =======================================================

# 1. 아이템 생성
@app.post("/items", status_code=201)
async def create_item(item: Item):
    global next_id
    fake_db[next_id] = item.dict()
    created_id = next_id
    next_id += 1

    return response("success", {"id": created_id, **item.dict()})


# 2. 일부러 에러 내기 (400 Bad Request 예시)
@app.post("/items/error")
async def create_error():
    raise HTTPException(status_code=400, detail="잘못된 요청입니다.")


# =======================================================
#                  GET (2개)
# =======================================================

# 3. 특정 아이템 조회
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")

    return response("success", fake_db[item_id])


# 4. 전체 아이템 조회
@app.get("/items")
async def get_all_items():
    return response("success", fake_db)


# =======================================================
#                  PUT (2개)
# =======================================================

# 5. 아이템 수정
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")

    fake_db[item_id] = item.dict()
    return response("success", {"id": item_id, **item.dict()})


# 6. 일부러 500 내부 에러 반환
@app.put("/items/error")
async def update_error():
    raise HTTPException(status_code=500, detail="서버 오류 발생 테스트")


# =======================================================
#                  DELETE (2개)
# =======================================================

# 7. 아이템 삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del fake_db[item_id]
    return response("success", {"deleted": item_id})


# 8. 전체 삭제 (204 No Content)
@app.delete("/items", status_code=204)
async def delete_all_items():
    fake_db.clear()
    return JSONResponse(
        status_code=204,
        content=None
    )
