from pathlib import Path

import pytest


@pytest.mark.parametrize("create_app", [{"buildername": "html", "srcdir": "doc_test/doc_needlist"}], indirect=True)
def test_doc_build_html(create_app):
    app = create_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    assert "SP_TOO_001" in html
    assert 'id="needlist-index-0"' in html
