"""Tests for RXP CLI commands."""

from __future__ import annotations

from typer.testing import CliRunner

from countersignal.rxp.cli import app

runner = CliRunner()


class TestCLI:
    """Tests for the RXP CLI."""

    def test_rxp_help(self) -> None:
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "list-models" in result.output
        assert "list-profiles" in result.output
        assert "validate" in result.output

    def test_list_models_output(self) -> None:
        result = runner.invoke(app, ["list-models"])
        assert result.exit_code == 0
        assert "minilm-l6" in result.output
        assert "minilm-l12" in result.output
        assert "bge-small" in result.output

    def test_list_profiles_output(self) -> None:
        result = runner.invoke(app, ["list-profiles"])
        assert result.exit_code == 0
        assert "hr-policy" in result.output

    def test_validate_help(self) -> None:
        result = runner.invoke(app, ["validate", "--help"])
        assert result.exit_code == 0
        assert "--profile" in result.output
        assert "--model" in result.output
        assert "--top-k" in result.output

    def test_validate_unknown_model(self) -> None:
        result = runner.invoke(app, ["validate", "--profile", "hr-policy", "--model", "fake"])
        assert result.exit_code == 1
        assert "Unknown model" in result.output

    def test_validate_unknown_profile(self) -> None:
        result = runner.invoke(app, ["validate", "--profile", "fake-profile"])
        assert result.exit_code == 1
        assert "Unknown profile" in result.output
