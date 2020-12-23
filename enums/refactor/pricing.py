from season import Season, Dummy


def discount(season_):
    if season_ not in Season:
        raise TypeError(f'arguments are expected either of {len(Season)} values {list(Season)}')
    if season_ == Season.SUMMER:
        return 0.2
    else:
        return 0.0


def price(season_, original_price):
    new_price = (1.0 - discount(season_)) * original_price
    return new_price


print(price(Season.SUMMER, 120))
# print(price(Dummy.OTHER, 120))


def list_discount_for_all_season():
    for s in Season:
        yield discount(s)


print(list(list_discount_for_all_season()))
