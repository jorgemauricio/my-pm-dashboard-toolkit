# 📊 Advanced Product Analytics Dashboard Toolkit

A professional toolkit for Product Managers and Data Scientists to design, architect, and deploy high-fidelity dashboards. This repo combines **AI-driven UI design**, **Power BI Theme JSONs**, and **Python data processing**.

---

## 💡 Design Philosophies

This toolkit offers two distinct design directions based on your target stakeholder:

### 1. The "Executive" (Apple Minimalist)
* **Focus:** Clarity, high-level KPIs, and "White Space."
* **Target:** C-Suite, VPs, and General Managers.
* **Philosophy:** Reduces cognitive load. It answers "Are we winning?" in 5 seconds or less.
* **Aesthetic:** Light mode, San Francisco typography, 20px+ corner radius.

### 2. The "Builder" (Linear Dark Mode)
* **Focus:** Precision, high data density, and technical health.
* **Target:** Product Managers, Engineering Leads, and Growth Squads.
* **Philosophy:** Designed for deep dives. It focuses on trends, technical friction, and performance bottlenecks.
* **Aesthetic:** Dark mode, high contrast, 8px corner radius, neon accents.

---

## 🛠 Repository Structure

* 📂 **/prompts**: Optimized Meta-Prompts to generate dashboard mockups using Gemini (Nano Banana 2).
* 📂 **/themes**: Ready-to-use `.json` files to apply Apple or Linear styles to Power BI instantly.
* 📂 **/scripts**: `data_processor.py` — A Python utility to simulate or process product adoption metrics.
* 📂 **/assets**: Preview images of the generated dashboard architectures.

---

## 🚀 Getting Started

### Step 1: Generate the Design
Copy the template from `/prompts/linear-dark-prompt.md` and paste it into Gemini. It will analyze your KPIs and provide a high-fidelity visual layout.

### Step 2: Set up Power BI
1. Open Power BI Desktop.
2. Go to **View** > **Themes** > **Browse for Themes**.
3. Select `themes/linear_dark.json`.
4. Your charts will automatically adopt the professional dark-mode palette.

### Step 3: Process the Data
Run the Python script to prepare your dataset for the dashboard:
```bash
python scripts/data_processor.py
