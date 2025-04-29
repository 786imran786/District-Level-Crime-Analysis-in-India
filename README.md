# District-Level-Crime-Analysis-in-India
crime analysis in India using the IPC 2013 dataset. It captures your EDA, visualizations, objectives, and tools used — all in clean markdown formatting.
# 🕵️‍♂️ CrimeScope: District-Level Crime Analysis in India (2013)

A data-driven dashboard to visualize and understand crime patterns across Indian districts using the **2013 IPC (Indian Penal Code)** crime dataset.  
This project applies **EDA (Exploratory Data Analysis)** and insightful **data visualizations** to uncover trends and correlations using Python libraries like Pandas, Seaborn, and Matplotlib.

--
## 📁 Dataset Description

**Source**: Government of India  
**File**: `01_District_wise_crimes_committed_IPC_2013.csv`  
**Columns** (sample):  
- `STATE/UT`, `DISTRICT`, `YEAR`, `MURDER`, `RAPE`, `KIDNAPPING`, `RIOTS`, `THEFT`, etc.  
- A total of 30+ crime categories reported under IPC.

---

## 🎯 Project Objectives

Each objective is accompanied by visualizations to support insights:

1. **Top 10 Crime-Prone States**  
   👉 Identifies states with the highest number of total crimes.

2. **Crime region wise**  
   👉 Shows how murder cases vary across different states.

3. **Trend of Violent Crimes**  
   👉 Line graph showing the frequency of major violent crimes like Murder, Rape, Riots, etc.

4. **Crimes Against Women: State-wise Comparison**  
   👉 Focuses on Rape, Assault, Dowry Deaths to assess gender-related crime hotspots.

5. **Districts with Highest Number of Thefts**  
   👉 Bar plot highlighting theft concentration zones.

6. **Heatmap of Correlation Between Crimes**  
   👉 Understands how various crimes are statistically related to each other.

7. **Scatter Plot: Riots vs Hurt/Grievous Hurt**  
   👉 Visualizes how mob violence may relate to physical injury cases.

---

## 📊 Libraries Used

- `Pandas` – Data handling and preprocessing  
- `Seaborn` – For rich statistical visualizations  
- `Matplotlib` – Core plotting tool  
- `NumPy` – Numerical operations  
- `Jupyter / IDLE` – Local environment for execution

---

## ⚙️ How to Run

1. Clone this repo  
2. Make sure Python 3.x is installed  
3. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
