def simplify(poly):
    monomials = [re.search(r'([+-]?\d*)([a-z]+)', monomial).groups() for monomial in re.findall(r'[+-]?\w+', poly)]
    sorted_monomials = sorted([[int(monomial[0] if monomial[0] not in ['+', '-'] else f"{monomial[0]}1") if monomial[
        0] else 1, ''.join(sorted(monomial[1]))] for monomial in monomials],
                              key=lambda monomial: (len(monomial[1]), monomial[1]))
                              