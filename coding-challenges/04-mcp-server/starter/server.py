"""Starter surface for the protocol challenge."""


class McpServer:
    def list_tools(self) -> list[dict[str, object]]:
        raise NotImplementedError

    def handle(self, request: dict[str, object]) -> dict[str, object]:
        raise NotImplementedError
