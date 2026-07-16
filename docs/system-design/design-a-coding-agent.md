# Design a Coding Agent

## Prompt

Design an agent that can inspect a repository, propose a change, run tests, and prepare a patch while keeping the developer in control.

## Assumptions

Start with one repository per run, a 10-minute interactive budget, read access by default, and explicit approval before writes or commands with side effects.

## Architecture

```text
IDE/CLI -> gateway -> run store + policy engine
                    -> orchestrator -> model
                                  -> read sandbox
                                  -> test sandbox
                                  -> approval-gated patch writer
```

The sandbox pins a workspace snapshot, limits network access, caps output, and records commands. The context builder selects relevant files and test results rather than sending the whole repository. The orchestrator keeps a step budget and can return a plan without executing it.

## Key trade-offs

- Running tests in an isolated container is safer but slower than a local process.
- Full-repository context is simple but expensive and may leak unrelated secrets; indexed retrieval is faster after setup but can miss dependencies.
- Automatic patch application is convenient; approval before mutation preserves user control and makes incident recovery easier.

## Failure and evaluation

Evaluate patch correctness, test preservation, scope of change, secret exposure, and whether the agent stops when it lacks evidence. Include malicious repository instructions and flaky tests in the dataset. Trace model decisions, tool calls, commands, approvals, and final diff hashes.
