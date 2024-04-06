import subprocess


def compile_shared_library(source_files, output_file):
    """
    Compile source files into a shared library.

    Args:
        source_files (list): List of source file paths.
        output_file (str): Output shared library file path.
    """
    # Command to compile source files into a shared library
    compile_command = ["gcc", "-shared", "-o", output_file] + source_files

    try:
        # Run the compilation command
        subprocess.run(compile_command, check=True)
        print("Compilation successful.")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:", e)


# Example usage
if __name__ == "__main__":
    # List of source files to compile
    source_files = [
        "languages/tree-sitter-cpp/src/parser.c",
        "languages/tree-sitter-javascript/src/parser.c",
    ]  # Update with actual source files

    # Output shared library file
    output_file = (
        "build_languages/my-languages.so"  # Update with desired output file path
    )

    # Compile shared library
    compile_shared_library(source_files, output_file)
