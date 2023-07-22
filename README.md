<a id="mode_calculator"></a>

# mode\_calculator

<a id="mode_calculator.ModeCounter"></a>

## ModeCounter Objects

```python
class ModeCounter()
```

Class to keep track of the mode in a list of numbers.

**Attributes**:

- `frequency_dictionary` - A dictionary where keys are numbers and values are their frequency
- `winning_frequency` - The highest frequency among all numbers.
- `winner` - The number with the highest frequency.

<a id="mode_calculator.ModeCounter.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes frequency dictionary and sets winning_frequency to 0

<a id="mode_calculator.ModeCounter.add_number"></a>

#### add\_number

```python
def add_number(number)
```

Adds a number to the frequecny dictionary and update the mode.

**Arguments**:

- `number` - The number to be added.

<a id="mode_calculator.ModeCounter.update"></a>

#### update

```python
def update(number)
```

Updates the current mode if the frequency of the number is higher than the current modes frequency.

args:
number: The number to be checked against the current mode.

<a id="mode_calculator.ModeCounter.get"></a>

#### get

```python
def get()
```

Returns the winner

**Returns**:

  The number with the highest frequency.

