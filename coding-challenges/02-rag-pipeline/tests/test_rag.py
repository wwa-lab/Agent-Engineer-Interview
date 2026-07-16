import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from solution.rag import Document, InMemoryRetriever, RagPipeline


class RagTests(unittest.TestCase):
    def setUp(self) -> None:
        self.documents = [
            Document("refund", "A refund is available within thirty days with approval."),
            Document("shipping", "Standard shipping takes five business days."),
        ]

    def test_retriever_returns_relevant_documents_in_stable_order(self) -> None:
        results = InMemoryRetriever(self.documents).search("refund approval")

        self.assertEqual([document.document_id for document in results], ["refund"])

    def test_pipeline_passes_only_evidence_to_answerer(self) -> None:
        seen: list[tuple[Document, ...]] = []
        pipeline = RagPipeline(self.documents, lambda _, evidence: (seen.append(evidence) or evidence[0].text))

        self.assertIn("thirty days", pipeline.answer("refund"))
        self.assertEqual([document.document_id for document in seen[0]], ["refund"])

    def test_empty_retrieval_abstains(self) -> None:
        pipeline = RagPipeline(self.documents, lambda *_: "unsafe")

        self.assertIn("not have enough evidence", pipeline.answer("quantum"))

    def test_empty_query_does_not_retrieve_everything(self) -> None:
        self.assertEqual(InMemoryRetriever(self.documents).search(""), ())


if __name__ == "__main__":
    unittest.main()
