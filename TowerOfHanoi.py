def towerCalc(height, fromTower, withTower, toTower):
    if height >=1:
        towerCalc(height-1,fromTower, toTower, withTower)
        MoveTower(fromTower, toTower)
        towerCalc(height-1, withTower, fromTower, toTower)

def MoveTower(ft, tt):
    print('Mode disk from',ft,'to',tt)

towerCalc(3,'A','B','C')
