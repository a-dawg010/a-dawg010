<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Ameya Panse — AI engineer, Pune. I build agents that know when they're guessing." src="assets/hero-light.svg" width="100%">
</picture>

Three years teaching language models to behave in rooms where being wrong is expensive —
automotive security, compliance, threat intel. In practice that means orchestration you can
audit, retrieval that understands relationships instead of vibes, and a surprising amount of
engineering dedicated to making a model say *I don't know that yet*.

The rest of the time I build small sharp tools for problems that annoy me.

<br>

## two of those

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/assay-dark.svg">
  <img alt="assay — your agents are hoarders. Scans the machine for what Claude Code, Cursor, Codex and Antigravity left behind and reports what you can reclaim." src="assets/assay-light.svg" width="100%">
</picture>

**[github.com/a-dawg010/assay →](https://github.com/a-dawg010/assay)**

<details>
<summary><b>how it works</b></summary>

<br>

Coding agents are messy guests. They spin up scratch directories, half-finished checkouts,
dependency caches and whole VMs, and then the session ends and nobody remembers any of it existed.
Six months later you are out sixty gigabytes and you have no idea why.

`assay` walks the filesystem looking for the fingerprints each harness leaves — directory shapes,
lockfile patterns, VM disk images, orphaned caches — attributes each find to the agent that made it,
and sorts by what you would actually get back. Nothing is deleted without you saying so; the whole
point is a list you can read, not a cleaner that surprises you.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/shelfmark-dark.svg">
  <img alt="shelfmark — talk to your storage. Ask your drive a question in plain English and get the file back." src="assets/shelfmark-light.svg" width="100%">
</picture>

**[github.com/a-dawg010/shelfmark →](https://github.com/a-dawg010/shelfmark)**

<details>
<summary><b>how it works</b></summary>

<br>

Search on your own machine is still filename matching wearing a nicer coat. You know what the
document *said*; you do not remember what you called it or which of four folders it ended up in.

`shelfmark` indexes content rather than names — text, documents, the readable parts of what you
already have — and answers a question in plain English with the file itself. No folder tree to
walk, no page of results ranked by how closely a filename matched. Ask the way you'd ask a person
who had read all of it.

</details>

<br>

---

<sub>more, and it moves: **[a-dawg010.github.io](https://a-dawg010.github.io/a-dawg010/)** &nbsp;·&nbsp; no analytics on this page, no newsletter, the worm is load-bearing</sub>
