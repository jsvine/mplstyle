# mplstyle

A simple API for setting [matplotlib](http://matplotlib.org/) styles, as well as a repository of nice styles.

[Click here for a basic demo.](http://nbviewer.ipython.org/url/gist.github.com/jsvine/8f70fa7cde2cd247fad3/raw/3fdab5fc64ac01d013815a9c2530820f3e42523c/mplstyle-example-01.ipynb)

## Usage

__mplstyle__ lets you set multiple matplotlib styles with a single dictionary object, rather than the more cumbersome native methods. So instead of:

	matplotlib.rcParams["lines.linewidth"] = 2
	matplotlib.rcParams["lines.color"] = "r"
	matplotlib.rcParams["grid.color"] = "#CCCCCC"
	matplotlib.rcParams["grid.linewidth"] = 0.5
	
...or the equivalent:

	matplotlib.rc("lines", linewidth=2, color="r")
	matplotlib.rc("grid", color="#CCCCCC", linewidth=0.5)

...you can do:

	import mplstyle
	mplstyle.set({
		"lines": { "linewidth": 2, "color": "r" },
		"grid": { "color": "#CCCCCC", "linewidth": 0.5 }
	})
	

You can find a full list of matplotlib style parameters [here](http://matplotlib.org/users/customizing.html).

### mplstyle.set(obj, *args, **kwargs)

As noted in the usage examples above, you can set matplotlib styles by passing a dictionary of values to `mplstyle.set`. The keys can be nested:

    mplstyle.set({
        "lines": { "linewidth": 2 }
    })

... or use dot notation:

    mplstyle.set({ "lines.linewidth": 2 })

Instead of passing a dictionary as the first argument, you can also pass a module containing a function named `style`. See the ["simple" style module](mplstyle/styles/simple.py) for an example. The module's `style` function can accept any number of positional and/or keyword arguments, which you can pass as additional arguments to `set`. So you can set the simple style like this:

    from mplstyle.styles import simple as simple_style
    mplstyle.set(simple_style)

... or like so, if you'd like to override the default `n_colors` keyword argument:

    from mplstyle.styles import pastel
    mplstyle.set(pastel, n_colors=2)

Currently, __mplstyle__ only comes with the "simple" style, but it's trivial to create your own. Feel free to submit pull requests with style modules you think work particularly well.

### mplstyle.reset(params=DEFAULT_PARAMS)

You can reset matplotlib's styles to their default values by calling `mplstyle.reset()`, or you can pass a dictionary of alternate defaults. The difference between `mplstyle.set()` and `mplstyle.reset()` is that `set` only adds style definitions, while `reset` removes all style definitions that you do not explicitly define.

### mplstyle.get(key=False)

Called without parameters, `mplstyle.get()` returns the current style definitions. Called with a string as its (only) parameter, `mplstyle.get("keystring")` returns the value corresponding to that key.

## Creating Style Modules

See the ["simple" style module](mplstyle/styles/simple.py) for an example of a style module. The only requirement of style modules is that they contain a top-level `style` function and that they return a dictionary of matplotlib style definitions. A bare-bones example:

    def style():
        return { "lines": { "marker": "x" }}

## License

__mplstyle__ is licensed under the MIT License. See LICENSE.txt for more details.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
