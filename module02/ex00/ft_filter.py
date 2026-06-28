def ft_filter(function_to_apply, iterable):
    """Filters elements of an iterable, raising native TypeErrors if inputs are invalid."""
    # Instantly validates the iterable parameter at initialization
    iterator = iter(iterable)

    def _generator_helper(it):
        for item in it:
            # If function_to_apply is None, filter by truthiness (native behavior)
            if function_to_apply is None:
                if item:
                    yield item
            else:
                if function_to_apply(item):
                    yield item

    gen_obj = _generator_helper(iterator)
    gen_obj.__name__ = "ft_filter"
    gen_obj.__qualname__ = "ft_filter"
    return gen_obj
