import unittest

from LargestProductSeries import LargestProductSeries


class LargestProductSeriesTest(unittest.TestCase):
    def test_trivial(self):
        num = 123456789
        self.assertEquals(72, LargestProductSeries.findLargestProductSeries(num, 2))

    def test_largeScaleSmallProbe(self):
        num = 73167176531331624919225119674426574742355349194934969835213127745163262395783181169848118694788518438586156178911294949545951173795833195285321881551112541698747158523863151715693291963295227443143557668966489514452445231617318564131987111217223831136222989342338131813533627661428281644448664523874931358917296291491561441772391713811515859317961866711724271218839987979187922749219116997218881937766572733311115336788122123542181975125454159475224352584917711671556113614839586446716324415722155397536978179778461741649551492918625693219784686224828397224137565715615749126141797296865241453511147482166371484413199891118895243451658541227588666881164271714799244429282318634656748139191231628245861786645835912456652947654568284891288314261769114224219122671155626321111119371544217516941658961418171984138519624554443629812319878799272442849191888458115616619791913387549921152416368991256171761615886116467119415177541112256983155211155935729725716362695618826714282524836118232575314217529634511
        self.assertEquals(81, LargestProductSeries.findLargestProductSeries(num, 2))

    def test_middle(self):
        num = 1234567654321
        self.assertEquals(252, LargestProductSeries.findLargestProductSeries(num, 3))


if __name__ == '__main__':
    unittest.main()
