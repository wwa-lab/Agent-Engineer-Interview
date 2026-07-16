"""Offline RAG components that keep evidence explicit."""

from dataclasses import dataclass
import re
from typing import Callable


@dataclass(frozen=True)
class Document:
    document_id: str
    text: str


def _terms(text: str) -> frozenset[str]:
    return frozenset(re.findall(r"[a-z0-9]+", text.lower()))


class InMemoryRetriever:
    def __init__(self, documents: list[Document]) -> None:
        self._documents = tuple(documents)

    def search(self, query: str, top_k: int = 3, threshold: float = 0.1) -> tuple[Document, ...]:
        query_terms = _terms(query)
        if not query_terms:
            return ()
        scored = []
        for document in self._documents:
            score = len(query_terms & _terms(document.text)) / len(query_terms)
            if score >= threshold:
                scored.append((score, document.document_id, document))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return tuple(document for _, _, document in scored[:top_k])


class RagPipeline:
    def __init__(self, documents: list[Document], answerer: Callable[[str, tuple[Document, ...]], str], top_k: int = 3, threshold: float = 0.1) -> None:
        self._retriever = InMemoryRetriever(documents)
        self._answerer = answerer
        self._top_k = top_k
        self._threshold = threshold

    def answer(self, query: str) -> str:
        evidence = self._retriever.search(query, self._top_k, self._threshold)
        if not evidence:
            return "I do not have enough evidence to answer that."
        return self._answerer(query, evidence)
