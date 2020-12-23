import season


def discount(season_):
    if season_ not in [season.SUMMER, season.WINTER, season.SPRING, season.FALL]:
        raise TypeError(f'arguments are expected to either of four values '
                        f'season.SUMMER, season.WINTER, season.SPRING, season.FALL')
    if season_ == season.SUMMER:
        return 0.2
    else:
        return 0.0


def price(season_, original_price):
    new_price = (1.0 - discount(season_)) * original_price
    return new_price


print(price(season.SUMMER, 120))
# print(price(None, 120))


def list_discount_for_all_season():
    for s in [season.SUMMER, season.WINTER, season.SPRING, season.FALL]:
        yield discount(s)


print(list(list_discount_for_all_season()))
