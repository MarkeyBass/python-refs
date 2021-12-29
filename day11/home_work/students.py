import sqlite3
import re


def show_all(conn):
    cur = conn.execute("""
        SELECT rowid, * FROM student; 
    """)

    if cur.rowcount == 0:
        print("No students in the database")
    else:
        print("rowid | firstname {:2}| lastname {:7}| final score {:3} ".format("", "", ""))
        print("--------------------------------------------------")
        for student in cur:
            print("{:4}) | {:11} | {:15} | {:3} \n".format(*student))


def add_student(conn):
    try:
        new_student = {
            "firstname": input("Enter firstname: "),
            "lastname": input("Enter lastname: "),
            "score": int(input("Enter final score (0 - 100): "))
        }
    except TypeError:
        print("score must be an int")
        return
    else:
        if new_student["score"] > 100 or new_student["score"] < 0:
            print("score must be in the rang (0 - 100)")
            return
        cur = conn.execute(
            """
                INSERT INTO student VALUES (?, ?, ?)
            """, (new_student["firstname"], new_student["lastname"], new_student["score"])
        )
        conn.commit()
        print(cur.rowcount, "rows have been affected!")


def show_by_score_and_higher(conn):
    try:
        score = int(input("Enter minimum score to show scores (0 - 100)"))
    except ValueError:
        print("Wrong input!")
        return
    if score < 0 or score > 100:
        print("Wrong input!")
        return
    else:
        query = """
            SELECT rowid, * 
            FROM student
            WHERE score >= ?
        """

        cur = conn.execute(query, (score,))
        print("rowid | firstname {:2}| lastname {:7}| final score {:3} ".format("", "", ""))
        print("--------------------------------------------------")
        for student in cur:
            print("{:4}) | {:11} | {:15} | {:3} \n".format(*student))


def remove_student(conn):
    try:
        student_row_id = int(input("Enter rowid of student to delete"))
    except ValueError:
        print("Wrong input! rowid must be a number.")
        return
    else:
        cur = conn.execute("""
            DELETE FROM student WHERE rowid = ?
        """, (student_row_id,))

        if cur.rowcount == 0:
            print("rowid not found")
        else:
            print(f"Student with the id of ({student_row_id}) was removed")


student_dic = {
    1: show_all,
    2: add_student,
    3: show_by_score_and_higher,
    4: remove_student
}

if __name__ == "__main__":
    with sqlite3.connect("school.sqlite") as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS student(
                 firstname TEXT,
                 lastname TEXT,
                 score INT
            )"""
        )

        quit_program = False
        while not quit_program:
            print("""
                Student menu:
                1) Show all students
                2) Add a student
                3) Show by min score and above
                4) Delete student
                0) Quite the program
            """)

            option = None
            while True:
                option = input("enter option number (0 - 4): ")

                if re.search("[0-4]", option):
                    option = int(option)
                    if int(option) == 0:
                        quit_program = True
                        print("GOODBYE!!!")
                        break
                    student_dic[option](connection)
                else:
                    print("wrong input")
                    break
