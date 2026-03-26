# Beyond Reward Optimization: Reliability-Aware Evaluation of MARL under Stochastic Stress

🔬 Official implementation :

**"Beyond Reward Optimization: Reliability-Aware Evaluation of Multi-Agent Reinforcement Learning under Stochastic Stress Conditions"**

---

## 📌 Overview

This repository provides the implementation of a **reliability-aware evaluation framework** for Multi-Agent Reinforcement Learning (MARL) in stochastic, safety-critical environments.

While conventional MARL evaluation focuses on **reward optimization**, this work demonstrates that:

> ⚠️ Policies with similar rewards can exhibit fundamentally different reliability characteristics.

---

## 📖 Related Work

This study builds upon prior work on curriculum learning for water distribution systems:

**Amarnath, V. (2026).**  
*Amarnath, V. (2026). Robust control of water distribution networks under drought stress: A multi-agent curriculum learning approach. Water Resources Management. In press. [Expected DOI: https://doi.org/10.1007/s11269-026-04592-5]

While the prior work focuses on improving control performance under drought stress, the present study extends this line of research by introducing a **reliability-aware evaluation framework** that explicitly characterizes failure dynamics under stochastic conditions.

---

## 🧠 Key Contributions

- ✅ **Reliability-aware evaluation framework** for MARL  
- ✅ Introduction of **failure-dynamics metrics**:
  - Deep depletion fraction  
  - Run-length distribution  
  - Failure persistence  
- ✅ Demonstration of **reward–reliability decoupling**
- ✅ Multi-Phase Curriculum Learning (**MPCL**) for robust policy learning  
- ✅ Statistical validation across **multi-seed stochastic environments (n = 20)**  

---

## 🌍 Problem Setting

We model a **stochastic water distribution system** with:

- Non-stationary demand  
- Variable inflow conditions  
- Multi-agent decentralized control  

### Stress Regimes:
- Nominal (I = 80)  
- Moderate (I = 50)  
- Severe Drought (I = 20)  

---

## ⚙️ Methodology

### 🔹 Baseline
- MAPPO (Multi-Agent PPO)
- Centralized critic, decentralized actors

### 🔹 Proposed Approach
- **Multi-Phase Curriculum Learning (MPCL)**
  - Phase 1: Nominal training  
  - Phase 2: Moderate stress  
  - Phase 3: Severe drought adaptation  

---

## 📊 Key Insight

> 📉 Reward ≈ Similar  
> 📈 Reliability ≠ Different  

- Baseline: Frequent short-duration failures  
- MPCL: Fewer, sustained stable regimes  

👉 Reveals **structural shift in failure dynamics**

---

## Repository Contents
- `marl_training_revised.ipynb`: Main training and analysis notebook.
- `inflow_sample.csv`: Example precipitation dataset (publicly available).
- `preprocess_demand.py`: Illustrative preprocessing script for restricted demand data.
- `requirements.txt`: Python dependencies.

---

## ▶️ Quick Start

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
2️⃣ Run training and evaluation
python marl_training_revised.py


This work introduces reliability-aware metrics beyond reward:

Metric	Description
Deep Depletion Fraction	Fraction of time in critical failure
Run-Length	Duration of continuous failure regimes
Violation Count	Number of constraint violations
Failure Persistence	Temporal structure of failures
🔬 Experimental Setup
Algorithm: MAPPO + MPCL
Seeds: 20 stochastic runs
Evaluation Horizon: Full simulation episodes
Statistical Tests:
Welch’s t-test
Mann–Whitney U test

📊 Results Summary
✔ Statistically indistinguishable rewards
✔ Significant differences in reliability (p < 0.001)
✔ Reduction in oscillatory failures
✔ Emergence of Predictive Throttling behavior
📦 Data Availability

Due to data usage restrictions, real-world demand data cannot be publicly shared.

However:

✔ Preprocessing scripts are provided
✔ Representative synthetic datasets are included
✔ Full pipeline reproducibility is supported
📜 License

This project is licensed under the MIT License.

## 📜 Intellectual Property

Portions of the methodology described in this repository are the subject of a pending U.S. provisional patent application:

**U.S. Provisional Patent Application No. 63/944,327**

This repository is provided for academic and research purposes. The patent application covers specific aspects of the curriculum learning and reliability-aware evaluation framework.

👩‍💻 Author

Vidhyalakshmi Amarnath
Department of Artificial Intelligence
City University of Seattle

📧 amarnathvidhyalakshmi@gmail.com

⭐ Acknowledgment

This work builds upon prior research in curriculum learning and MARL for infrastructure systems and extends it toward reliability-aware evaluation in safety-critical environments.
