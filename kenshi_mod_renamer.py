import os
import argparse

def rename_mod_folders_from_steam(directory, dry_run=False):
    print(f"Processing directory: {directory}")

    for item in os.listdir(directory):
        folder_path = os.path.join(directory, item)

        if os.path.isdir(folder_path):
            mod_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".mod")]

            if not mod_files:
                print(f"  Warning: No .mod file found in folder '{item}'. Skipping.")
                continue  # Skip to the next folder

            if len(mod_files) > 1:
                print(f"  Warning: Multiple .mod files found in folder '{item}'. Using the first one: '{mod_files[0]}'.")

            mod_file_name = mod_files[0]
            new_folder_name = os.path.splitext(mod_file_name)[0]  # Remove the .mod extension
            new_folder_path = os.path.join(directory, new_folder_name)

            if item == new_folder_name:
                print(f"  Folder '{item}' already named after the .mod file. Skipping.")
                continue

            if dry_run:
                print(f"  Dry Run: Would rename folder '{item}' to '{new_folder_name}'")
            else:
                try:
                    os.rename(folder_path, new_folder_path)
                    print(f"  Renamed folder '{item}' to '{new_folder_name}'")
                except OSError as e:
                    print(f"  Error renaming folder '{item}' to '{new_folder_name}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Rename folders based on .mod files within them.")
    parser.add_argument("directory", nargs='?', default=os.getcwd(), help="The directory containing folders to rename (defaults to current directory).")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Perform a dry run, showing changes without renaming.")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
        return

    rename_mod_folders_from_steam(args.directory, args.dry_run)
    print("\nFolder renaming process completed.")

if __name__ == "__main__":
    main()
