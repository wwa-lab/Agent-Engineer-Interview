# Model Context Protocol (MCP)

## Interview Question

What problem does MCP solve, and what does it not solve?

## Short Answer

MCP standardizes how an AI application discovers and invokes external capabilities and receives resources or prompts through a server boundary. It can reduce bespoke connector work, but it does not make a tool safe, authorize a user, evaluate an agent, or guarantee that a server is trustworthy.

## Core interaction

1. A host chooses a client and connects to a server through an agreed transport.
2. The server advertises capabilities such as tools, resources, or prompts.
3. The client presents selected capabilities to the model or application.
4. An invocation crosses the client/server boundary with structured arguments.
5. The result returns as data and is traced, validated, and policy-checked by the host.

The host should control which servers are installed, which tools are exposed for a task, which identity is used, and whether a mutation needs approval. Discovery is not permission.

## Example

A local repository MCP server may expose `search_files` and `read_file`. The host can allow both for analysis, but require a separate approval-gated `write_file` tool for edits. Tool descriptions should say what the server can access, what it changes, and what errors mean.

## Trade-offs

Standardization improves portability and ecosystem reuse. It also adds a trust boundary, version compatibility concerns, and another place where schemas or tool descriptions can drift. Keep a capability allowlist, pin server versions, sandbox processes, limit output size, and log invocations.

## Common Mistakes

- Treating every discovered server as trusted.
- Giving a read-only task access to mutation tools.
- Assuming protocol-level interoperability implies semantic compatibility.
- Omitting server identity, version, or authorization from traces.

## Follow-up Questions

- How do you revoke a compromised server?
- How do you prevent a tool result from becoming a privileged instruction?
- Would a direct internal API be simpler for this one integration?

## Senior-Level Discussion

MCP is an integration contract, not a governance layer. A platform should manage registry, approval, isolation, credentials, quotas, audit retention, and compatibility separately from protocol transport.

## Hands-on Exercise

Run the [minimal MCP server challenge](../../coding-challenges/04-mcp-server/README.md) and add a test that rejects an unknown method and an invalid argument.

## Related Topics

[Tool protocols](tool-protocols.md), [protocol comparison](protocol-comparison.md), [security](../production/security.md), [observability](../production/observability.md).
