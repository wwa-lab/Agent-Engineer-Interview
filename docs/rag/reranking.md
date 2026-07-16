# Reranking

Reranking applies a more expensive relevance model or rule after candidate retrieval. It can improve precision at small k but adds latency and may amplify bias in the candidate set. Log candidate and final ranks so regressions are diagnosable.
