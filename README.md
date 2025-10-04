# Technation AI Equity Challenge: Analysis of AI's Impact on the Canadian Job Market

## Introduction

This project, undertaken for the Technation AI Equity Challenge, analyzes the multifaceted impact of Artificial Intelligence on the Canadian job market. It seeks to understand AI readiness across various occupations and industries, identify potential employment impacts, and assess the vulnerability of different demographic groups to AI-driven workforce changes. By integrating data from multiple authoritative Canadian sources, this analysis provides a comprehensive overview through a series of data visualizations and detailed reports.

---

## Visualizations

This repository contains the data and scripts to generate three key visualizations, each offering a unique perspective on AI's role in the Canadian labour landscape:

### 1. AI Employment Impact Bubble Matrix

**Description:** A bubble matrix that illustrates the scale of AI's impact on employment across different provinces and industries. The size of each bubble corresponds to the number of "workers exposed" to AI, while the color indicates the projected timeline of this impact (Immediate, Medium-term, or Long-term).

**Files:**

* `ai_employment_impact.csv`: The dataset containing the data for the bubble matrix.
* `bubble_matrix_generator.py`: The Python script used to generate the bubble matrix visualization.
* `methodology_bubble_matrix.md`: A detailed report outlining the methodology used for the bubble matrix analysis.

### 2. Occupation-Industry Network Graph

**Description:** A network graph that visualizes the intricate connections between various occupations and industries in Canada. The size of each node (representing an occupation or industry) is proportional to its employment count, and the color of the node indicates its "AI Readiness Score". The thickness of the links between nodes represents the number of workers in each occupation-industry pair.

**Files:**

* `links_network_data.csv`: The dataset defining the connections (edges) between occupations and industries.
* `points_network_data.csv`: The dataset defining the nodes (points) representing occupations and industries.
* `methodology_report_network.md`: A detailed report on the methodology behind the network graph.

### 3. Canadian Provincial AI Job Exposure Map

**Description:** A choropleth map of Canada that displays a population-weighted AI occupational exposure score for each province and territory. This visualization highlights regions with higher overall exposure to AI transformation in the workforce, particularly those with large urban centers.

**Files:**

* `Map_Generator.py`: The Python script to generate the choropleth map.

### 4. AI Impact Vulnerability Radar Chart

**Description:** A multi-axis radar chart designed to visualize the Canadian AI Impact Vulnerability Index (AIVI). Each polygon on the chart represents a specific demographic cohort, with vertices showing average scores for Industry Risk, Educational Vulnerability, Overall AIVI Score, and self-perceived AI risk and benefit. This allows for a comparative analysis of AI vulnerability across different population segments.

**Files:**

* `canadianAIsentimentsurvey.csv`: The dataset from the Canadian AI Sentiment Survey (CAISS) used to calculate the AIVI.
* `methodology_survey.md`: The methodology report detailing the construction of the AIVI and the design of the radar chart.

---

## Methodology

The analytical approach is grounded in a combination of quantitative data analysis and survey-based research. Key methodological components include:

* **AI Readiness Index:** A composite score that quantifies the preparedness of occupations and industries for AI integration. This index is a weighted average of four components: Automation Risk, Digital Skill Share, Vacancy AI-Skill Growth, and Industry Digital Adoption.
* **Income Level Classification:** Occupations are categorized into Low, Medium, and High-income levels based on the 2023 national income distribution.
* **Canadian AI Impact Vulnerability Index (AIVI):** A composite metric based on a national survey that assesses the perceived risk and impact of AI on the Canadian workforce. The AIVI incorporates demographic, professional, and educational data to profile AI vulnerability.

**For a comprehensive understanding of the methodologies employed, please refer to the detailed methodology reports:**

* `methodology_report_network.md`
* `methodology_bubble_matrix.md`
* `methodology_survey.md`

---

## Data Sources

The analysis is based on data aggregated from several authoritative Canadian sources, including:

* Statistics Canada – Labour Force Survey (2023–2024)
* Job Bank Canada – Wage Data (2024)
* AI Exposure and Adoption Studies (2024–2025)
* Canadian Survey on Business Conditions (Q2 2025)
* Canadian AI Sentiment Survey (CAISS) (Q3 2025)

---

## File Descriptions

* `links_network_data.csv`: Data for the network graph's edges, connecting occupations to industries.
* `points_network_data.csv`: Data for the network graph's nodes, representing occupations and industries.
* `ai_employment_impact.csv`: Data for the bubble matrix, showing AI's impact on employment.
* `canadianAIsentimentsurvey.csv`: Anonymized data from the Canadian AI Sentiment Survey.
* `Survey_dataset.csv`: A smaller, anonymized survey dataset.
* `bubble_matrix_generator.py`: Python script to generate the bubble matrix visualization.
* `Map_Generator.py`: Python script to generate the choropleth map of AI job exposure.
* `methodology_report_network.md`: Methodology report for the network analysis.
* `methodology_bubble_matrix.md`: Methodology report for the bubble matrix analysis.
* `methodology_survey.md`: Methodology report for the survey-based vulnerability index.
* `LICENSE`: The MIT License for this project.
* `.gitignore`: A file specifying which files and directories to ignore in a Git repository.

---

## How to Run the Scripts

To generate the visualizations, you can run the provided Python scripts. Ensure you have the necessary libraries installed (e.g., pandas, matplotlib, geopandas).

**Bubble Matrix:**

```bash
python bubble_matrix_generator.py
```

**Choropleth Map:**

```bash
python Map_Generator.py
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For any inquiries regarding the methodology or data, please contact:

* Statistics Canada: [infostats@statcan.gc.ca](mailto:infostats@statcan.gc.ca)
* Owner: Ronald Wopara(rwopara@ualberta.ca)
* Owner: Peretz Onyina(ponyia@ualberta.ca)
* Job Bank Canada: [NC-LMI-IMT-GD@hrsdc-rhdcc.gc.ca](mailto:NC-LMI-IMT-GD@hrsdc-rhdcc.gc.ca)
