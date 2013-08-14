import matplotlib as mpl
import matplotlib.cm
def style():
	N_COLORS = 10
	COLORS = map(mpl.colors.rgb2hex, mpl.cm.Paired([ float(x)/(N_COLORS - 1) for x in range(N_COLORS) ]))
	DARK_GRAY = "#555555"
	LIGHT_GRAY = "#EFEFEF"
	return {
		"axes": {
			"color_cycle": COLORS,
			"facecolor": "white",
			"edgecolor": DARK_GRAY,
			"grid": True,
			"titlesize": "x-large",
			"labelsize": "x-large",
			"labelcolor": "#555555",
			"axisbelow": True
		},
		"patch": {
			"facecolor": COLORS[0]	
		},
		"lines": {
			"color": "r",
			"linewidth": 2,
			"marker": "."
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
