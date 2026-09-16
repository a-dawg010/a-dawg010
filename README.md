<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Ameya Panse — AI engineer. A query enters an orchestrator, routes through specialist sub-agents, and resolves into a grounded answer." src="assets/hero-light.svg" width="100%">
</picture>

<br>

<a href="https://a-dawg010.github.io/a-dawg010/"><b>▸&nbsp; OPEN THE LIVE SYSTEM MAP</b></a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="docs/resume.pdf">Résumé</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/ameya-p-453abb106/">LinkedIn</a>
&nbsp;&nbsp;·&nbsp;&nbsp;
<a href="mailto:ameypanse786@gmail.com">Email</a>

</div>

---

Most LLM demos are impressive exactly once. I build the other kind — systems that still hold up on
the hundredth query, in a domain where a confident wrong answer ends up as a finding in someone's
audit. In practice that means orchestration you can reason about, retrieval that knows how two facts
are connected, and output you can trace back to a clause.

<br>

## Retrieval that knows the relationships

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/graph-dark.svg">
  <img alt="A cybersecurity knowledge graph assembling — threats linked to assets linked to mitigations — then a traversal from CAN injection through the CAN bus and brake ECU to a message-authentication mitigation." src="assets/graph-light.svg" width="100%">
</picture>

> A vector index can tell you that a document mentions the telematics ECU. It cannot tell you that
> the brake ECU sits two hops downstream of it. That distance is usually the entire answer.

<details>
<summary><b>Why a graph rather than a flat index</b></summary>

<br>

The corpus here is an automotive cybersecurity ontology — threats, assets, mitigations, clauses,
CVEs — and almost every real question is about the **edges**, not the nodes:

- *reachability* — which safety-relevant assets can an attacker touch, and in how many hops
- *coverage* — which threats in the ontology have no mitigation attached
- *evidence* — which ISO/SAE 21434 clause does this artefact actually satisfy

Neo4j holds the ontology; Cypher does variable-length traversal; FAISS covers the unstructured
remainder where there is no useful structure to exploit. Results are re-ranked together and
returned with citations, so a reviewer can follow the path the system took rather than trusting it.

Built at SecureThings, extended at Arkcore into a domain RAG pipeline serving threat analysis,
compliance evidence validation and TARA gap detection.

</details>

<br>

## Orchestration, not one big prompt

The hero above is a real architecture, not a decoration. A query is classified before anything
executes; the router picks a sub-agent and a data source and applies guardrails; each sub-agent owns
one responsibility and hands off explicitly; synthesis reconciles what comes back and refuses to
paper over disagreement.

<details>
<summary><b>What each sub-agent is responsible for</b></summary>

<br>

| Sub-agent | Owns | Backed by |
|---|---|---|
| **Router** | intent classification, tool/data-source selection, guardrails | LangGraph |
| **Retrieval** | relationship-aware lookup, re-ranking, citation | Neo4j · Cypher · FAISS |
| **Threat analysis** | attack-path traversal, reachability scoring | MITRE ATT&CK · EMB3D |
| **Compliance** | clause-wise evidence validation, TARA gap analysis | ISO/SAE 21434 · UNECE R155 |
| **Extraction** | assets, threats, CVEs and vectors out of unstructured text | CRF NER + domain features |
| **Synthesis** | reconciliation, conflict resolution, grounded answer | LLM APIs |

The extraction model is a conditional random field with hand-built domain features rather than an
off-the-shelf NER — security entities are exactly the ones a general model gets wrong.

</details>

<br>

## The stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Technical stack by layer — agents, retrieval, models, service, data, domain, languages." src="assets/stack-light.svg" width="100%">
</picture>

<br>

## Where this came from

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">
  <img alt="Career timeline — SecureThings intern and associate engineer, founding engineer at Arkcore, AI engineer at Equations Work." src="assets/timeline-light.svg" width="100%">
</picture>

<details>
<summary><b>What shipped at each stop</b></summary>

<br>

**Equations Work** · AI Engineer · Apr 2026 → now<br>
Specialised sub-agents for an enterprise agentic-AI engagement with a global manufacturing client —
decomposing and routing complex queries so multi-step requests resolve reliably. Designed the
orchestration layer itself: responsibilities, hand-off logic, guardrails. Also a data pipeline over
large volumes of operational data, pairing data science with agentic AI to surface findings.

**Arkcore** · Founding Engineer · Jan 2025 – Mar 2026<br>
Owned LLM-powered systems on AWS end to end — architecture through deployment — for intelligent data
processing, threat analysis and automated decision-making. Built the multi-agent frameworks behind
threat intelligence, compliance mapping and incident correlation, and the domain RAG pipeline that
made cybersecurity knowledge querying accurate enough to rely on. Worked directly with clients on
constraints that decide the design: data availability, latency budgets, token cost, integration.

**SecureThings** · Associate Software Engineer / Engineering Intern · Jan 2023 – Dec 2024<br>
The custom CRF NER model. The Neo4j knowledge graph and the RAG pipeline over it. An ISO/SAE 21434
compliance assistant that validates evidence, finds gaps and generates clause-wise reports assessors
accept. A TARA gap analysis tool that flags missing threats, assets and mitigations before a risk
assessment reaches the OEM.

**MSc Scientific Computing** · Savitribai Phule Pune University · 2023 · GPA 9.45 / 10

</details>

<br>

## Elsewhere

**[▸ The live system map](https://a-dawg010.github.io/a-dawg010/)** — the interactive version of the
hero. Drag the graph apart, run one of four queries, and watch it route through the sub-agents and
traverse the ontology with a live trace.

**[assay](https://github.com/a-dawg010/assay)** &nbsp;·&nbsp; **[shelfmark](https://github.com/a-dawg010/shelfmark)**

<details>
<summary><b>How this page is built</b></summary>

<br>

Every moving thing here is a hand-authored SVG with SMIL and CSS keyframes inside it — no badge
services, no stat generators, no JavaScript (GitHub strips it). Sources live in `assets/src/`, one
file per panel, and `build.py` renders each into a light and a dark variant that `<picture>` selects
between. `preview.html` renders all of them side by side at desktop and phone width.

Full notes: [`docs/ASSETS.md`](docs/ASSETS.md).

</details>

---

<div align="center">
<sub>Open to interesting conversations — agentic systems, retrieval infrastructure, security tooling.<br>
<a href="mailto:ameypanse786@gmail.com">ameypanse786@gmail.com</a> · Pune, India</sub>
</div>
