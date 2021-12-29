import sqlite3

SELECT_FROM_PRODUCT = 'select * from product;'

with sqlite3.connect('shop.sqlite') as conn:
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

        if option == '1':
            cur = conn.execute(SELECT_FROM_PRODUCT)

            for line in cur:
                print("{:3}) {:17} | {:^10}| price:{:8.2f} | quantity:{:4}".format(*line))

        elif option == '2':
            min_price = input("enter minimum price:")
            max_price = input("enter max price:")

            cur = conn.execute('''
                SELECT *
                FROM product
                WHERE price  BETWEEN ? AND ?
            ''', (min_price, max_price))

            for line in cur:
                print("{:3}) {:17} | {:^10}| price:{:8.2f} | quantity:{:4}".format(*line))

        elif option == '3':
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

        elif option == '4':
            product_id = input("enter product ID:")
            price_sub = input("how much to increase")

            cur = conn.execute('''
                UPDATE product
                SET price = price - ?
                WHERE product_id = ? 
            ''', (price_sub, product_id))

            conn.commit()

            if cur.rowcount == 0:
                print("could not update id:", product_id)
            else:
                print("updated successfully")
        elif option == '5':
            pid = input("enter product ID to delete:")

            product = conn.execute('''
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
                    cur = conn.execute("""
                        DELETE FROM product
                        WHERE product_id = ? 
                    """, (pid,))

                    if cur.rowcount == 0:
                        print("ID not found!")
                    else:
                        print(pid, "deleted")

                    conn.commit()

        elif option == '0':
            break
        else:
            print("invalid option.")