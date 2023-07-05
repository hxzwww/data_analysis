import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        return self.df.head()

    def task2(self) -> tp.List[str]:
        return list(self.df.loc[:, self.df.isna().any()].keys())

    def task3(self) -> pd.DataFrame:
        self.df = self.df.dropna()
        return self.df

    def task4(self) -> pd.DataFrame:
        return self.df.describe()

    def task5(self) -> int:
        return len(self.df[self.df['test_score'] == 100])

    def task6(self) -> pd.DataFrame:
        df_copy = self.df.copy()
        df_copy['cnt_100'] = df_copy.groupby('school')['test_score'].transform(lambda x: x == 100)
        df_copy = df_copy.groupby('school').agg({'cnt_100': 'sum', 'number_of_students': 'max'})
        df_copy = df_copy.sort_values(by=['cnt_100', 'school'], ascending=False).loc[df_copy.cnt_100 != 0].reset_index()
        return df_copy

    def task7(self) -> pd.DataFrame:
        return self.average_score_df().head(10)

    def task8(self) -> pd.DataFrame:
        return self.average_score_df().tail(10)

    def task9(self):  # -> Axes:
        plt.figure(figsize=(12, 4))
        df_le = self.df.copy()[self.df['number_of_students'] <= 1000]
        df_g = self.df.copy()[self.df['number_of_students'] > 1000]
        plt.hist(df_g.test_score, bins=30, alpha=0.5)
        plt.hist(df_le.test_score, bins=30, alpha=0.5)
        plt.xlabel('Балл ЕКЭ')
        plt.ylabel('Число котиков')
        plt.legend(['Большая школа', 'Маленькая школа'])
        plt.title('Школо-кото-балло-график')
        # return plt.gca()

    def average_score_df(self) -> pd.DataFrame:
        df_copy = self.df.copy()
        df_copy = df_copy.groupby('school').agg({'test_score': 'mean', 'number_of_students': 'max'})
        df_copy = df_copy.sort_values(by='test_score', ascending=False).reset_index()
        return df_copy
