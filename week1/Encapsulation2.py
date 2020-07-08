class employee():
    def __init__(self):
        self._maxearn = 30000
    def earn(self):
        print("earning is:{}".format(self._maxearn))
    def setmaxearn(self, earn):
        self._maxearn = earn

emp1 = employee()
emp1.earn()

emp1._maxearn = 10000
emp1.earn()

emp1.setmaxearn(15000)
emp1.earn()