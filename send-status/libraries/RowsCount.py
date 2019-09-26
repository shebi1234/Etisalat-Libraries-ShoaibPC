import pandas as pd


class RowsCount(object):

    # def agentname(self):
    #     df = pd.read_excel('E:/BIMA-Parallel/agents.xlsx')
    #     return df['Name'].to_string()
    def rowscount(self, filepath):
        df = pd.read_excel(filepath, error_bad_lines=False)
        try:
            return int(df.shape[0])
        except Exception as e:
            raise e


