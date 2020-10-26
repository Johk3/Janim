## Mobjects
Arrows(LaggedStartMap(GrowArrow, arrows, lag_ratio))

## Transformations
ShowPassingFlash
```
words = TextMobject("Frictionless")
words.shift(2 * RIGHT)
words.add_updater(
    lambda m, dt: m.shift(dt * LEFT)
)
```
## Classes
PiComputingAlgorithmsAxes as a graph for things
