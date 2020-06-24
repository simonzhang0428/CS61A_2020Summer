# 06/24/2020

# Each function should have exactly one job.
# That job should be identifiable with a short name and characterizable in a single line of text.
# Functions that perform multiple jobs in sequence should be divided into multiple functions.

# Don't repeat yourself is a central tenet of software engineering.
# The so-called DRY principle states that multiple fragments of code should not describe redundant logic.
# Instead, that logic should be implemented once, given a name, and applied multiple times.
# If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.

# Functions should be defined generally. Squaring is not in the Python Library precisely
# because it is a special case of the pow function, which raises numbers to arbitrary powers.

# A function definition will often include documentation describing the function, called a docstring,
# which must be indented along with the function body.
# Docstrings are conventionally triple quoted.
# The first line describes the job of the function in one line.
# The following lines can describe arguments and clarify the behavior of the function:
def pressure(v, t, n=6.022e23):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas (default: one mole)
    """
    k = 1.38e-23  # Boltzmann's constant
    # Constant k, bound in the function body or global frame.
    return n * k * t / v


help(pressure)  # see docstring, not including comments

print('Default 1 mole:', pressure(1, 273.15))
print('3 mole:', pressure(1, 273.15, 3 * 6.022e23))

"""
Help on function pressure in module __main__:

pressure(v, t, n=6.022e+23)
    Compute the pressure in pascals of an ideal gas.
    
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
    
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas (default: one mole)

Default 1 mole: 2269.974834
3 mole: 6809.924502
"""