# Import necessary libraries
import os

import matplotlib.font_manager as fm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties

# ---------------------------------------------------------------------
# Font Setup
# ---------------------------------------------------------------------


def get_custom_font(font_path=r"C:\Windows\Fonts\AptosNarrow.ttf"):
    """
    Loads custom font (Aptos Narrow) if available; falls back to Arial if not found,
    suppressing warnings if the font file does not exist.
    """
    if os.path.exists(font_path):
        fm.fontManager.addfont(font_path)
        return FontProperties(fname=font_path)
    else:
        print("Aptos Narrow font file not found. Using Arial as fallback.")
        return FontProperties(family="Arial")


# Load font
font_to_use = get_custom_font()

# ---------------------------------------------------------------------
# Plot Settings
# ---------------------------------------------------------------------

# Dynamically adjust figure size based on merged cell size
figure_width = 6  # Fixed width in inches, modify if needed
figure_height = 10  # Adjust based on the merged cell area height

# Padding Settings
padding = {
    "top": 0.075,
    "bottom": 0.05,
    "left": 0.05,
    "right": 0.05,
    "outline_margin": 0.02,  # Margin between outline and plot area
}

# Outline Settings
outline_properties = {"color": "black", "linewidth": 2, "linestyle": "-"}

# Grid Settings for Major/Minor Ticks
grid_settings = {
    "x_major_interval": 1000,
    "x_minor_interval": 100,
    "y_major_interval": 5,
    "y_minor_interval": 1,
}

# ---------------------------------------------------------------------
# Data and Plot Configuration
# ---------------------------------------------------------------------

plots = [
    {
        "data": da1_c1_left,
        "x": "M_min",
        "y": "Y",
        "color": "blue",
        "label": "M_min vs Y - C1 Left",
    },
    {
        "data": da1_c1_left,
        "x": "M_max",
        "y": "Y",
        "color": "green",
        "label": "M_max vs Y - C1 Left",
    },
    {
        "data": da1_c2_left,
        "x": "M_min",
        "y": "Y",
        "color": "red",
        "label": "M_min vs Y - C2 Left",
    },
    {
        "data": da1_c2_left,
        "x": "M_max",
        "y": "Y",
        "color": "purple",
        "label": "M_max vs Y - C2 Left",
    },
]

# ---------------------------------------------------------------------
# Text and Label Configuration
# ---------------------------------------------------------------------

title_config = {
    "text": "ULS Bending Moment Envelope Plot",
    "show": True,
    "font_family": "Aptos Narrow",
    "size": 16,
    "bold": True,
    "italic": True,
    "underline": True,
}

xlabel_config = {
    "text": "M values",
    "show": True,
    "font_family": "Aptos Narrow",
    "size": 14,
    "bold": False,
    "italic": False,
    "underline": False,
}

ylabel_config = {
    "text": "Y",
    "show": True,
    "font_family": "Aptos Narrow",
    "size": 14,
    "bold": False,
    "italic": False,
    "underline": False,
}

legend_config = {
    "show": True,
    "font_family": "Aptos Narrow",
    "size": 12,
    "bold": False,
    "italic": False,
    "border": True,
}

# ---------------------------------------------------------------------
# Plotting Functions
# ---------------------------------------------------------------------


def plot_data(ax, plot_list):
    """
    Plots each dataset from `plot_list` onto `ax` with specified colors and labels.
    """
    for plot in plot_list:
        ax.plot(
            plot["data"][plot["x"]],
            plot["data"][plot["y"]],
            color=plot["color"],
            label=plot["label"],
        )


def configure_axes_limits(ax, plot_list):
    """
    Dynamically sets x-axis limits based on the data range in `plot_list`
    and centers the y-axis at x = 0.
    """
    # Calculate x-axis limits based on the range of data in the plots
    x_min = min([plot["data"][plot["x"]].min() for plot in plot_list])
    x_max = max([plot["data"][plot["x"]].max() for plot in plot_list])
    ax.set_xlim(x_min, x_max)

    # Center y-axis at x = 0
    ax.spines["left"].set_position(("data", 0))  # Position the y-axis at x = 0
    ax.spines["right"].set_color("none")  # Hide the right spine
    ax.spines["top"].set_color("none")  # Hide the top spine


