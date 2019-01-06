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

    def test_solution(self):
        num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
        self.assertEquals(23514624000, LargestProductSeries.findLargestProductSeries(num, 13))





if __name__ == '__main__':
    unittest.main()
