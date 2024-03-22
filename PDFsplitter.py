import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_dir, pages_per_subdivision):
    with open(input_path, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)
        num_pages = len(pdf_reader.pages)

        # Calculate number of subdivisions
        num_subdivisions = num_pages // pages_per_subdivision
        if num_pages % pages_per_subdivision != 0:
            num_subdivisions += 1

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Split PDF into subdivisions
        for i in range(num_subdivisions):
            start_page = i * pages_per_subdivision
            end_page = min((i + 1) * pages_per_subdivision, num_pages)
            output_pdf_path = os.path.join(output_dir, f'subdivision_{i+1}.pdf')

            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer = PdfWriter()
                for page_num in range(start_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                pdf_writer.write(output_file)

            print(f'Subdivision {i+1} saved as: {output_pdf_path}')

if __name__ == "__main__":
    input_path = input("Enter the path to the input PDF file: ")
    output_dir = input("Enter the directory to save the output subdivisions: ")
    pages_per_subdivision = int(input("Enter the number of pages per subdivision: "))

    split_pdf(input_path, output_dir, pages_per_subdivision)
