# Agent-to-Agent Protocols

Agent-to-agent protocols describe how one agent or service delegates work to another. The hard engineering problem is not message transport; it is identity, capability discovery, task ownership, cancellation, partial results, and authorization. Keep delegation bounded and observable, and prefer a direct service call when the boundary is not genuinely agentic.
