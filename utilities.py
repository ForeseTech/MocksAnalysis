import matplotlib.pyplot as plt

# Change the default width of bar in bar plot
def change_width(plot, new_value):
    for patch in plot.patches:
        current_width = patch.get_width()
        diff = current_width - new_value

        # Change the bar width
        patch.set_width(new_value)

        # Recenter the bar
        patch.set_x(patch.get_x() + diff * 0.5)


# Show values in each pie sector
def show_values(pct, total):
    absolute = round(pct / 100.0 * total)
    return "{}".format(absolute)

# Attach a text label above each vertical bar, displaying its value
def annotate_bar(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            "{}".format(height),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )
