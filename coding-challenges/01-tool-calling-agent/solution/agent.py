"""A deliberately small, provider-neutral tool-calling runtime."""

import ast
from dataclasses import dataclass
import operator
from typing import Any, Callable


@dataclass(frozen=True)
class ToolRequest:
    name: str
    arguments: dict[str, Any]


Model = Callable[[tuple[str, ...]], ToolRequest | str]


class ToolCallingAgent:
    def __init__(self, tools: dict[str, Callable[..., Any]], model: Model, max_steps: int = 5) -> None:
        if max_steps < 1:
            raise ValueError("max_steps must be positive")
        self._tools = dict(tools)
        self._model = model
        self._max_steps = max_steps

    def run(self, prompt: str) -> str:
        observations: tuple[str, ...] = (prompt,)
        for _ in range(self._max_steps):
            decision = self._model(observations)
            if isinstance(decision, str):
                return decision
            if not isinstance(decision, ToolRequest):
                raise TypeError("model must return ToolRequest or str")
            observations = (*observations, self._execute(decision))
        return "Agent stopped after reaching the step budget."

    def _execute(self, request: ToolRequest) -> str:
        tool = self._tools.get(request.name)
        if tool is None:
            return f"tool_error: unknown tool {request.name}"
        try:
            result = tool(**dict(request.arguments))
        except (TypeError, ValueError, KeyError, ArithmeticError) as error:
            return f"tool_error: invalid arguments ({error})"
        except Exception as error:  # tool failures are observations, not runtime crashes
            return f"tool_error: execution failed ({error})"
        return f"tool_result: {result}"


def calculate(expression: str) -> float:
    """Evaluate a tiny arithmetic grammar without executing arbitrary code."""
    operations = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}

    def visit(node: ast.AST) -> float:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return float(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](visit(node.left), visit(node.right))
        raise ValueError("expression contains unsupported syntax")

    try:
        return visit(ast.parse(expression, mode="eval").body)
    except (SyntaxError, ZeroDivisionError, OverflowError) as error:
        raise ValueError("invalid arithmetic expression") from error


def service_status(service: str) -> str:
    statuses = {"search": "healthy", "billing": "degraded"}
    if service not in statuses:
        raise ValueError("unknown service")
    return statuses[service]
