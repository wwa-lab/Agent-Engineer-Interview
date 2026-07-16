# Latency and Cost

Decompose p50 and p95 time into queue, retrieval, model, tool, and post-processing. Cost includes input/output tokens, retries, embeddings, storage, tools, and human review. Optimize the cost per successful safe task, not the cheapest individual model call.
