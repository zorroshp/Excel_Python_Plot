Here's a comprehensive README file detailing all options for your repository:

---

# Dynamic Plotting for Excel Integration with Matplotlib

This repository contains a Python script for creating dynamically sized plots with Matplotlib, specifically designed for seamless integration with Excel, where plot dimensions may vary based on cell size. The script provides customizable options for fonts, gridlines, axis labels, legend styling, and plot outline, making it versatile for a variety of visualization needs.

## Features

- **Dynamic Sizing**: Automatically adjusts plot size to fit Excel's merged cells.
- **Custom Font Handling**: Supports custom fonts with fallbacks to standard fonts.
- **Flexible Configuration**: Customize gridlines, labels, legends, and outlines for a professional look.
- **Edge-Centered Y-Axis**: Positions the y-axis at \( x = 0 \) for a balanced layout.
- **Modular Functions**: Organized code for easy customization and extension.

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install matplotlib
   ```
2. **Update the Font Path**: Modify `font_path` in `get_custom_font()` if using a custom font, such as Aptos Narrow.

3. **Define Plot Data**: Update `plots` to include your datasets.

## Usage

Run the script to generate a plot dynamically fitted to your Excel cell area. Adjust figure height and width as needed.

## Configuration Options

### Font Setup
```python
font_to_use = get_custom_font(font_path="path/to/custom_font.ttf")
```
- **font_path**: Path to the desired font. If unavailable, defaults to Arial.

### Plot Settings

```python
figure_width = 6
figure_height = 10
```
- **figure_width**: Width of the figure in inches.
- **figure_height**: Height of the figure in inches, adjustable for merged cells.

#### Padding Settings
```python
padding = {
    'top': 0.075, 'bottom': 0.05, 'left': 0.05, 'right': 0.05,
    'outline_margin': 0.02
}
```
- **top, bottom, left, right**: Control the padding within the plot area.
- **outline_margin**: Gap between plot area and outline.

#### Outline Settings
```python
outline_properties = {
    'color': 'black', 'linewidth': 2, 'linestyle': '-'
}
```
- **color**: Outline color.
- **linewidth**: Outline thickness.
- **linestyle**: Outline line style (e.g., `'-'`, `'--'`).

#### Grid Settings
```python
grid_settings = {
    'x_major_interval': 1000, 'x_minor_interval': 100,
    'y_major_interval': 5, 'y_minor_interval': 1
}
```
- **x_major_interval, y_major_interval**: Spacing for major grid lines.
- **x_minor_interval, y_minor_interval**: Spacing for minor grid lines.

### Plot Data and Labels

#### Plot Data
```python
plots = [
    {"data": da1_c1_left, "x": "M_min", "y": "Y", "color": "blue", "label": "M_min vs Y - C1 Left"},
    {"data": da1_c1_left, "x": "M_max", "y": "Y", "color": "green", "label": "M_max vs Y - C1 Left"}
]
```
- **data**: Dataset for each plot.
- **x, y**: Column names for x and y values.
- **color**: Line color for the plot.
- **label**: Label for the legend.

#### Title, X-label, Y-label, and Legend Configurations

##### Title Configuration
```python
title_config = {
    'text': "Plot Title",
    'show': True, 'font_family': 'Aptos Narrow', 'size': 16,
    'bold': True, 'italic': True, 'underline': True
}
```
- **text**: Title text.
- **show**: Show or hide title.
- **font_family, size**: Font family and size for the title.
- **bold, italic, underline**: Set styling options.

##### X-Label and Y-Label Configuration
```python
xlabel_config = {
    'text': "X-Axis Label",
    'show': True, 'font_family': 'Aptos Narrow', 'size': 14,
    'bold': False, 'italic': False, 'underline': False
}

ylabel_config = {
    'text': "Y-Axis Label",
    'show': True, 'font_family': 'Aptos Narrow', 'size': 14,
    'bold': False, 'italic': False, 'underline': False
}
```
- Same options as title, but for x and y axis labels.

##### Legend Configuration
```python
legend_config = {
    'show': True, 'font_family': 'Aptos Narrow', 'size': 12,
    'bold': False, 'italic': False, 'border': True
}
```
- **show**: Display the legend.
- **font_family, size**: Font family and size.
- **bold, italic**: Styling for legend text.
- **border**: Show or hide legend border.

## Example Output

When configured, the script generates a plot that fits dynamically within Excel cells, with centered y-axis and clear, customizable labels and legends.

## License

This project is licensed under the MIT License.

--- 

This README provides an overview, usage instructions, and explanations for each configurable option, making it easy to understand and modify as needed.
