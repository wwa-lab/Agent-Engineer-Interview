# Design a RAG Assistant

In a support or internal-knowledge setting, start with tenant-aware ingestion, structure-aware chunks, metadata filters, hybrid retrieval, optional reranking, context assembly, answer generation, and citations. Define a no-answer threshold and a freshness signal. The most important trade-off is recall versus context cost; the most dangerous failure is retrieving data the user is not allowed to see.
