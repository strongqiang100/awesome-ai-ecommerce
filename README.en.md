<div align="center">

# Awesome AI Ecommerce

### From one repeatable action to a dependable operating system

**Give every tool a purpose, every fact a source, and every action a measurable result.**

[简体中文](README.md) · English

[Read the handbook](docs/en/handbook.md) · [Explore tools](docs/tools.md) · [Integrate APIs](docs/integrations.md) · [Run examples](examples/README.md)

</div>

---

A bilingual starting point for cross-border sellers, independent stores, brand teams, and developers. Covers product research, product truth, listings, images, video, creators, advertising, support, inventory, fulfillment, and analytics, together with data contracts, agents, reliability, evaluation, and open research boundaries.

> Let systems carry repetition. Let evidence guide judgment.

## Find your path

| Your question | Start here | What you will find |
|---|---|---|
| How does ecommerce automation work? | [Chapters 01–03](docs/en/handbook.md#c01) | Tasks, architecture, and data contracts |
| How do I investigate products? | [Chapters 04–06](docs/en/handbook.md#c04) | Selection, reviews, costs, and facts |
| How do I create listings and media? | [Chapters 07–09](docs/en/handbook.md#c07) | Localization, fidelity, and video |
| How do I organize acquisition? | [Chapters 10–11](docs/en/handbook.md#c10) | Partnerships, diagnosis, and experiments |
| How do I improve service and fulfillment? | [Chapters 12–14](docs/en/handbook.md#c12) | Retrieval, orders, stock, and retention |
| How do I build dependable integrations? | [Chapters 15–18](docs/en/handbook.md#c15) | APIs, agents, evaluation, and cost |
| Is there a comparable workflow? | [24 recipes](docs/en/handbook.md#c20) | Inputs, candidate tools, and acceptance |
| What remains unproven? | [Research boundaries](docs/en/handbook.md#c19) | Hypotheses, validation, and stopping rules |

## Repository map

```text
.
├── README.md / README.en.md      Language entry points
├── docs/
│   ├── zh-CN/handbook.md         Chinese long-form guide
│   ├── en/handbook.md            Corresponding English edition
│   ├── tools.md                 Bilingual selection catalog
│   ├── integrations.md          Platforms and Chuhaijiang
│   └── sources.md               Sources, evidence, and dates
├── examples/                    Synthetic offline demonstrations
├── ai-ecommerce-news-workflow.json  Manual n8n demonstration
├── tests/                       Boundary tests
├── scripts/check_repo.py         Links, structure, and publication checks
├── CONTRIBUTING.md              Bilingual contribution rules
├── SECURITY.md                  Data and security guidance
└── .github/                     Checks and issue templates
```

## Evidence levels

| Label | Meaning |
|---|---|
| **LIVE** | A real query succeeded within the stated date and scope; not comprehensive validation |
| **DOC** | Capability confirmed in official documentation; no end-to-end test |
| **DEMO** | Offline synthetic example without production connections |
| **DESIGN** | Reference design with inputs, steps, and acceptance criteria |
| **RESEARCH** | Unvalidated hypothesis with reasoning and implementation ideas |

Inclusion is not paid endorsement or a claim that every tool was tested. Consult current official terms for prices, quotas, versions, regions, permissions, and licensing. [Evidence and sources](docs/sources.md).

## Understand a small loop in ten minutes

Requires Python 3.10+. These commands do not use the network, send messages, or operate stores.

```bash
python3 examples/research_pipeline.py
python3 examples/unit_economics.py
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
```

The first example normalizes product records and detects duplicate records. The second calculates contribution for a synthetic order. See the [example notes](examples/README.md) for connecting models and platforms.

The [n8n JSON](ai-ecommerce-news-workflow.json) uses manual execution and synthetic news to deduplicate items and prepare a review draft. **JSON, graph structure, and code logic have been checked; live n8n import has not.** Read the [configuration notes](examples/README.md#n8n) before adding RSS, models, or delivery channels.

## Principles

- **Facts before expression.** Ground product claims, prices, and policies.
- **Feedback before scale.** Observe a real result before increasing volume.
- **Rules constrain models.** Enforce arithmetic, permissions, and money boundaries deterministically.
- **Keep uncertainty visible.** Fluent text does not replace evidence.
- **Human involvement is architecture.** Preserve review, exception handling, and stopping.

## Contribute and maintain

Contribute reproducible scenarios, tool limitations, sources, and failure cases. Read [contribution rules](CONTRIBUTING.md) and [security guidance](SECURITY.md). Main guides have corresponding chapters; shared tool, integration, and maintenance documents are bilingual.

Evidence reviewed: **2026-09-23**. Repository code and documentation retain the [MIT license](LICENSE). Third-party tools, models, data, and assets retain their own terms.
