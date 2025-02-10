import os
import zipfile
import gzip
import shutil
from pathlib import Path

class SmartFlow:
    def __init__(self, directory):
        self.directory = Path(directory)
        if not self.directory.is_dir():
            raise NotADirectoryError(f"{directory} is not a valid directory.")

    def compress_zip(self, output_filename):
        """Compress files in the directory to a ZIP archive."""
        output_path = self.directory / f"{output_filename}.zip"
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.directory):
                for file in files:
                    file_path = Path(root) / file
                    zipf.write(file_path, file_path.relative_to(self.directory))
        print(f"Files compressed to {output_path}")

    def compress_gzip(self, file_name):
        """Compress a single file in the directory using GZIP."""
        file_path = self.directory / file_name
        if not file_path.is_file():
            raise FileNotFoundError(f"{file_name} not found in the directory.")

        output_path = self.directory / f"{file_name}.gz"
        with open(file_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"{file_name} compressed to {output_path}")

    def decompress_gzip(self, gz_file_name):
        """Decompress a GZIP file in the directory."""
        gz_file_path = self.directory / gz_file_name
        if not gz_file_path.is_file() or not gz_file_path.suffix == '.gz':
            raise FileNotFoundError(f"{gz_file_name} not found or is not a .gz file in the directory.")

        output_path = self.directory / gz_file_path.stem
        with gzip.open(gz_file_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"{gz_file_name} decompressed to {output_path}")

# Example usage:
# sf = SmartFlow('path_to_directory')
# sf.compress_zip('archive_name')
# sf.compress_gzip('file_name.txt')
# sf.decompress_gzip('file_name.txt.gz')