# Protocol Comparison

| Need | Direct API | MCP-style capability protocol | Agent-to-agent delegation |
| --- | --- | --- | --- |
| One internal integration | Simple and explicit | Often extra machinery | Usually excessive |
| Reusable tools across hosts | Custom adapters needed | Stronger fit | Not the primary goal |
| Delegating a task with progress | Add job API | Possible but secondary | Stronger fit |
| Governance | Application-owned | Still application-owned | Must cross identities and budgets |

Choose the smallest interface that preserves the required trust and lifecycle semantics.
