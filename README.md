[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/mfahmiq/fortune-cookie-engineers/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/mfahmiq/fortune-cookie-engineers/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

# Fortune Cookie Funnies for Engineers

The funniest one-line fortune cookie message for a software engineer:

> You will ship on Friday, and the bug will wait until Monday to introduce itself.

80 characters. The setup is the prophecy every engineer dreads — the Friday deploy — and the twist is a bug with manners: it does not crash the release, it politely waits out the weekend and introduces itself on Monday, when everyone is back. The funniest word sits at the end, and the line is a genuine fortune-cookie prophecy rather than a slogan about engineering.

## How it was chosen

Sixteen candidate lines were written across different angles (deploys, code review, legacy code, cache, passwords, standups, regex, on-call, pull requests), then run through an internal pairwise tournament judged against the published judge brief in weight order — fortune-cookie-for-an-engineer first, then first-read punchline, fortune-cookie sound, freshness, and tightness. The champion beat the runner-up, "Your next bug hides in the one line you swore you did not touch.", in the final: the personified bug waiting until Monday is fresher, sounds more like a fortune-cookie prophecy, and lands its punchline on the last word.

## How to run

```sh
python3 main.py
```

This writes the fortune verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
