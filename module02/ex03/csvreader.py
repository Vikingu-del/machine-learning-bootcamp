class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        self.file_object = None
        self.header_data = None
        self.data = None


    def __enter__(self):
        try:
            self.file_object = open(self.filename, "r")
            lines = self.file_object.readlines()
        except Exception:
            return None
        

        all_rows = []
        for line in lines:
            clean_line = line.replace('\r', '').replace('\n', '')
            if not clean_line:
                continue
            fields = [field.strip() for field in clean_line.split(self.sep)]
            all_rows.append(fields)

        if not all_rows:
            return None
        
        excepted_length = len(all_rows[0])
        if not all(len(row) == excepted_length for row in all_rows):
            return None
        
        if self.header:
            self.header_data = all_rows[0]
            data_pool = all_rows[1:]
        else:
            self.header_data = None
            data_pool = all_rows
        start = self.skip_top
        end = len(data_pool) - self.skip_bottom

        if start < 0 or self.skip_bottom < 0 or start > len(data_pool) or end < start:
            return None
        
        self.data = data_pool[start:end]

        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file_object:
            self.file_object.close()
        return False


    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data


    def getheader(self):
        """ Retrieves the header from the csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header_data
    

if __name__ == "__main__":
    try:
        with CsvReader('player.csv', ',', True) as file:
            data = file.getdata()
            header = file.getheader()
            print(header)
            for d in data:
                print(d)
            print("Inside the with block, is file closed?", file.file_object.closed)
    except Exception as e:
        print(e)
    print("Outside the with block, is file closed?", file.file_object.closed)
