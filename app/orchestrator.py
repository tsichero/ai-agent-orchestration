from dataclasses import dataclass

@dataclass
class AgentResult:
    route: str
    answer: str
    status: str

class Orchestrator:
    def run(self, request: str) -> AgentResult:
        text = request.strip()
        if not text:
            return AgentResult(route="fallback", answer="A request is required.", status="rejected")
        if "calcular" in text.lower() or "calculate" in text.lower():
            return AgentResult(route="calculator", answer="Tool route selected in demo mode.", status="ok")
        return AgentResult(route="knowledge", answer="Knowledge route selected in demo mode.", status="ok")
