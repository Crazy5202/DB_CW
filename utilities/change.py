import re

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    pattern = r"COMMENT\s+ON\s+(?:TABLE|COLUMN)\s+(\w+(?:\.\w+)?)\s+IS\s+'([^']+)'"

    matches = re.findall(pattern, content)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        current_table = None 

        for match in matches:
            table_or_column, comment = match

            if '.' not in table_or_column:
                if current_table is not None and current_table != table_or_column:
                    output_file.write('\n')
                current_table = table_or_column

            if '.' in table_or_column:
                column_name = table_or_column.split('.', 1)[1]
            else:
                column_name = table_or_column

            output_file.write(f"{column_name} - {comment}\n")

input_file_path = './migrations/ddl.sql'
output_file_path = 'output.txt'
process_file(input_file_path, output_file_path)