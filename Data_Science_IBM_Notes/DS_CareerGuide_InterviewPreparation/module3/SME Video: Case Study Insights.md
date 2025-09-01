# Expert Viewpoints: Case Study Insights

**Goal of the video:** Understand what interviewers want to see in a case study round, how to reason through a problem, and how to communicate your approach clearly.

---

## What Interviewers Are Looking For
- **Business thinking first:** Can you restate the business problem, define the hypothesis, and keep an **end outcome** in mind (impact, users, KPIs)?
- **Clarifying questions:** Do you slow down, ask for requirements/constraints, and confirm success criteria before jumping to solutions?
- **Structured reasoning:** Can you form reasonable **assumptions**, pick a **methodology**, and articulate **trade-offs**?
- **ML lifecycle awareness:** Data construction → transformations → modeling → validation → **deployment + monitoring** (drift, performance).
- **Thinking out loud:** Walk your logic step by step so the interviewer can follow how you’d operate on the job.

---

## A Simple, Reusable Framework (for DS Case Studies)

1. **Clarify & Reframe**
   - Business objective / target question
   - User & stakeholder needs
   - Success metrics (primary & guardrails)
   - Scope, timeline, constraints (data, compute, privacy)

2. **Form a Hypothesis & Plan**
   - Hypothesis for causality/behavior
   - Key drivers you expect to matter (with assumptions)
   - Experimental or analytical approach (A/B test? modeling? EDA?)

3. **Data Strategy**
   - **Construct the dataset:** sources, grain, keys, time windows
   - **Transformations:** cleaning, feature engineering, leakage avoidance
   - **Quality checks:** missingness, outliers, bias, sampling

4. **Method & Modeling**
   - Baseline (heuristic / simple model) for comparison
   - Candidate models (why these?), evaluation plan, cross-validation
   - Regularization / hyperparameters; interpretability vs accuracy trade-off

5. **Evaluate & Decide**
   - Metrics tied to the business KPI (e.g., uplift, cost-sensitive metrics)
   - Error analysis, bias/fairness checks, robustness tests
   - “What would change my mind?” (decision thresholds)

6. **Ship & Monitor**
   - Deployment plan (batch vs real-time)
   - **Monitoring:** data drift, performance decay, alerting, retraining cadence
   - Feedback loop with stakeholders; iteration plan

> **Tip:** Say assumptions out loud. If new info appears, update your plan explicitly.

---

## Typical Case Study Question Styles

- **Business scenario:** “A client says a deliverable was late/incorrect—what do you do?”
  - Look for: stakeholder comms, root-cause analysis, remediation plan, prevention.

- **Analytics/ML build:** “Predict churn / forecast demand.”
  - Look for: metric selection, leakage control, baseline, feature plan, monitoring.

- **Ambiguous prompt:** Sparse details by design.
  - Look for: clarifying questions, explicit assumptions, structured decomposition.

---

## Example: Walkthrough (Concise)

**Prompt:** “Marketing wants to reduce churn by 10% next quarter. What’s your approach?”

1. **Clarify**
   - Definition of churn, horizon (30/60/90 days), segments, current rate/baseline.
   - Success metric: relative churn reduction; guardrails: CAC, fairness.

2. **Hypothesis**
   - Drivers: usage frequency, support tickets, price sensitivity, competitor activity.

3. **Data**
   - Tables: customers, usage events, billing, tickets, campaigns.
   - Feature windows: last 30/60/90 days; label window aligned to horizon.
   - Quality: late arriving data, seasonality, survivorship bias.

4. **Method**
   - Baseline: rule-based score.
   - Models: regularized logistic regression → tree-based model for non-linearities.
   - Eval: PR-AUC, cost-sensitive utility; calibration for targeting.

5. **Decision & Action**
   - Target top-risk deciles with tailored retention offers.
   - A/B or multi-armed bandit to optimize incentives; measure incremental lift.

6. **Deploy & Monitor**
   - Weekly batch scoring; dashboards for drift, lift, and offer ROI.
   - Retrain monthly; post-hoc fairness checks by segment.

---

## Sample Clarifying Questions (Use a Few Early)

- What’s the **primary objective** and time horizon?
- Who are the **stakeholders** and **end users**?
- Which **metrics** define success and which are guardrails (cost, fairness, latency)?
- What data do we have, at what **granularity** and **freshness**?
- Operational constraints (SLA, privacy, tooling, deployment environment)?

---

## Speak Your Reasoning (What to Say Out Loud)

- “I’ll **restate the goal** and how we’ll measure success…”
- “Given limited details, I’ll **assume** X; if that changes, I’d pivot to Y…”
- “I’d start with a **baseline**, then justify moving to a more complex model…”
- “Here’s how I’d **monitor** drift and performance post-launch…”

---

## Quick Do/Don’t

**Do**
- Tie every step to the **business outcome**.
- Make **assumptions explicit**; update them when new info arrives.
- Show **end-to-end thinking** (data → model → deployment → monitoring).

**Don’t**
- Jump to an algorithm without clarifying the problem.
- Ignore metrics that matter to the business.
- Hand-wave data quality, leakage, or post-deployment monitoring.

---

## Mini Practice Prompts

1. **Late Deliverable:** A client says your dashboard is wrong and late. How do you handle it?
2. **Cold-Start Reco:** New marketplace—how to recommend with sparse data?
3. **Forecasting:** Weekly demand forecasting with promotions and holidays.
4. **Fairness:** Loan approval model shows group disparity. Diagnose and mitigate.

> Practice answering with the 6-step framework above; speak assumptions and trade-offs.

---