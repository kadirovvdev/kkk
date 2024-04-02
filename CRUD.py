class Computer:


     num_computers = 0

     def __init__(self, model, make, cpu, memory):
         self.model = model
         self.make = make
         self.cpu = cpu
         self.memory = memory
         Computer.num_computers += 1

     def get_info(self):
         return f"Model:{self.model}\nMake:{self.make}\nCPU:{self.cpu}\nMemory:{self.memory}"

     def __str__(self):
         return self.make, self.model

     def __repr__(self):
         return self.make, self.model


computer1 = Computer('MacBook Pro', 'Apple', 'Intel Core i7', '256GB')
computer2 = Computer('MacBook Pro M3', 'Apple', 'M3', '1024GB')
computer3 = Computer('MacBook Pro M1', 'Apple', 'M1', '16GB')
print(Computer.num_computers)
print(computer2.get_info())
print(computer3.__repr__())


class ComputerShop:

    num_shops = 0
    def __init__(self, name):
        self.name = name
        self.computers = []
        ComputerShop.num_shops += 1

    def add_computer(self, computer):
        if isinstance(computer, Computer):
            self.computers.append(computer)

    def __getitem__(self,index):
        return self.computers[index]

    def __len__(self):
        return len(self.computers)

    def delete_computer(self, index):
        del self.computers[index]



computer1 = Computer('MacBook Pro', 'Apple', 'Intel Core i7', '256GB')
computer2 = Computer('MacBook Pro M3', 'Apple', 'M3', '1024GB')
computer3 = Computer('MacBook Pro M1', 'Apple', 'M1', '16GB')
computer4 = Computer('MacBook Pro M2', 'Apple', 'M2', '512GB')

shop1 = ComputerShop('Enter Computers')
shop2 = ComputerShop('UPG')

shop1.add_computer(computer1)
shop1.add_computer(computer2)
shop1.add_computer(computer3)

shop2.add_computer(computer1)
shop2.add_computer(computer2)
shop2.add_computer(computer3)
shop2.add_computer(computer4)

shop2.delete_computer(1)
shop2.delete_computer(2)

for i in range(shop2.__len__()):
    print(f"{i+1}\n{shop2.computers[i].get_info()}\n")

print(ComputerShop.num_shops)
print(Computer.num_computers)