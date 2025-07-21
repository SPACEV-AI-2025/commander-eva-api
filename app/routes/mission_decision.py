from fastapi import APIRouter
from pydantic import BaseModel
from app.services.decision_function import call_launch_decision

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/decision")
def mission_decision(req: QuestionRequest):
    try:
        result = call_launch_decision(req.question)
        return {
            "question": req.question,
            "decision": result["status"],
            "reason": result["reason"],
            "timestamp": result["timestamp"]
        }
    except Exception as e:
        return {"error": str(e)}
