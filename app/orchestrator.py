import ast
import operator
from dataclasses import dataclass

@dataclass
class AgentResult:
    route: str
    answer: str
    status: str

_ALLOWED_OPERATORS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}

def calculate(expression: str) -> float:
    tree = ast.parse(expression, mode="eval")
    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](evaluate(node.left), evaluate(node.right))
        raise ValueError("Unsupported expression")
    return evaluate(tree)

class Orchestrator:
    def run(self, request: str) -> AgentResult:
        text = request.strip()
        if not text:
            return AgentResult(route="fallback", answer="A request is required.", status="rejected")
        lower = text.lower()
        if lower.startswith(("calcular ", "calculate ")):
            expression = text.split(" ", 1)[1]
            try:
                result = calculate(expression)
            except (ValueError, SyntaxError, ZeroDivisionError):
                return AgentResult(route="calculator", answer="Invalid or unsupported calculation.", status="tool_error")
            return AgentResult(route="calculator", answer=str(result), status="ok")
        return AgentResult(route="knowledge", answer="Knowledge route selected in demo mode.", status="ok")
