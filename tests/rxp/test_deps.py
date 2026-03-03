"""Tests for RXP dependency guard."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from countersignal.rxp._deps import _RXP_INSTALL_MSG, require_rxp_deps


class TestDepsGuard:
    """Tests for the RXP dependency guard."""

    def test_require_rxp_deps_missing(self) -> None:
        """Simulated missing import raises ImportError with install message."""
        with patch.dict("sys.modules", {"chromadb": None}):
            with pytest.raises(ImportError, match="pip install countersignal"):
                require_rxp_deps()

    def test_install_message_content(self) -> None:
        assert "pip install countersignal[rxp]" in _RXP_INSTALL_MSG
        assert "uv sync --extra rxp" in _RXP_INSTALL_MSG
