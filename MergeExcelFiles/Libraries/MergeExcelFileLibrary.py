import glob

import pandas as pd


class MergeExcelFileLibrary:

    def excel_file_merge(self, target_dir, file_path):
        try:
            path = target_dir
            excel_names = glob.glob(path + "/*.xlsx")

            excels = [pd.ExcelFile(name) for name in excel_names]

            frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]

            frames[1:] = [df[1:] for df in frames[1:]]

            combined = pd.concat(frames)

            combined.to_excel(file_path, header=False, index=False)
            # print("Combined", combined.to_excel(file_path, header=False, index=False))

        except Exception as e:
            raise e

# data = MergeExcelFileLibrary()
# data.excel_file_merge(r'E:/Forex', 'E:/2222.xlsx')
