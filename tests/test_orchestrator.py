from app.orchestrator import Orchestrator

agent = Orchestrator()

def test_routes_and_executes_calculation():
    result = agent.run("calcular 2 + 3 * 4")
    assert result.route == "calculator"
    assert result.status == "ok"
    assert result.answer == "14.0"

def test_rejects_unsafe_calculation():
    result = agent.run("calcular __import__('os').getcwd()")
    assert result.route == "calculator"
    assert result.status == "tool_error"

def test_routes_knowledge_request():
    assert agent.run("explique RAG").route == "knowledge"

def test_rejects_empty_request():
    result = agent.run("   ")
    assert result.status == "rejected"
    assert result.route == "fallback"
