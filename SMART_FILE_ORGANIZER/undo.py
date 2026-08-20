import shutil
from logger import log_info, log_error


def undo_operations(operations):

    if not operations:

        print("\nNothing to undo.")

        return

    print("\nUndoing last operation...\n")

    for destination, original in reversed(
        operations
    ):

        try:

            if destination.exists():

                shutil.move(
                    str(destination),
                    str(original)
                )

                print(
                    f"Restored: "
                    f"{destination.name}"
                )

                log_info(
                    f"Undo: "
                    f"{destination} -> {original}"
                )

        except Exception as error:

            print(
                f"Could not restore "
                f"{destination.name}"
            )

            log_error(
                f"Undo error: {error}"
            )

    operations.clear()

    print("\nUndo completed.")