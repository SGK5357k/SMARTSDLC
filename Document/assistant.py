from fastapi import APIRouter

router = APIRouter()

@router.get("/ask")
async def ask_city_bot(question: str):
    return {"answer": f"You asked: {question}. (IBM Granite integration coming soon)"}
