# Import CSV files into MySQL table
from import_data.insert_query import InsertQuery
from import_data.sql_connection import SQLConnection


class ImportData:

    def __init__(self, file_names: list):
        self.file_names = file_names

    def open_file(self):
        sql_connection = SQLConnection("localhost", "root", "dance").connect()
        cursor = sql_connection.cursor()

        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as f:
                lines = (line for line in f)
                column_names = next(lines).split(",")
                insert_data = InsertQuery()

                line_number = 0
                for current_line in lines:
                    line_number += 1
                    sql_query = insert_data.query_create(column_names, current_line)
                    if sql_query == "No query":
                        continue

                    cursor.execute(sql_query)
                    sql_connection.commit()

        cursor.close()
