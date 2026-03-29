# AI Cloud Resource Orchestrator

## 📌 Problem Statement
Efficiently allocate cloud resources dynamically to handle workloads while minimizing cost.

---

## 🚀 Features
- OpenEnv compliant environment
- Real-world cloud simulation
- 3 difficulty levels (Easy, Medium, Hard)
- Reward-based evaluation system
- Baseline agent implementation
- Web UI using Gradio (for Hugging Face)

---

## 🧠 How It Works
- The environment simulates cloud VM allocation
- The agent creates/scales/deletes VMs
- Tasks are processed based on resource capacity
- Final score is calculated using efficiency and cost

---

## 🖥️ Running Locally

```bash
pip install -r requirements.txt
python app.py