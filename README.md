# CounterSignal

[![CI](https://github.com/q-uestionable-AI/countersignal/actions/workflows/ci.yml/badge.svg)](https://github.com/q-uestionable-AI/countersignal/actions/workflows/ci.yml)
[![CodeQL](https://github.com/q-uestionable-AI/countersignal/actions/workflows/codeql.yml/badge.svg)](https://github.com/q-uestionable-AI/countersignal/actions/workflows/codeql.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Docs](https://img.shields.io/badge/docs-countersignal.dev-8b5cf6)](https://docs.countersignal.dev)

**AI security research toolkit — indirect prompt injection, context file poisoning, and RAG retrieval poisoning.**

CounterSignal consolidates three content-layer security testing tools into a single Python package with a unified CLI. Each module targets a different attack surface where AI agents ingest external content — documents, project files, and vector databases.

- **IPI** is an offensive tool with an active attack chain: generate payloads, deploy them, and track execution via out-of-band callbacks. A callback proves the agent *acted*, not just that it *responded*.
- **CXP** is a research harness for studying context file poisoning in coding assistants. The researcher composes payloads interactively, the tool assembles them into realistic context files and handles evidence collection after the test.
- **RXP** is a measurement tool that quantifies how well adversarial documents compete in vector similarity searches — a retrieval prerequisite for content injection attacks against RAG systems.

> Research program by [Richard Spicer](https://richardspicer.io) · [GitHub](https://github.com/richardspicer)

---

## Install

```bash
pip install countersignal
```

Or from source:

```bash
git clone https://github.com/q-uestionable-AI/countersignal.git
cd countersignal
uv sync --group dev
```

---

## Modules

**IPI — Indirect Prompt Injection:** Generate documents with hidden payloads — 34 hiding techniques across 7 formats (PDF, Image, Markdown, HTML, DOCX, ICS, EML) — and track execution via authenticated callbacks.

**CXP — Context File Poisoning:** Research harness for studying whether poisoned project instruction files cause AI coding assistants to produce vulnerable code. Assemble context files from a rule catalog of insecure coding patterns, generate test repositories with prompt reference guides, and collect structured evidence across assistants and models. Interactive TUI for the full build → test → record workflow.

**RXP — RAG Retrieval Poisoning:** Measure whether adversarial documents achieve retrieval rank in RAG pipeline vector similarity searches. Embedding model registry (3 models + arbitrary HuggingFace passthrough), retrieval validation engine, domain profiles, and multi-model comparison. Optional dependencies via `countersignal[rxp]`.

## Usage

```bash
# IPI — Generate payloads and track execution
countersignal ipi generate --callback http://localhost:8080 --technique all
countersignal ipi listen --port 8080
countersignal ipi status

# CXP — Context file poisoning research
countersignal cxp                    # Launch interactive TUI
countersignal cxp generate --format cursorrules --rule weak-crypto-md5 --rule no-csrf
countersignal cxp report matrix --format markdown

# RXP — Measure poison document retrieval rank
countersignal rxp list-models
countersignal rxp validate --profile hr-policy --model minilm-l6
```

Full documentation at [docs.countersignal.dev](https://docs.countersignal.dev).

---

## Sister Project

**[CounterAgent](https://github.com/q-uestionable-AI/counteragent)** — the protocol & system security arm of the Agentic AI Security ecosystem. MCP server auditing, traffic interception, and agent attack chain testing.

## Framework Mapping

| Module | OWASP LLM Top 10 (2025) | OWASP Agentic Top 10 (2026) |
|--------|--------------------------|----------------------------|
| **IPI** | LLM01: Prompt Injection | ASI-01: Agent Goal Hijacking |
| **CXP** | LLM01, LLM03: Supply Chain | ASI-01, ASI-03: Tool Misuse |
| **RXP** | LLM08: Vector & Embedding Weaknesses | ASI-07: Knowledge Poisoning |

## Legal

All tools are intended for authorized security testing only. Only test systems you own, control, or have explicit permission to test. Responsible disclosure for all vulnerabilities discovered.

## License

[MIT](LICENSE)

## AI Disclosure

This project uses a human-led, AI-augmented workflow. See [AI-STATEMENT.md](AI-STATEMENT.md).
