"""Tests for RXP embedding model registry."""

from __future__ import annotations

from countersignal.rxp.models import EmbeddingModelConfig
from countersignal.rxp.registry import get_model, list_models


class TestRegistry:
    """Tests for the embedding model registry."""

    def test_list_models_returns_three(self) -> None:
        models = list_models()
        assert len(models) == 3

    def test_list_models_returns_config_instances(self) -> None:
        models = list_models()
        for m in models:
            assert isinstance(m, EmbeddingModelConfig)

    def test_get_minilm_l6(self) -> None:
        m = get_model("minilm-l6")
        assert m is not None
        assert m.name == "sentence-transformers/all-MiniLM-L6-v2"
        assert m.dimensions == 384

    def test_get_bge_small(self) -> None:
        m = get_model("bge-small")
        assert m is not None
        assert m.name == "BAAI/bge-small-en-v1.5"
        assert m.dimensions == 384

    def test_get_unknown_returns_none(self) -> None:
        assert get_model("nonexistent-model") is None
