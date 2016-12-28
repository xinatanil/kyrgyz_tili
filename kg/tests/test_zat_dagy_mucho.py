# coding=utf-8

from kg.lang.bashka._dagy import DagyZatMuchosu
from kg.lang.lang import KyrgyzWord
from kg.tests import KGTestCase


class ZatDagyMuchoTest(KGTestCase):
    def test_1(self):
        data = self.get_data()

        for word, expected_form in data.items():
            affix = DagyZatMuchosu(KyrgyzWord(word))
            self.assertEqual(affix.make(), expected_form)

    def get_data(self):
        return {
            u'негиздөөчү': u'негиздөөчүдөгү',
            u'бушайман': u'бушаймандагы',
            u'бадыран': u'бадырандагы',
            u'эс-акыл': u'эс-акылдагы',
            u'көпүрө': u'көпүрөдөгү',
            u'качыр': u'качырдагы',
            u'чоорчу': u'чоорчудагы',
            u'коменданты': u'комендантыдагы',
            u'тармал': u'тармалдагы',
            u'тартыш': u'тартыштагы',
            u'кап': u'каптагы',
            u'новокаин': u'новокаиндеги',
            u'жарк': u'жарктагы',
            u'кут': u'куттагы',
            u'амалкөйлүк': u'амалкөйлүктөгү',
            u'айбан': u'айбандагы',
            u'сүзмө': u'сүзмөдөгү',
            u'көр': u'көрдөгү',
            u'символика': u'символикадагы',
            u'кызматчы': u'кызматчыдагы',
            u'кесип': u'кесиптеги',
            u'нускама': u'нускамадагы',
            u'жоруш': u'жоруштагы',
            u'энциклопедия': u'энциклопедиядагы',
            u'цемент': u'цементтеги',
            u'түп нуска': u'түп нускадагы',
            u'гранит': u'граниттеги',
            u'тообо': u'тоободогу',
            u'үй': u'үйдөгү',
            u'бажы': u'бажыдагы',
            u'сака': u'сакадагы',
            u'түтүк': u'түтүктөгү',
            u'жубарымбек': u'жубарымбектеги',
            u'сооп': u'сооптогу',
            u'күнгөй': u'күнгөйдөгү',
            u'олигарх': u'олигархтагы',
            u'магистратура': u'магистратурадагы',
            u'такай': u'такайдагы',
            u'даярдоочу': u'даярдоочудагы',
            u'марс': u'марстагы',
            u'тамарка': u'тамаркадагы',
            u'дем': u'демдеги',
            u'кылмыш': u'кылмыштагы',
            u'танапис': u'танапистеги',
            u'том': u'томдогу',
            u'жанр': u'жанрдагы',
            u'адамгерчиликте': u'адамгерчиликтедеги',
            u'доллар': u'доллардагы',
            u'бактерия': u'бактериядагы',
        }