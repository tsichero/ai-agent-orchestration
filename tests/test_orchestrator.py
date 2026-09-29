from app.orchestrator import Orchestrator

agent = Orchestrator()

def test_routes_calculation_request():
    result = agent.run("calcular faturamento")
    assert result.route == "calculator"
    assert result.status == "ok"

def test_routes_knowledge_request():
    result = agent.run("explique RAG")
    assert result.route == "knowledge"

def test_rejects_empty_request():
    result = agent.run("   ")
    assert result.status == "rejected"
    assert result.route == "fallback"
