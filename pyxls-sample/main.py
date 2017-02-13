import os
import re
from datetime import datetime

import xlrd
import xlwt
from xlrd.sheet import Sheet
from xlwt import Worksheet


def main_logic():
    # 1. Get input files
    input_file_names = get_input_file_names('resources/input_files/')

    # 2. Make output file
    output_book = xlwt.Workbook()
    output_sheet = output_book.add_sheet('Sheet')

    # 3. loop for input files
    for idx, file_name in enumerate(input_file_names):
        # 3.1. Open the input file
        book = xlrd.open_workbook('resources/input_files/{file_name}'.format(file_name=file_name))
        sheet = book.sheet_by_index(0)

        # 3.2. Pick up the values needed
        student_info = read_student_info(sheet, file_name)

        # 3.3. Write the values into the output file
        write_student_info(output_sheet, student_info, idx + 1)

    # 4. Save output file
    output_book.save('resources/output_{time}.xls'.format(time=datetime.now().strftime("%Y%m%d_%H%M%S")))


# 1. Get input files
def get_input_file_names(directory_name: str) -> list:
    files = os.listdir(directory_name)
    file_name_pattern = 'student_[0-9]+\.xlsx'
    files = [x for x in files if re.match(file_name_pattern, x)]  # Filter by file name pattern
    print('[get_input_files] ' + str(files))
    return files


# 3.2. Pick up the values needed
def read_student_info(sheet: Sheet, file_name: str) -> dict:
    student_id = file_name.replace('student_', '').replace('.xlsx', '')
    student_name = sheet.cell(0, 4).value
    student_score = round(sheet.cell(15, 4).value, 1)
    print('[read_student_info]\t' + student_id + ' : ' + student_name + ' : ' + str(student_score))
    return {'id': student_id, 'name': student_name, 'score': student_score}


# 3.3. Write the values into the output file
def write_student_info(sheet: Worksheet, student_info: dict, row_num: int) -> None:
    sheet.write(row_num, 1, student_info['id'])
    sheet.write(row_num, 2, student_info['name'])
    sheet.write(row_num, 3, student_info['score'])
    print('[write_student_info]')


if __name__ == '__main__':
    main_logic()
