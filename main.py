"""Entry for the Absurd Micro-Startup Pitch-Off.

Writes a single-sentence pitch for an absurdly specific micro-startup
for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
v2: narrower niche, named buyer, explicit guardrail, set-and-forget loop;
v2b trims the meeting clause to fit the 200-character gate.
v3: folds the guardrail into the payoff clause, cutting the redundancy
between the keep-clause and the ending, and drops the monthly qualifier.
v4: sharpens the humour turn by framing the agent's own refusal to
attend as the selling point, keeping niche, buyer, price and payoff.
"""

import os

PITCH = "NoAgenda: a $3-per-agent service where a lazy AI agent auto-declines no-agenda recurring status meetings for solo founders, it won't sit through them either, so founders meet only paying clients."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
