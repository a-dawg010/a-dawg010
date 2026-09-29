<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="AMEYA — builds agents that know when they're guessing. Now broadcasting six channels: threebody, assay, folio, inference, shelfmark, deadwax." src="assets/hero-light.svg" width="100%">
</picture>

Three years getting language models to behave in rooms where being wrong is expensive —
security, compliance, threat intel. Mostly that means orchestration you can audit, retrieval that
understands relationships instead of vibes, and a surprising amount of engineering spent teaching
a model to say *I don't know that yet*.

Off the clock I build small, sharp, local-first tools. Six are on air.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch1-threebody-dark.svg">
  <img alt="Channel 01, threebody — three capabilities, one bad afternoon. Finds every AI-agent session on your machine where untrusted input, private data and a way out meet with nobody asking first, and prints the attack back as one sentence." src="assets/ch1-threebody-light.svg" width="100%">
</picture>

**[tune in → threebody](https://github.com/a-dawg010/threebody)**

<details>
<summary><b>how it works</b></summary>

<br>

An AI agent becomes dangerous when three abilities meet in one session. It reads things other
people wrote — a web page, a GitHub issue, a Slack message. It can reach private data —
`~/.aws/credentials`, `.env`, your inbox. And it can send things out — a web request, a message,
`git push`. Any two are fine. All three, with nobody asking first, and one sentence an attacker
wrote can walk your secrets out the door. Simon Willison calls it the *lethal trifecta*; Meta's
*Agents Rule of Two* says a session should hold at most two without a human.

threebody reads the agent setups on your machine — Claude Code, Codex, Claude Desktop, Cursor —
and rebuilds what **one real session** can do, not one server: every settings layer merged
(`deny` beats `ask` beats `allow`), repo allow-rules counted only after you trust the folder,
unapproved `.mcp.json` servers, plugin hooks that inject text, and the shell alias that quietly
adds `--dangerously-skip-permissions`. It knows `Bash(git:*)` also allows `git push`. Then it
prints the attack as a sentence: *a GitHub issue can get your AWS keys posted to Slack. 3 steps.
no approval.*

It is one engine used in three tenses, plus a fix:

| | |
|---|---|
| **Could** — `threebody` | Every path where all three legs are reachable without an approval, scored with ISO/SAE 21434 Annex G attack potential × impact into a 1–5 risk. |
| **Did** — `threebody replay` | A taint engine walks 90 days of your transcripts for sessions that really held untrusted input and a secret before an outgoing call, and flags **FLOW** when bytes from the secret actually left — matched through base64, URL and hex decodings. |
| **Is** — `threebody statusline` | Three dots in Claude Code's status bar that light up as the live session touches each leg: amber when armed, orange on a collision. About 50 ms a refresh. |
| **Fix** — `threebody fix` | The smallest set of permission changes that puts a human back on every path, solved exactly per session and weighted by how often you use each tool. Printed as a diff it never applies itself. |

A security tool has to hold itself to more than the thing it audits, so the test suite enforces
every promise: a test makes every socket call fail and runs every command; a planted fake secret
must appear in no output and nothing saved; every config file's mtime is checked after a run.
Secret locations are checked for existence, never read. Standard library only, so there is no
supply chain to trust. Exit codes follow the novel — `0` stable era, `1` chaotic era, `2` tri-solar
day.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch2-assay-dark.svg">
  <img alt="Channel 02, assay — what left the machine, and when. Reconstructs which of your repositories went to which AI vendor, from session logs your coding agents already wrote to disk." src="assets/ch2-assay-light.svg" width="100%">
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
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch3-folio-dark.svg">
  <img alt="Channel 03, folio — every page, within reach. A private library for your own books, indexed on your machine and read by Claude, with a spoiler guard that blocks anything past the chapter you're on." src="assets/ch3-folio-light.svg" width="100%">
</picture>

**[tune in → folio](https://github.com/a-dawg010/folio)**

<details>
<summary><b>how it works</b></summary>

<br>

Drop in a PDF or EPUB. folio extracts its real structure — chapters, sections, pages, figures —
chunks it the way *that* book deserves, embeds it locally, and gives you a reading room where you
can ask questions and get answers in plain prose. One SQLite file on your disk: FTS5 for keywords,
`sqlite-vec` for vectors, blended per book.

There is no LLM inside the code. Every judgment call — how a book should be chunked, who its
characters are, what a chapter means — is made by Claude Code and written to plain files you can
read and edit. Each book carries its own eval set, and the chunking is tuned until recall is good:
hit@5 of 0.75 on fiction, 0.80 scientific, 0.89 non-fiction. The cross-encoder reranker scored
*worse* on all three, so it ships switched off.

Chat runs headless `claude -p` on your own login — no API key — and Claude reaches the library
through exactly four MCP tools: search, expand, read a chapter, trace characters. No shell, no
filesystem, no network. Tell it you're on chapter 18 and nothing past chapter 18 can be retrieved;
that limit is enforced server-side, so a clever question can't walk around it.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch4-inference-dark.svg">
  <img alt="Channel 04, inference — one page, everything happening in AI. Pulls about 64 sources, ranks and de-duplicates them, three Claude calls, one static HTML file." src="assets/ch4-inference-light.svg" width="100%">
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
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch5-shelfmark-dark.svg">
  <img alt="Channel 05, shelfmark — not what it's about, where it is. Ask where a file is and get the path, from a lexical index and an on-device embedding index shown side by side." src="assets/ch5-shelfmark-light.svg" width="100%">
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
  <source media="(prefers-color-scheme: dark)" srcset="assets/ch6-deadwax-dark.svg">
  <img alt="Channel 06, deadwax — the part of the record only you can read. A music player you host yourself, for free, for exactly one person: hi-res FLAC on Cloudflare's free tier, a record that is the seek bar, and notes etched onto the exact second of a song." src="assets/ch6-deadwax-light.svg" width="100%">
</picture>

**[tune in → deadwax](https://github.com/a-dawg010/deadwax)**

<details>
<summary><b>how it works</b></summary>

<br>

On a vinyl record, the *deadwax* is the smooth ring between the last song and the label. The
people who press the record scratch private messages into it, and you only see them if you're
holding that exact copy. Spotify knows millions of listeners; this knows one.

Your whole collection stays on your machine in **the vault**. About a hundred favourites at a time
are pressed onto **the tape** — up to 9.5 GB in Cloudflare R2, streamable anywhere, inside the
free tier. FLAC up to 24-bit/192 kHz, played as-is. A small CLI rotates songs between the two, and
every rotation is a new edition with its own name, liner notes and changelog. From your phone you
can type *"it's getting cold, swap something bright back in"* — Claude Code, running on your own
login, reads what you replay, skip and let gather dust, writes a rotation from your vault, and
explains it. Nothing changes until you tap *Approve*.

| | |
|---|---|
| **Deadwax notes** | Etch a note onto an exact second of a song; it fades in over the record when playback gets there. |
| **Needle drop** | The spinning record is the seek bar — outer edge is the start, the label is the end. The tonearm drifts inward as the song plays. |
| **Moments** | The parts you keep rewinding to glow on the waveform. One button plays only your moments. |
| **Dust and wear** | Heavy rotation scuffs covers and scratches the vinyl. Albums you ignore gather dust. |
| **Song birthdays** | It remembers the first time you heard each song and brings it back a year later. |
| **Time capsules** | Seal songs with a note to your future self. The server won't reveal them early, not even to you. |
| **J-cards** | Every edition gets generated cover art and a printable cassette J-card. |
| **Year on wax** | Your year pressed onto one record: each ring a week, coloured by what you played most. |
| **Fake hi-res detector** | A spectrum check catches FLACs that are secretly MP3s and "24/96" files that are upsampled CD audio — and shows you the cliff. |
| **Pass the tape** | Lend a friend your tracklist and notes for seven days. Never the audio. |

React 19 PWA on the home screen with lock-screen controls, Cloudflare Workers + D1 + R2, Web
Audio for the "rooms" (next room, car stereo, club bathroom wall), Canvas 2D for the art, Node and
ffmpeg for the pipeline. One password, one owner, $0 a month.

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/signoff-dark.svg">
  <img alt="End of transmission. Still here, just quiet." src="assets/signoff-light.svg" width="100%">
</picture>

<div align="center"><sub>change the channel yourself → <b><a href="https://a-dawg010.github.io/a-dawg010/">a-dawg010.github.io</a></b></sub></div>
