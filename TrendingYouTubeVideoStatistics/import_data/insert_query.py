# Insert Data with SQL Query

class InsertQuery:

    @staticmethod
    def query_create(columns, values):

        # Transform inner comma values to & before splitting
        values = values.replace(", ", "=&=")

        # Split the given string from CSV
        current_values = values.split(",")

        # Return the commas back to text.
        current_values = [v.replace("=&=", ", ") for v in current_values]

        # Add quotations to the unique ID
        current_values[0] = "\"" + current_values[0] + "\""

        # Transform the Date format
        date_value = current_values[1].split(".")
        current_values[1] = f"\"20{date_value[0]}.{date_value[2]}.{date_value[1]}\""

        # Cut non-necessary symbols of date-time format
        current_values[5] = "\"" + current_values[5][:-2] + "\""

        # Wrap the "Tags" value in quotations
        current_values[6] = '\'' + current_values[6].replace("\'", "\\'") + '\''

        # Wrap thumbnail link in quotations
        current_values[11] = "\'" + current_values[11] + "\'"

        # Join the comment(16 value) if divided with commas
        current_values[15] = ", ".join(current_values[15:])
        current_values = current_values[:16]

        # Close quotations on "description" column if new line inserted
        if "\"" not in current_values[15][-2:]:
            current_values[15] += "\""

        # Join columns and values as per sql syntax.
        columns = ",".join(columns)
        joined_values = ",".join(current_values)
        query = f"""
        INSERT INTO youtubestatistics.VideosStats({columns})
        VALUES({joined_values});
        """
        print(query)
        return query
