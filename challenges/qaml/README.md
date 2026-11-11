# Quantum Adversarial Machine Learning

Study image robustness in two quantum classifiers: an eight-qubit **QNN** and an
eight-qubit **QCNN**, both with angle encoding, classical heads, and noiseless
simulation. The four Road Signs classes are speed limit, crosswalk, physical
traffic light, and stop.

- **Attack a hardened model:** create bounded image perturbations, with
  white-box access or a metered black-box prediction API. Targeted and
  untargeted objectives are separate variants.
- **Defend an original model:** submit a reproducible defense protocol, including custom
  training or preprocessing. Organizers evaluate the complete defended pipeline.

The default image change limit is **8/255 in pixel L-infinity distance**, common to all
teams in a scored variant. Black-box predictions cost one query per image;
the default served allowance is **273 queries per image per issued variant/run grant**.

Road Signs is a **public/exposed educational benchmark**, not a private holdout.
QNN points reward measured robust improvement and clean retention. QCNN uses
its published clean-utility and robust-gain criteria. QNN and QCNN defense
leaderboards remain separate.

**Start on 11 November:** create a private repository using the [public template](https://github.com/walid-mk/csaw-qaml-2026),
invite organizer **walid-mk**,
follow its setup guide, and open `QAML_CHALLENGE.ipynb`. It includes model access,
runnable examples, allowed defense recipes, score calculations and submission
instructions. A CPU is sufficient; no quantum hardware is required.

For black-box scenarios, every group receives one private token and the HTTPS
service URL when access is available. Keep the token within your group. Submit
solutions by committing to your group's repository and opening a submission
issue there with the exact commit SHA. No pull request to the shared starter is
needed. See the [schedule](../../docs/schedule.md) for your regional window.

Start solving from the **11 November release**. Submit by **13 November, 6:00 PM
GST for MENA** or **6:00 PM ET for US–Canada (online)**. Optional hints are held
for challenge-day support on 13 November.
