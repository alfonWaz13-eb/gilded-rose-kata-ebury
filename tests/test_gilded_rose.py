import pytest

from available_items import NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE, SULFURAS
from gilded_rose import GildedRose, Item


def test_normal_item_quality_degrades_one_point_before_sell_date():
    item = Item(name=NORMAL_ITEM, sell_in=10, quality=10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.name == "foo"
    assert item.quality == 9