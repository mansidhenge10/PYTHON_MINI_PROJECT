from pathlib import Path
import shutil
import hashlib
from datetime import datetime

from config import get_category
from logger import log_info, log_error


class FileOrganizer:

    def __init__(self, source_directory):

        self.source_directory = Path(source_directory)

        if not self.source_directory.exists():
            raise FileNotFoundError(
                "The selected directory does not exist."
            )

        if not self.source_directory.is_dir():
            raise NotADirectoryError(
                "The selected path is not a directory."
            )

        self.operations = []


    # -----------------------------------
    # Find NEW / UNORGANIZED files
    # -----------------------------------

    def get_files(self):

        files = []

        # These folders are created by the organizer.
        # Files inside these folders are already organized.
        ignored_folders = {
            "Images",
            "Documents",
            "Videos",
            "Audio",
            "Archives",
            "Code",
            "Others",
            "Duplicates"
        }

        for item in self.source_directory.rglob("*"):

            if not item.is_file():
                continue

            # Get the path relative to TEST_FILES
            relative_parts = item.relative_to(
                self.source_directory
            ).parts

            # Example:
            # Images / 2026 / August / photo.jpg
            #
            # relative_parts[:-1] gives:
            # Images, 2026, August

            if any(
                folder in ignored_folders
                for folder in relative_parts[:-1]
            ):
                continue

            files.append(item)

        return files


    # -----------------------------------
    # Show already organized files
    # -----------------------------------

    def show_organized_files(self):

        print("\n" + "=" * 60)
        print("              ORGANIZED FILES")
        print("=" * 60)

        found_files = False

        categories = [
            "Images",
            "Documents",
            "Videos",
            "Audio",
            "Archives",
            "Code",
            "Others",
            "Duplicates"
        ]

        for category in categories:

            category_folder = (
                self.source_directory / category
            )

            if not category_folder.exists():
                continue

            files = [
                file
                for file in category_folder.rglob("*")
                if file.is_file()
            ]

            if not files:
                continue

            found_files = True

            print(f"\n📁 {category}")

            for file in files:

                relative_path = file.relative_to(
                    category_folder
                )

                parts = relative_path.parts

                # New format:
                # Year / Month / filename

                if len(parts) >= 3:

                    year = parts[0]
                    month = parts[1]
                    filename = parts[-1]

                    print(
                        f"   └── {filename}"
                    )

                    print(
                        f"       📅 Date: "
                        f"{year} / {month}"
                    )

                else:

                    # Files organized before the
                    # Year/Month feature was added

                    filename = file.name

                    modification_time = (
                        file.stat().st_mtime
                    )

                    date = datetime.fromtimestamp(
                        modification_time
                    )

                    year = str(date.year)

                    month = date.strftime("%B")

                    print(
                        f"   └── {filename}"
                    )

                    print(
                        f"       📅 Date: "
                        f"{year} / {month}"
                    )

        if not found_files:

            print(
                "\nNo organized files found."
            )

        print("\n" + "=" * 60)


    # -----------------------------------
    # Create category + Year + Month
    # -----------------------------------

    def create_category_folder(
        self,
        category,
        year,
        month
    ):

        folder = (
            self.source_directory /
            category /
            year /
            month
        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder


    # -----------------------------------
    # Rename conflicting files
    # -----------------------------------

    def get_unique_filename(
        self,
        destination
    ):

        if not destination.exists():

            return destination

        counter = 1

        while True:

            new_name = (
                f"{destination.stem}_"
                f"{counter}"
                f"{destination.suffix}"
            )

            new_destination = (
                destination.parent /
                new_name
            )

            if not new_destination.exists():

                return new_destination

            counter += 1


    # -----------------------------------
    # Calculate SHA-256 hash
    # -----------------------------------

    def calculate_hash(
        self,
        file_path
    ):

        sha256 = hashlib.sha256()

        try:

            with open(
                file_path,
                "rb"
            ) as file:

                while True:

                    data = file.read(8192)

                    if not data:
                        break

                    sha256.update(data)

            return sha256.hexdigest()

        except Exception as error:

            log_error(
                f"Hash error for "
                f"{file_path}: {error}"
            )

            return None


    # -----------------------------------
    # Find duplicate
    # -----------------------------------

    def find_duplicate(
        self,
        file_path,
        category_folder
    ):

        file_hash = (
            self.calculate_hash(
                file_path
            )
        )

        if file_hash is None:
            return False

        # Search all files inside:
        # Category / Year / Month

        for existing_file in (
            category_folder.rglob("*")
        ):

            if not existing_file.is_file():
                continue

            existing_hash = (
                self.calculate_hash(
                    existing_file
                )
            )

            if existing_hash == file_hash:

                return True

        return False


    # -----------------------------------
    # Get Year and Month
    # -----------------------------------

    def get_date_folder(
        self,
        file_path
    ):

        """
        Get the year and month based on
        the file's last modification date.
        """

        modification_time = (
            file_path.stat().st_mtime
        )

        date = datetime.fromtimestamp(
            modification_time
        )

        year = str(date.year)

        month = date.strftime("%B")

        return year, month


    # -----------------------------------
    # Organize files
    # -----------------------------------

    def organize(self):

        files = self.get_files()

        # -----------------------------------
        # No new files
        # -----------------------------------

        if not files:

            print(
                "\nNo new files to organize."
            )

            self.show_organized_files()

            return


        print(
            "\nStarting file organization...\n"
        )


        # -----------------------------------
        # Process each file
        # -----------------------------------

        for file_path in files:

            try:

                # -----------------------------------
                # Get Year and Month
                # -----------------------------------

                year, month = (
                    self.get_date_folder(
                        file_path
                    )
                )


                # -----------------------------------
                # Get file extension
                # -----------------------------------

                extension = file_path.suffix


                # -----------------------------------
                # Get category
                # -----------------------------------

                category = get_category(
                    extension
                )


                # -----------------------------------
                # Display information
                # -----------------------------------

                print(
                    f"File: {file_path.name}"
                )

                print(
                    f"Category: {category}"
                )

                print(
                    f"Date: {year} / {month}"
                )


                # -----------------------------------
                # Create:
                #
                # Category
                #     ↓
                # Year
                #     ↓
                # Month
                # -----------------------------------

                category_folder = (
                    self.create_category_folder(
                        category,
                        year,
                        month
                    )
                )


                # -----------------------------------
                # Check duplicate
                # -----------------------------------

                if self.find_duplicate(
                    file_path,
                    category_folder
                ):

                    duplicate_folder = (
                        self.source_directory /
                        "Duplicates"
                    )

                    duplicate_folder.mkdir(
                        exist_ok=True
                    )


                    destination = (
                        duplicate_folder /
                        file_path.name
                    )


                    destination = (
                        self.get_unique_filename(
                            destination
                        )
                    )


                    shutil.move(
                        str(file_path),
                        str(destination)
                    )


                    self.operations.append(
                        (
                            destination,
                            file_path
                        )
                    )


                    print(
                        f"Result: Duplicate"
                    )

                    print(
                        f"Moved to: "
                        f"{destination}"
                    )


                    log_info(
                        f"Duplicate moved: "
                        f"{file_path} -> "
                        f"{destination}"
                    )

                    print()

                    continue


                # -----------------------------------
                # Normal file destination
                # -----------------------------------

                destination = (
                    category_folder /
                    file_path.name
                )


                # -----------------------------------
                # Handle same filename
                # -----------------------------------

                destination = (
                    self.get_unique_filename(
                        destination
                    )
                )


                # -----------------------------------
                # Move file
                # -----------------------------------

                shutil.move(
                    str(file_path),
                    str(destination)
                )


                # -----------------------------------
                # Save operation for Undo
                # -----------------------------------

                self.operations.append(
                    (
                        destination,
                        file_path
                    )
                )


                print(
                    f"Result: Moved successfully"
                )

                print(
                    f"Location: "
                    f"{category}/{year}/{month}"
                )

                print("-" * 40)


                log_info(
                    f"Moved: "
                    f"{file_path} -> "
                    f"{destination}"
                )


            except Exception as error:

                print(
                    f"Error processing "
                    f"{file_path.name}: "
                    f"{error}"
                )


                log_error(
                    f"Error processing "
                    f"{file_path}: "
                    f"{error}"
                )


        print(
            "\nOrganization completed."
        )

        print(
            "\nCurrent organized files:"
        )

        self.show_organized_files()