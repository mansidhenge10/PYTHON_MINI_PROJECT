from organizer import FileOrganizer
from undo import undo_operations


def main():

    print("=" * 50)
    print("        SMART FILE ORGANIZER")
    print("=" * 50)

    directory = input(
        "\nEnter the folder path to organize: "
    ).strip()

    try:

        organizer = FileOrganizer(directory)

    except FileNotFoundError as error:

        print(f"\nError: {error}")
        return

    while True:

        print("\n")
        print("1. Organize New Files")
        print("2. Show Organized Files")
        print("3. Undo Last Operation")
        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # -----------------------------------
        # Organize
        # -----------------------------------

        if choice == "1":

            organizer.organize()

        # -----------------------------------
        # Show organized files
        # -----------------------------------

        elif choice == "2":

            organizer.show_organized_files()
            

        # -----------------------------------
        # Undo
        # -----------------------------------

        elif choice == "3":

            undo_operations(
                organizer.operations
            )

        # -----------------------------------
        # Exit
        # -----------------------------------

        elif choice == "4":

            print(
                "\nThank you for using "
                "Smart File Organizer!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


if __name__ == "__main__":
    main()