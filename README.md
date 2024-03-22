# PDF Splitter

This Python script allows you to split a PDF file into multiple subdivisions based on the desired number of pages per subdivision.

## Requirements

- Python 3.x
- PyPDF2 library

Install the required library using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/pdf-splitter.git
    cd pdf-splitter
    ```

2. **Run the script:**

    ```bash
    python split_pdf.py
    ```

3. **Follow the prompts to provide the path to the input PDF file, the directory to save the output subdivisions, and the number of pages per subdivision.**

4. **The script will split the PDF file according to your specifications and save the subdivisions in the specified output directory.**

## Example

Suppose you have a PDF file named `input.pdf` with 20 pages and you want to split it into subdivisions with 5 pages each:

- Input PDF file: `input.pdf`
- Output directory: `output_subdivisions`
- Pages per subdivision: 5

After running the script, you will get four subdivisions saved as `subdivision_1.pdf`, `subdivision_2.pdf`, `subdivision_3.pdf`, and `subdivision_4.pdf` in the `output_subdivisions` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
