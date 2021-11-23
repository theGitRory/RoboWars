class BulletManager():

    bulletArr = []

    @staticmethod
    def addBullets(bullet):
        BulletManager.bulletArr.append(bullet)

    def getBullets():
        return BulletManager.bulletArr
