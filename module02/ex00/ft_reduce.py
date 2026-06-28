def ft_reduce(function_to_apply, iterable, initializer=None):
    """Reduces an iterable to a single value, raising native TypeErrors on invalid inputs."""
    # 1. Verify iterable parameter instantly
    try:
        iterator = iter(iterable)
    except TypeError:
        # Adding 'from None' cuts the chain and hides the first traceback!
        raise TypeError("ft_reduce() arg 2 must support iteration") from None

    # 2. Set up the starting accumulator value
    if initializer is None:
        try:
            accum_value = next(iterator)
        except StopIteration:
            # Native reduce throws a TypeError if you pass an empty list with no starting point
            raise TypeError("ft_reduce() of empty sequence with no initial value") from None
    else:
        accum_value = initializer

    # 3. Process the remaining items eagerly
    for item in iterator:
        accum_value = function_to_apply(accum_value, item)

    return accum_value
