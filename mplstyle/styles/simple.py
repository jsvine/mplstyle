import matplotlib as mpl
import matplotlib.cm

MAX_COLORS = 8
DARK_GRAY = "#555555"
LIGHT_GRAY = "#EFEFEF"

def style(palette=mpl.cm.Set1, n_colors=MAX_COLORS):
    colors = map(mpl.colors.rgb2hex, palette([
        float(x)/(MAX_COLORS) for x in range(MAX_COLORS)
    ]))[:min(MAX_COLORS, n_colors)]
    return {
        "axes": {
            "color_cycle": colors,
            "facecolor": "white",
            "edgecolor": DARK_GRAY,
            "grid": True,
            "titlesize": "x-large",
            "labelsize": "x-large",
            "labelcolor": "#555555",
            "axisbelow": True
        },
        "patch": {
            "facecolor": colors[0]	
        },
        "lines": {
            "color": "r",
            "marker": "o",
            "markersize": 4,
            "markeredgewidth": 0
        },
        "figure": {
            "facecolor": "white",
            "edgecolor": DARK_GRAY
        },
        "ytick": {
            "color": DARK_GRAY,
            "direction": "out"
        },
        "xtick": {
            "color": DARK_GRAY,
            "direction": "out"
        },
        "grid": {
            "color": DARK_GRAY,
            "linestyle": ':'
        }
    }
