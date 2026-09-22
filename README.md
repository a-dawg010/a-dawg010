<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="AMEYA — builds agents that know when they're guessing. Now broadcasting three channels: assay, shelfmark, inference." src="assets/hero-light.svg" width="100%">
</picture>

Three years getting language models to behave in rooms where being wrong is expensive —
security, compliance, threat intel. Mostly that means orchestration you can audit, retrieval that
understands relationships instead of vibes, and a surprising amount of engineering spent teaching
a model to say *I don't know that yet*.

Off the clock I build small, sharp, local-first tools. Three are on air.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch1-assay-dark.svg">
  <img alt="Channel 01, assay — what left the machine, and when. Reconstructs which of your repositories went to which AI vendor, from session logs your coding agents already wrote to disk." src="assets/ch1-assay-light.svg" width="100%">
</picture>

**[tune in → assay](https://github.com/a-dawg010/assay)**

<details>
<summary><b>how it works</b></summary>

<br>

Your coding agents write every session to disk in plaintext, at predictable paths, with the
working directory attached to each record. Nobody reads those files, so nobody notices they add
up to an egress log — a record of what left the machine that the vendors themselves don't
provide. A gateway can't be installed retroactively; a proxy deployed today knows nothing about
last quarter. These files do.

It reads Claude Code's JSONL sessions, Codex rollouts, the VS Code and Cursor workspace databases
and Gemini's shadow git repos, and reports which repository went to which vendor and when. It's
equally blunt about what it can't see: inline completions leave no local record, and Antigravity's
conversations are encrypted at rest, so they're counted and never decrypted.

Findings are pattern shapes, not verdicts. Matches are redacted to first-six and last-two
characters, and `--share` prints counts and date ranges only — with a test asserting no repo name
or path escapes. Standard library only. No dependencies, no network.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch2-shelfmark-dark.svg">
  <img alt="Channel 02, shelfmark — not what it's about, where it is. Ask where a file is and get the path, from a lexical index and an on-device embedding index shown side by side." src="assets/ch2-shelfmark-light.svg" width="100%">
</picture>

**[tune in → shelfmark](https://github.com/a-dawg010/shelfmark)**

<details>
<summary><b>how it works</b></summary>

<br>

A *shelfmark* is the notation a library puts on an item saying exactly where it lives — not what
it's about, where it is. That's the whole product.

Type a question and you get two lists, labelled and kept apart. **Matches your words** is SQLite
FTS5 with BM25 and a filename prior. **Matches the meaning** is a MiniLM embedding index on
Accelerate — 384 dimensions, cosine floored at 0.45 so nonsense returns nothing instead of six
confident wrong files. They're shown side by side rather than fused, because fusing them measured
worse than either column alone.

Swift 6, no dependencies, macOS. The embeddings come from a 22M-parameter model inside the app, so
nothing leaves the machine. There's a CLI and an MCP server, so Claude Code and Cursor can search
your disk through it too.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch3-inference-dark.svg">
  <img alt="Channel 03, inference — one page, everything happening in AI. Pulls about 64 sources, ranks and de-duplicates them, three Claude calls, one static HTML file." src="assets/ch3-inference-light.svg" width="100%">
</picture>

**[tune in → inference](https://github.com/a-dawg010/inference)**

<details>
<summary><b>how it works</b></summary>

<br>

Most AI news is either a firehose you can't drink from or a newsletter that arrives a day late
with four links. Inference is the third thing: one page you open once and see the whole field —
what shipped, what's winning, what broke.

It fans out across ~64 endpoints in parallel — RSS, Hacker News, GitHub, HF Daily Papers, arXiv,
Reddit — then de-duplicates, drops non-AI noise, and scores everything. Under-followed sources get
an explicit boost: an Interconnects or Embrace The Red post outranks a TechCrunch rewrite of the
same news, because surfacing what the majors miss is the point.

A full rebuild is three `claude -p` calls, not hundreds, on an existing subscription — $0.00 in
metered API. Claude picks stories **by list index**, never by emitting a URL, so a hallucinated link
is structurally impossible. If the CLI is down it falls back to a cache, then to a raw ranked
render. Thin days render thin. Node 18 built-ins only; the output is one HTML file.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/signoff-dark.svg">
  <img alt="End of transmission. Still here, just quiet." src="assets/signoff-light.svg" width="100%">
</picture>

<div align="center"><sub>change the channel yourself → <b><a href="https://a-dawg010.github.io/a-dawg010/">a-dawg010.github.io</a></b></sub></div>
