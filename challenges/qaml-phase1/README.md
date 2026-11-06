# Quantum Adversarial Machine Learning — Phase 1

Study image robustness in two quantum classifiers: an eight-qubit **QNN** and an
eight-qubit **QCNN**, both with angle encoding, classical heads, and noiseless
simulation. The four Road Signs classes are speed limit, crosswalk, physical
traffic light, and stop.

- **Attack a hardened model:** create bounded image perturbations, with
  white-box access or a metered black-box prediction API. Targeted and
  untargeted objectives are separate variants.
- **Defend an original model:** submit a reproducible, bounded adversarial
  training recipe. Organizers train and evaluate it using the fixed pipeline.

The image change limit is **8/255 in pixel L-infinity distance**, common to all
teams in a scored variant. Black-box predictions cost one query per image;
the served allowance is **273 queries per image per issued variant/run grant**.

Road Signs is a **public/exposed educational benchmark**, not a private holdout.
The QNN reference defense failed its scientific robustness gate. Its defense
challenge uses an explicitly approved educational scoring waiver, with scientific
diagnostics still shown. QCNN retains its existing gates. The two defense
leaderboards remain separate.

Participants receive rules, examples, the submission template, scoring details,
and approved assets through an independent private team repository. Checkpoint
and dataset distribution is pending the final release checks; this announcement
does not activate the challenge. No real traffic system or external target is involved.
