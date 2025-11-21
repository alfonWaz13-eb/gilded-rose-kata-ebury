import pytest

from available_items import NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE, SULFURAS
from gilded_rose import GildedRose, Item


class TestGeneralRules:

    @pytest.mark.parametrize("product", [NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE])
    def test_sell_in_days_decreases_one_day_every_day_except_sulfuras(self, product):
        item = Item(name=product, sell_in=10, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == 9

    def test_sulfuras_never_decreases_the_sell_in_value(self):
        item = Item(name=SULFURAS, sell_in=10, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.sell_in == 10

    @pytest.mark.parametrize("product", [NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE, SULFURAS])
    def test_quality_is_never_negative(self, product):
        item = Item(name=product, sell_in=10, quality=0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality >= 0

    @pytest.mark.parametrize("product", [NORMAL_ITEM, BACKSTAGE_PASS, AGED_BRIE])
    def test_quality_of_an_item_except_sulfuras_is_never_more_than_50(self, product):
        item = Item(name=product, sell_in=10, quality=50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality <= 50


class TestNormalItem:

    def test_quality_degrades_one_point_before_sell_date(self):
        item = Item(name=NORMAL_ITEM, sell_in=10, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 9

    def test_once_the_sell_by_date_has_passed_normal_items_quality_decreases_twice_as_fast(self):
        item = Item(name=NORMAL_ITEM, sell_in=0, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 8


class TestAgedBrie:

    def test_brie_increases_its_quality_in_one_the_older_it_gets(self):
        item = Item(name=AGED_BRIE, sell_in=20, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 11

    def test_brie_increases_its_quality_in_two_the_older_it_gets_when_sell_in_date_has_passed(self):
        item = Item(name=AGED_BRIE, sell_in=-5, quality=10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 12


class TestSulfuras:

    def test_sulfuras_never_decreases_its_quality(self):
        item = Item(name=SULFURAS, sell_in=10, quality=35)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 35


class TestBackstagePasses:

    @pytest.mark.parametrize("days_left", [10, 6, 8])
    def test_quality_increases_in_2_when_sell_in_is_between_10_and_6_included(self, days_left):
        item = Item(name=BACKSTAGE_PASS, sell_in=days_left, quality=5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 7

    @pytest.mark.parametrize("days_left", [5, 1, 3])
    def test_quality_increases_in_3_when_sell_in_is_between_5_and_1_included(self, days_left):
        item = Item(name=BACKSTAGE_PASS, sell_in=days_left, quality=5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 8

    def test_quality_drops_to_0_after_the_concert(self):
        item = Item(name=BACKSTAGE_PASS, sell_in=0, quality=5)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        assert item.quality == 0