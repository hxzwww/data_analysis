from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp


class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(
            path_to_df, parse_dates=['trending_date'],
            date_parser=(
                lambda x: pd.to_datetime(x, format='%y.%d.%m')
            )
        )

    def task1(self) -> pd.DataFrame:
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df = self.df[['trending_date', 'category_id', 'views', 'likes', 'dislikes', 'comment_count']]
        self.df.trending_date = self.df.trending_date.dt.day
        return self.df

    def task3(self) -> Figure:
        self.aboba34()
        return plt.gcf()

    def task4(self):  # -> Figure:
        self.aboba34()
        plt.ylim((0, 5e5))
        # return plt.gcf()

    def task5(self) -> Figure:
        sns.jointplot(data=self.df, x=self.df.views, y=self.df.likes, alpha=0.5)
        plt.title('useful jointplot')
        plt.xlabel('num of views')
        plt.ylabel('num of likes')
        return plt.gcf()

    def task6(self):  # -> Figure:
        with sns.plotting_context(font_scale=1.5), sns.axes_style("darkgrid"):
            self.df = self.df[(self.df.likes <= 1000) & (self.df.views <= 50000)]
            sns.jointplot(data=self.df, x=self.df.views, y=self.df.likes, alpha=0.5, joint_kws={'s': 70}, dropna=True,
                          space=.7)
            plt.title('Просмотры и лайки')
            plt.xlabel('Количество просмотров')
            plt.ylabel('Количество лайков')
        # return plt.gcf()

    def aboba34(self):
        plt.figure(figsize=(12, 4))
        sns.boxplot(x=self.df.trending_date, y=self.df.views)
        plt.title('Зависимость просмотров от даты')
        plt.xlabel('Дата')
        plt.ylabel('Количество просмотров')