def configure_grid(ax, grid_settings):
    """
    Applies major and minor grid settings for x and y axes on `ax`.
    """
    ax.xaxis.set_major_locator(
        ticker.MultipleLocator(grid_settings["x_major_interval"])
    )
    ax.xaxis.set_minor_locator(
        ticker.MultipleLocator(grid_settings["x_minor_interval"])
    )
    ax.yaxis.set_major_locator(
        ticker.MultipleLocator(grid_settings["y_major_interval"])
    )
    ax.yaxis.set_minor_locator(
        ticker.MultipleLocator(grid_settings["y_minor_interval"])
    )
    ax.grid(which="major", color="gray", linestyle="-", linewidth=0.8)
    ax.grid(which="minor", color="lightgray", linestyle=":", linewidth=0.5)


def configure_text(ax, config, axis="title"):
    """
    Configures text for title, xlabel, and ylabel using the settings in `config`.
    """
    font_props = FontProperties(
        family=config["font_family"],
        size=config["size"],
        weight="bold" if config["bold"] else "normal",
        style="italic" if config["italic"] else "normal",
    )

    if axis == "title" and config["show"]:
        ax.set_title(config["text"], fontproperties=font_props, pad=20)
        if config["underline"]:
            plt.plot(
                [0.3, 0.7],
                [1.05, 1.05],
                transform=ax.transAxes,
                color="black",
                linewidth=1.5,
            )
    elif axis == "xlabel" and config["show"]:
        ax.set_xlabel(config["text"], fontproperties=font_props)
        if config["underline"]:
            ax.xaxis.label.set_underline(True)
    elif axis == "ylabel" and config["show"]:
        ax.set_ylabel(config["text"], fontproperties=font_props)
        if config["underline"]:
            ax.yaxis.label.set_underline(True)


def add_legend(ax, config):
    """
    Adds a legend to `ax` based on `config` settings.
    """
    if config["show"]:
        font_props = FontProperties(
            family=config["font_family"],
            size=config["size"],
            weight="bold" if config["bold"] else "normal",
            style="italic" if config["italic"] else "normal",
        )
        legend = ax.legend(
            loc="upper center",
            bbox_to_anchor=(0.5, -0.1),
            ncol=2,
            frameon=config["border"],
        )
        for text in legend.get_texts():
            text.set_fontproperties(font_props)


def add_outline(fig, outline_properties, padding):
    """
    Adds an outline rectangle with specified properties and padding around the plot area.
    """
    outline = patches.Rectangle(
        (padding["outline_margin"], padding["outline_margin"]),
        1 - 2 * padding["outline_margin"],
        1 - 2 * padding["outline_margin"],
        transform=fig.transFigure,
        **outline_properties,
        fill=False
    )
    fig.patches.append(outline)


# ---------------------------------------------------------------------
# Main Plotting Routine
# ---------------------------------------------------------------------

# Initialize figure and axes with dynamic figure size
fig, ax = plt.subplots(figsize=(figure_width, figure_height))

# Plot data
plot_data(ax, plots)

# Configure axis limits, grid, and text
configure_axes_limits(ax, plots)
configure_grid(ax, grid_settings)
configure_text(ax, title_config, axis="title")
configure_text(ax, xlabel_config, axis="xlabel")
configure_text(ax, ylabel_config, axis="ylabel")
add_legend(ax, legend_config)

# Adjust padding and add outline
plt.subplots_adjust(
    left=padding["left"] + padding["outline_margin"],
    right=1 - padding["right"] - padding["outline_margin"],
    top=1 - padding["top"] - padding["outline_margin"],
    bottom=padding["bottom"] + padding["outline_margin"] + 0.1,
)
add_outline(fig, outline_properties, padding)

# Show the plot
plt.show()
