import os.path


class Product:
    def __init__(self, name: str, weidht:float, category: str):
        self.name = name
        self.weight = weidht
        self.category = category

    def __str__(self):
        products_str = (f'{self.name}, {self.weight}, {self.category}')
        return products_str


class Shop:

    def __init__(self):
        self.__file_name = open('product.txt')
        self.__file_name.close()

    def get_products(self):
        get_file = open('products.txt', 'r', encoding='utf-8')
        name_product = get_file.read()
        get_file.close()
        return name_product

    def add (self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a+', encoding='utf-8')
                file.write(f'{str(product)}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


if __name__=='__main__':


    print('-------------------------------------------')
    s1 = Shop()
    p1 = Product('Potato', 50.5,'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)
    s1.add(p1, p2, p3)
    print(s1.get_products())

    print('--------------------------------------------')

