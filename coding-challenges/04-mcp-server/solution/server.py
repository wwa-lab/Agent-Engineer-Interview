"""Tiny JSON-RPC dispatcher with explicit capability and argument checks."""

from typing import Any


class McpServer:
    def list_tools(self) -> list[dict[str, object]]:
        return [{"name": "sum", "description": "Add two numbers", "input": ["left", "right"]}]

    def handle(self, request: dict[str, object]) -> dict[str, object]:
        request_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})
        if not isinstance(method, str):
            return self._error(request_id, -32600, "method is required")
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": request_id, "result": {"tools": self.list_tools()}}
        if method == "tools/call":
            return self._call_tool(request_id, params)
        if method == "resources/read":
            if params == {"uri": "memory://health"}:
                return {"jsonrpc": "2.0", "id": request_id, "result": {"contents": [{"text": "ok"}]}}
            return self._error(request_id, -32004, "resource not found")
        return self._error(request_id, -32601, "method not found")

    def _call_tool(self, request_id: object, params: object) -> dict[str, object]:
        if not isinstance(params, dict) or params.get("name") != "sum":
            return self._error(request_id, -32602, "unknown tool")
        arguments = params.get("arguments")
        if not isinstance(arguments, dict) or not self._numbers(arguments.get("left"), arguments.get("right")):
            return self._error(request_id, -32602, "left and right must be numbers")
        result = float(arguments["left"]) + float(arguments["right"])
        return {"jsonrpc": "2.0", "id": request_id, "result": {"content": [{"text": str(result)}]}}

    @staticmethod
    def _numbers(left: Any, right: Any) -> bool:
        return isinstance(left, (int, float)) and not isinstance(left, bool) and isinstance(right, (int, float)) and not isinstance(right, bool)

    @staticmethod
    def _error(request_id: object, code: int, message: str) -> dict[str, object]:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}
