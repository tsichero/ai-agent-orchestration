from fastapi import FastAPI
from pydantic import BaseModel, Field
from .orchestrator import Orchestrator

app = FastAPI(title="AI Agent Orchestration", version="0.1.0")
orchestrator = Orchestrator()

class AgentRequest(BaseModel):
    request: str = Field(min_length=1, max_length=2000)

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-agent-orchestration"}

@app.post("/run")
def run(request: AgentRequest):
    result = orchestrator.run(request.request)
    return {"route": result.route, "answer": result.answer, "status": result.status}
