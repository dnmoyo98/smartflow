# SmartFlow

SmartFlow is a Python-based application offering advanced file compression options on Windows, aimed at reducing file sizes for storage and transfer. It provides functionality to compress files into ZIP archives and compress/decompress individual files using GZIP.

## Features

- Compress all files in a directory into a ZIP archive.
- Compress individual files using GZIP.
- Decompress GZIP files.

## Installation

SmartFlow requires Python 3.6 or higher.

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/smartflow.git
   cd smartflow
   ```

2. Install the required packages (if any are added in future development):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from smartflow import SmartFlow

# Initialize SmartFlow with the path to the directory containing files
sf = SmartFlow('path_to_directory')

# Compress all files in the directory into a ZIP file
sf.compress_zip('compressed_archive_name')

# Compress a single file using GZIP
sf.compress_gzip('file_name.txt')

# Decompress a GZIP file
sf.decompress_gzip('file_name.txt.gz')
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

Created by [Your Name](https://github.com/yourusername) - feel free to contact me!