import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties  # Import FontProperties explicitly

# Font Path for "Aptos Narrow" with fallback to Arial
try:
    font_path = r"C:\Windows\Fonts\AptosNarrow.ttf"  # Update this path if needed
    fm.fontManager.addfont(font_path)
    aptos_narrow = FontProperties(fname=font_path)
    font_to_use = aptos_narrow
except FileNotFoundError:
    print("Aptos Narrow not found. Using Arial as fallback.")
    font_to_use = FontProperties(family="Arial")  # Fallback to Arial

# General Plot Settings
figure_size = (6, 10)   # Portrait orientation

# Padding Settings for Outline (individual control for each side)
top_padding = 0.075      # Gap between outline and plot at the top
bottom_padding = 0.05   # Gap between outline and plot at the bottom
left_padding = 0.05      # Gap between outline and plot on the left
right_padding = 0.05     # Gap between outline and plot on the right

# Outline Margin (gap between outline and figure edge, adjustable)
outline_margin = 0.02

# Outline Settings
border_linewidth = 2    # Border width around plot
border_linestyle = '-'  # Border line style around plot
border_color = 'black'  # Color for the plot outline

# Grid Settings
x_major_grid_interval = 1000
x_minor_grid_interval = 100
y_major_grid_interval = 5
y_minor_grid_interval = 1

# Data and Colors
plot_color_min = 'blue'   # Line color for M_min
plot_color_max = 'green'  # Line color for M_max

# Text Settings
# Title Settings
show_title = True
plot_title = "ULS Bending Moment Envelope Plot"
title_font_family = 'Aptos Narrow'  # Ensure this font is available, or adjust to another if needed
title_font_size = 16
title_bold = True
title_italic = True
title_underline = True

# X-axis Label Settings
show_xlabel = True
xlabel_text = "M values"
xlabel_font_family = 'Aptos Narrow'
xlabel_font_size = 14
xlabel_bold = False
xlabel_italic = False
xlabel_underline = False

# Y-axis Label Settings
show_ylabel = False
ylabel_text = "Y"
ylabel_font_family = 'Aptos Narrow'
ylabel_font_size = 14
ylabel_bold = False
ylabel_italic = False
ylabel_underline = False

# Legend Settings
show_legend = True
legend_labels = {"M_min": "M_min vs Y", "M_max": "M_max vs Y"}
legend_font_family = 'Aptos Narrow'
legend_font_size = 12
legend_bold = False
legend_italic = False
legend_border = True

# Create the Plot
fig, ax = plt.subplots(figsize=figure_size)

# Plot Data from DataFrame da1_c1_left
ax.plot(da1_c1_left["M_min"], da1_c1_left["Y"], color=plot_color_min, label=legend_labels["M_min"])
ax.plot(da1_c1_left["M_max"], da1_c1_left["Y"], color=plot_color_max, label=legend_labels["M_max"])

# Center the y-axis at x=0
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')  # Hide the right spine
ax.spines['top'].set_color('none')    # Hide the top spine

# Set x-axis limits
x_min = min(da1_c1_left["M_min"].min(), da1_c1_left["M_max"].min())
x_max = max(da1_c1_left["M_min"].max(), da1_c1_left["M_max"].max())
ax.set_xlim(x_min, x_max)

# Apply Grid Settings
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_grid_interval))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_grid_interval))
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_major_grid_interval))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(y_minor_grid_interval))
ax.grid(which='major', color='gray', linestyle='-', linewidth=0.8)
ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)

# Title Settings
if show_title:
    title_font = FontProperties(family=title_font_family, size=title_font_size,
                                weight='bold' if title_bold else 'normal',
                                style='italic' if title_italic else 'normal')
    ax.set_title(plot_title, fontproperties=title_font, pad=20)
    if title_underline:
        underline_y_offset = 1.05  # Position offset for the underline
        plt.plot([0.3, 0.7], [underline_y_offset, underline_y_offset], transform=ax.transAxes, color='black', linewidth=1.5)

# X-axis Label Settings
if show_xlabel:
    xlabel_font = FontProperties(family=xlabel_font_family, size=xlabel_font_size,
                                 weight='bold' if xlabel_bold else 'normal',
                                 style='italic' if xlabel_italic else 'normal')
    ax.set_xlabel(xlabel_text, fontproperties=xlabel_font)
    if xlabel_underline:
        ax.xaxis.label.set_underline(True)

# Y-axis Label Settings
if show_ylabel:
    ylabel_font = FontProperties(family=ylabel_font_family, size=ylabel_font_size,
                                 weight='bold' if ylabel_bold else 'normal',
                                 style='italic' if ylabel_italic else 'normal')
    ax.set_ylabel(ylabel_text, fontproperties=ylabel_font)
    if ylabel_underline:
        ax.yaxis.label.set_underline(True)

# Legend Settings - Position legend just below the x-axis label with a small padding
if show_legend:
    legend_font = FontProperties(family=legend_font_family, size=legend_font_size,
                                 weight='bold' if legend_bold else 'normal',
                                 style='italic' if legend_italic else 'normal')
    legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=legend_border)
    for text in legend.get_texts():
        text.set_fontproperties(legend_font)

# Apply individual padding around the plot
plt.subplots_adjust(left=left_padding + outline_margin,
                    right=1 - right_padding - outline_margin,
                    top=1 - top_padding - outline_margin,
                    bottom=bottom_padding + outline_margin + 0.1)  # Extra padding for outline below legend

# Add an Outline Rectangle with Adjustable Gaps
outline = patches.Rectangle(
    (outline_margin, outline_margin), 1 - 2 * outline_margin, 1 - 2 * outline_margin,
    transform=fig.transFigure, color=border_color, linewidth=border_linewidth,
    linestyle=border_linestyle, fill=False
)
fig.patches.append(outline)

# Show Plot
plt.show()