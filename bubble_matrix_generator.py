import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

# 1. Load the provided AI impact data
csv_data = """Province,Industry,Total Workers,Workers Exposed,Impact Timeline
Ontario,Healthcare,909000,554490,Medium
Ontario,Manufacturing,754000,271440,Medium
Ontario,Retail,557000,334200,Immediate
Ontario,Finance & Insurance,412000,403760,Immediate
Ontario,Professional & Technical Services,662000,609040,Immediate
Ontario,Transportation & Warehousing,318000,108120,Long-term
Ontario,Natural Resources,98000,31360,Long-term
Quebec,Healthcare,642000,391620,Medium
Quebec,Manufacturing,452000,162720,Medium
Quebec,Retail,418000,250800,Immediate
Quebec,Finance & Insurance,205000,200900,Immediate
Quebec,Professional & Technical Services,312000,287040,Immediate
Quebec,Transportation & Warehousing,215000,73100,Long-term
Quebec,Natural Resources,87000,27840,Long-term
British Columbia,Healthcare,312000,190320,Medium
British Columbia,Manufacturing,172000,61920,Medium
British Columbia,Retail,267000,160200,Immediate
British Columbia,Finance & Insurance,128000,125440,Immediate
British Columbia,Professional & Technical Services,256000,235520,Immediate
British Columbia,Transportation & Warehousing,132000,44880,Long-term
British Columbia,Natural Resources,78000,24960,Long-term
Alberta,Healthcare,289000,176290,Medium
Alberta,Manufacturing,122000,43920,Medium
Alberta,Retail,246000,147600,Immediate
Alberta,Finance & Insurance,142000,139160,Immediate
Alberta,Professional & Technical Services,218000,200560,Immediate
Alberta,Transportation & Warehousing,131000,44540,Long-term
Alberta,Natural Resources,135000,43200,Long-term
Manitoba,Healthcare,98000,59780,Medium
Manitoba,Manufacturing,58000,20880,Medium
Manitoba,Retail,85000,51000,Immediate
Manitoba,Finance & Insurance,42000,41160,Immediate
Manitoba,Professional & Technical Services,48000,44160,Immediate
Manitoba,Transportation & Warehousing,42000,14280,Long-term
Manitoba,Natural Resources,28000,8960,Long-term
Saskatchewan,Healthcare,72000,43920,Medium
Saskatchewan,Manufacturing,34000,12240,Medium
Saskatchewan,Retail,68000,40800,Immediate
Saskatchewan,Finance & Insurance,28000,27440,Immediate
Saskatchewan,Professional & Technical Services,38000,34960,Immediate
Saskatchewan,Transportation & Warehousing,38000,12920,Long-term
Saskatchewan,Natural Resources,52000,16640,Long-term
"""
df = pd.read_csv(StringIO(csv_data))

# 2. Prepare data for plotting
# Define order and mapping for categorical data
provinces = df['Province'].unique()[::-1]  # Reverse to have Ontario at the top
industries = [
    'Finance & Insurance', 'Professional & Technical Services', 'Retail',
    'Healthcare', 'Manufacturing', 'Transportation & Warehousing', 'Natural Resources'
]
df['Province'] = pd.Categorical(df['Province'], categories=provinces, ordered=True)
df['Industry'] = pd.Categorical(df['Industry'], categories=industries, ordered=True)

# Map impact timeline to colors
color_map = {'Immediate': '#d73027', 'Medium': '#fdae61', 'Long-term': '#fee090'}
df['color'] = df['Impact Timeline'].map(color_map)

# Normalize bubble sizes for better visualization
# We use a power scale to reduce the difference between the largest and smallest bubbles
min_workers = df['Workers Exposed'].min()
max_workers = df['Workers Exposed'].max()
df['size'] = (df['Workers Exposed'] / max_workers) * 2000  # Scale factor for bubble size

# 3. Create the Bubble Matrix Plot
fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Scatter plot for the bubbles
scatter = ax.scatter(
    x=df['Industry'],
    y=df['Province'],
    s=df['size'],
    c=df['color'],
    alpha=0.8,
    edgecolors='black',
    linewidth=0.5
)

# 4. Add Labels and Titles
ax.set_xlabel('Industry', fontsize=14, fontweight='bold')
ax.set_ylabel('Province', fontsize=14, fontweight='bold')
ax.set_title('AI Employment Impact: Workers Exposed by Province and Industry', fontsize=18, fontweight='bold', pad=20)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Add data labels (number of workers exposed) inside each bubble
for i, row in df.iterrows():
    # Format label to thousands (e.g., 554k)
    label = f"{row['Workers Exposed']/1000:.0f}k"
    ax.text(row['Industry'], row['Province'], label,
            ha='center', va='center', fontsize=9, color='black', fontweight='bold')

# 5. Create Legends
# Color Legend for Impact Timeline
legend_elements_color = [
    plt.Line2D([0], [0], marker='o', color='w', label='Immediate', markerfacecolor=color_map['Immediate'], markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Medium-term', markerfacecolor=color_map['Medium'], markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Long-term', markerfacecolor=color_map['Long-term'], markersize=12)
]
color_legend = ax.legend(handles=legend_elements_color, title='Impact Timeline', loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, title_fontsize=14)
ax.add_artist(color_legend)

# Size Legend for Workers Exposed
# Create some proxy artists for the size legend
size_values = [100000, 300000, 600000]
scaled_sizes = [(v / max_workers) * 2000 for v in size_values]
legend_elements_size = [
    plt.scatter([], [], s=s, c='gray', alpha=0.8, label=f'{v/1000:.0f}k') for s, v in zip(scaled_sizes, size_values)
]
size_legend = ax.legend(handles=legend_elements_size, title='Workers Exposed', loc='upper left', bbox_to_anchor=(1.02, 0.7), labelspacing=2.5, fontsize=12, title_fontsize=14)

# 6. Final Touches
ax.grid(True, which='major', linestyle='--', linewidth='0.5', color='gray', alpha=0.5)
ax.set_axisbelow(True) # Send grid lines to the back

# Remove plot spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Adjust layout to prevent labels from being cut off
plt.tight_layout(rect=[0, 0, 0.85, 1]) # Make space for the legends on the right

# Save the figure
svg_filename = "ai_impact_bubble_matrix.svg"
fig.savefig(svg_filename, format='svg')

print(f"Bubble matrix chart successfully saved as {svg_filename}")