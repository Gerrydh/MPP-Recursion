#include <stdio.h>
#include <string>

struct Product {
    char* name;
    double price;
}

struct ProductStock {
    struct Product product;
    int quantity;
};

struct Shop {
    double cash;
    struct ProductStock stock[20];
};

struct Customer {
    char* name;
    double budget;
    struct ProductStock shoppingList[10];
};

void printProduct(struct Product p)
{
    printf("---------------------\n");
    printf("PRODUCT NAME: %s \nPRODUCT PRICE %.2f \n", p.name, p.price);
    printf("---------------------\n");
}

int main(void)
{
    struct Customer Ger = {"Ger", 100.00};
    printf("Customer name is %s\n", Ger.name);

    struct Product Coke = {"Can Coke", 1.10}
    printProduct(coke);

    struct ProductStock cokeStock = {coke, 20};
    printf("The store has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);
    return 0;
}