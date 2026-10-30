"""B14 auxiliary: compute sexagenary index and xun-kong for given day ganzhi only. No case data."""
stems="甲乙丙丁戊己庚辛壬癸"
branches="子丑寅卯辰巳午未申酉戌亥"
def idx(s):
    g=s[0]; z=s[1]
    for i in range(60):
        if stems[i%10]==g and branches[i%12]==z:
            return i+1
    return None
for day in ["丙戌","乙巳","戊子","戊申","壬辰","辛巳","戊戌","庚子","辛丑","丁亥","丁卯","辛未","壬子","丙辰","癸丑","乙未","丁卯","乙卯","戊辰","辛巳","己巳"]:
    i=idx(day)
    if i:
        xun_start = i - (i-1)%10  # first of xun (jia...)
        # kong branches are the two not covered in 10
        start_branch_idx = branches.index("甲子"[1])  # placeholder
        # compute: xun start branch
        sb = branches[(xun_start-1)%12]
        covered=[branches[(branches.index(sb)+k)%12] for k in range(10)]
        kong=[b for b in branches if b not in covered]
        print(day, i, "xun_start_index", xun_start, "start_branch", sb, "kong", kong)
