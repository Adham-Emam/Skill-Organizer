import sqlite3
import sys

input_message = """
What do you want to do?
1 => Show all skilss
2 => Add a new skill
3 => Delete a skill
4 => Update skill progress
5 => close app
"""


def main():
    user_input = int(input(input_message))

    # Check if input valid
    if user_input in [1, 2, 3, 4, 5]:
        run_command(user_input)
    else:
        print("Please type a number from above")


def run_command(cmd):
    # Start Database
    db = sqlite3.connect("skills.db")
    cr = db.cursor()
    cr.execute(
        """CREATE TABLE if not exists skills(
            skill TEXT,
            progress INTEGER
            )
        """
    )

    if cmd == 1:
        show_skills(cr)
    elif cmd == 2:
        add_skill(cr)
        db.commit()
    elif cmd == 3:
        delete_skill(cr)
        db.commit()
    elif cmd == 4:
        update_skill(cr)
        db.commit()
    elif cmd == 5:
        print("GoodBye")
        db.close()
        sys.exit()


def show_skills(cr):
    cr.execute("SELECT * FROM skills")

    for key, skill in enumerate(cr.fetchall()):
        print(f"{key + 1}: Skill => {skill[0]}, Progress => {skill[1]}%")


def add_skill(cr):
    skill = input("Type your skill: ").strip()
    progress = input("Type your progress: ").strip()
    cr.execute(f"INSERT INTO skills(skill, progress) values('{skill}', '{progress}')")
    print("Skill added")


def delete_skill(cr):
    print()
    cr.execute("SELECT * FROM skills")

    for key, skill in enumerate(cr.fetchall()):
        print(f"{key + 1}: Skill => {skill[0]}, Progress => {skill[1]}%")

    skill = input("Type the skill name you want to delete: ").strip()
    cr.execute(f"DELETE FROM skills WHERE skill = '{skill}'")


def update_skill(cr):
    print()
    cr.execute("SELECT * FROM skills")

    for key, skill in enumerate(cr.fetchall()):
        print(f"{key + 1}: Skill => {skill[0]}, Progress => {skill[1]}%")

    skill = input("Type the skill name you want to update: ").strip()
    new_progress = int(input("New skill progress: "))
    cr.execute(f"UPDATE skills SET progress = '{new_progress}' WHERE skill = '{skill}'")


if __name__ == '__main__':
    main()
