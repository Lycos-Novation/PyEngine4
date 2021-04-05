def clamp(value, mini=None, maxi=None):
    if mini is not None and value < mini:
        return mini
    elif maxi is not None and value > maxi:
        return maxi
    return value