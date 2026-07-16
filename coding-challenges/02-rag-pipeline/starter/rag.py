"""Starter surface for the RAG challenge."""

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Document:
    document_id: str
    text: str


class RagPipeline:
    def __init__(self, documents: list[Document], answerer: Callable[[str, tuple[Document, ...]], str]) -> None:
        raise NotImplementedError

    def answer(self, query: str) -> str:
        raise NotImplementedError
