import pytest

from available_items import NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE, SULFURAS
from gilded_rose import GildedRose, Item


def test_normal_item_quality_degrades_one_point_before_sell_date():
    item = Item(name=NORMAL_ITEM, sell_in=10, quality=10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 9


@pytest.mark.parametrize("product", [NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE])
def test_normal_item_sell_in_days_decreases_one_day_every_day_for_every_product_except_sulfuras(product):
    item = Item(name=product, sell_in=10, quality=10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 9


def test_sulfuras_never_decreases_the_sell_in_value():
    item = Item(name=SULFURAS, sell_in=10, quality=10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 10