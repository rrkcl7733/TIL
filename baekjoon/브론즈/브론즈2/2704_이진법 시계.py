def to_binary_clock(h, m, s):
    h_bin = bin(h)[2:].zfill(6)
    m_bin = bin(m)[2:].zfill(6)
    s_bin = bin(s)[2:].zfill(6)

    col3 = ""
    for i in range(6):
        col3 += h_bin[i] + m_bin[i] + s_bin[i]

    row3 = h_bin + m_bin + s_bin

    return col3, row3


for _ in range(int(input())):
    h, m, s = map(int, input().split(":"))
    col3, row3 = to_binary_clock(h, m, s)
    print(col3, row3)
