# Interview Preparation Plan

Use this plan when you have more than 30 days or want a repeatable cycle. Adjust the depth, not the order of feedback: concepts without implementation are fragile, and implementation without evaluation is hard to defend.

## Four phases

### 1. Baseline and vocabulary

Complete the [skill assessment](skill-assessment.md). Review LLM basics, structured output, tool calling, RAG, and the [agent loop](../agent-engineering/agent-loop.md). Your output is a one-page system glossary in your own words.

### 2. Build and measure

Complete two coding challenges. Add at least one negative test to each: malformed tool arguments, no retrieval match, stale memory, or an evaluator disagreement. Write down latency and cost assumptions even when the sample is offline.

### 3. Design and operate

Practice three system design cases. For each, cover authorization, retries, idempotency, traces, evaluation, rollback, and human escalation. Use the [system design framework](../system-design/system-design-framework.md) to keep answers comparable.

### 4. Communicate and simulate

Prepare a [project story](../job-search/project-storytelling.md), two resume bullets, and five behavioral stories. Run one timed mock interview per week. Ask a reviewer to interrupt with “why?”, “what fails?”, and “how do you know?”

## Weekly review questions

- What did I build that would fail under a different model or provider?
- Which metric would tell me that the change helped?
- What permission does each tool need, and what happens if its output is malicious?
- What is the cheapest safe fallback when the model, retrieval layer, or tool is unavailable?
- Which decision can I explain with evidence rather than preference?

## Final week

Reduce scope. Re-run the coding challenge tests, rehearse the project story in two minutes, and practice one system design question from a blank page. Do not add a new framework just to make the portfolio look broader.
