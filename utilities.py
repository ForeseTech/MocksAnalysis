# Change the default width of bar in bar plot
def change_width(plot, new_value):
  for patch in plot.patches:
    current_width = patch.get_width()
    diff = current_width - new_value

    # Change the bar width
    patch.set_width(new_value)

    # Recenter the bar
    patch.set_x(patch.get_x() + diff * .5)

# Show values in each pie sector
def show_values(pct, total):
  absolute = round(pct / 100.*total)
  return "{}".format(absolute)
