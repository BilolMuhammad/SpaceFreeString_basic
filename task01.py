def remove_spaces(string: str) -> str:
    """
    Removes all spaces from a string of fixed length of 5 characters.
    args:
        string: str
    returns:
        str
    """
    # Your code here
    pass
    ans = ''
    idx = 0
    if string[idx] != ' ':
        ans += string[idx]
    idx += 1
    if string[idx] != ' ':
        ans += string[idx]
    idx += 1
    if string[idx] != ' ':
        ans += string[idx]
    idx += 1
    if string[idx] != ' ':
        ans += string[idx]
    idx += 1
    if string[idx] != ' ':
        ans += string[idx]
    return ans


print(remove_spaces('s f s '))
