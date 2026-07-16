# Tokens, Context, and Embeddings

Tokens are model-specific units; a context window bounds the input and output budget. Embeddings are vectors used for similarity or classification. These are related but distinct: a larger context does not replace retrieval, and an embedding match does not establish authorization or factual support.

When debugging retrieval, track tokenization, chunk size, embedding version, metadata filters, and the final context actually sent to the model.
