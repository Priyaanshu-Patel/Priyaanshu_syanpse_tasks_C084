def earliest_lumos_step(runes: str) -> int:
    needed = {'L', 'U', 'M', 'O', 'S'}
    seen = set()

    for i, ch in enumerate(runes):
        c = ch.upper()   
        if c in needed:
            seen.add(c)
            if len(seen) == len(needed):  
                return i + 1   
    return -1


# Ex
print(earliest_lumos_step("xxlUmoSzz"))   #7 
print(earliest_lumos_step("lumos"))       #5
print(earliest_lumos_step("LULUMO"))      #-1
print(earliest_lumos_step("suaxwmol"))     #8
