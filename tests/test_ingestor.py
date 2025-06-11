import tempfile
import shutil
from pathlib import Path
from sourcebot.ingestor import DocumentIngestor

def test_load_local_txt():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "sample.txt"
        file_path.write_text("Hello test world!", encoding="utf-8")

        ingestor = DocumentIngestor(tmpdir)
        docs = ingestor.load_docs()
        assert len(docs) == 1
        assert "Hello test world!" in docs[0]

