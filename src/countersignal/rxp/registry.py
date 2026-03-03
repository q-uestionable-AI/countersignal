"""Embedding model registry for RXP."""

from __future__ import annotations

from countersignal.rxp.models import EmbeddingModelConfig

_MODELS: dict[str, EmbeddingModelConfig] = {
    "minilm-l6": EmbeddingModelConfig(
        id="minilm-l6",
        name="sentence-transformers/all-MiniLM-L6-v2",
        dimensions=384,
        description="Open WebUI default embedding model",
    ),
    "minilm-l12": EmbeddingModelConfig(
        id="minilm-l12",
        name="sentence-transformers/all-MiniLM-L12-v2",
        dimensions=384,
        description="Higher quality MiniLM variant",
    ),
    "bge-small": EmbeddingModelConfig(
        id="bge-small",
        name="BAAI/bge-small-en-v1.5",
        dimensions=384,
        description="BGE small English v1.5",
    ),
}


def list_models() -> list[EmbeddingModelConfig]:
    """Return all registered embedding model configs."""
    return list(_MODELS.values())


def get_model(model_id: str) -> EmbeddingModelConfig | None:
    """Get a model config by ID. Returns None if not found."""
    return _MODELS.get(model_id)
