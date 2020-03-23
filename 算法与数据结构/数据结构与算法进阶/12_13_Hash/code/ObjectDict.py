class People:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __hash__(self):
        """ 获取 index """
        return hash((self.name, self.age))
    
    def __eq__(self, other):
        """ 当 __hash__() 得到的 index 相同时，__eq__() 若返回 False, 则表不等，object 会存储在不同的位置 """
        return (self.name, self.age, self.salary) == (other.name, other.age, other.salary)
    
    def __ne__(self, other):
        """
        Not strictly neccessary, but to avoid having both x==y and x!=y
        True at the same time
        """
        return not(self == other)

    def __str__(self):
        return self.name + str(self.age) + str(self.salary)
    
    def eat(self):
        print("eat")
    
    def sleep(self):
        pass


if __name__ == "__main__":
    p1 = People("Tom", '1', 20)
    p5 = People("Tom", '1', 18)

    p2 = People("Zion", '2', 18)
    p3 = People("Adam", '3', 20)
    p4 = People("Alice", '4', 18)

    dic = {
        p1: 'A',    # 使用对象实例作为 key
        p2: 'B',
        p3: 'C',
        p4: 'D',
        p5: 'E',
    }
    print("-------------")
    print(dic)
    print("-------------")
    for key in dic:
        print(key, 'corresponds to', dic[key])