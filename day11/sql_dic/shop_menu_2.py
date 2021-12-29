import sqlite3
import re


def show_all(connection):
    SELECT_FROM_PRODUCT = 'select * from product;'
    cursor = connection.execute(SELECT_FROM_PRODUCT)
    for line in cursor:
        print("{:3}) {:17} | {:^10}| price:{:8.2f} | quantity:{:4}".format(*line))


def show_in_price_range(connection):
    min_price = input("enter minimum price:")
    max_price = input("enter max price:")

    cursor = connection.execute('''
                    SELECT *
                    FROM product
                    WHERE price  BETWEEN ? AND ?
                ''', (min_price, max_price))

    for line in cursor:
        print("{:3}) {:17} | {:^10}| price:{:8.2f} | quantity:{:4}".format(*line))


def increase_price(conn):
    product_id = input("enter product ID:")
    price_add = input("how much to increase")

    cur = conn.execute('''
        UPDATE product
        SET price = price + ?
        WHERE product_id = ? 
    ''', (price_add, product_id))

    conn.commit()

    if cur.rowcount == 0:
        print("could not update id:", product_id)
    else:
        print("updated successfully")


def decrease_price(connection):
    product_id = input("enter product ID:")
    price_sub = input("how much to increase")

    cur = connection.execute('''
                    UPDATE product
                    SET price = price - ?
                    WHERE product_id = ? 
                ''', (price_sub, product_id))

    connection.commit()

    if cur.rowcount == 0:
        print("could not update id:", product_id)
    else:
        print("updated successfully")


def delete_product(connection):
    pid = input("enter product ID to delete:")

    product = connection.execute('''
        select *
        from product
        where product_id = ?
    ''', (pid,)).fetchone()

    if product is None:
        print("no such ID")
    else:

        print("you are about to delete the following product:")
        print("{:3}) {:17} | {:^10}| price:{:8.2f} | quantity:{:4}".format(*product))

        answer = input("are you sure you want to delete? (y/N)").lower()
        if answer == 'y':
            cur = connection.execute("""
                DELETE FROM product
                WHERE product_id = ? 
            """, (pid,))

            if cur.rowcount == 0:
                print("ID not found!")
            else:
                print(pid, "deleted")

            connection.commit()


menu_dic = {
    1: show_all,
    2: show_in_price_range,
    3: increase_price,
    4: decrease_price,
    5: delete_product
}

# MAIN

if __name__ == "__main__":
    with sqlite3.connect('shop2.sqlite') as conn:
        while True:
            option = None
            while True:
                print("""
                        Shop Menu:
                        1) Show All
                        2) Show in price range
                        3) Increase Price
                        4) Decrease Price
                        5) Delete Product
                        0) Exit
                        """)
                option = input("enter option number:")
                if re.search("[0-9]", option):
                    option = int(option)
                    break
                else:
                    print("wrong input")

            if option == 0:
                break
            else:
                menu_dic[option](conn)



