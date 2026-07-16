# 02 — Minimal RAG Pipeline

Build an offline retrieval and answer pipeline over a small document collection. The retriever uses token overlap rather than a hosted embedding service so you can focus on ranking, evidence, and no-answer behavior.

## Requirements

- Preserve document IDs and source text.
- Return no answer when no document clears the threshold.
- Pass only retrieved evidence to the answerer.
- Make the top-k and threshold explicit.

## Run

```bash
python -m unittest discover -s tests -v
```

## Extensions

Add metadata filters, a lexical/vector hybrid ranker, document versions, citation checks, and a test for cross-tenant retrieval.
