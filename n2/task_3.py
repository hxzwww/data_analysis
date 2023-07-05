import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure

import os
import sys

f = open(os.devnull, 'w')
sys.stderr = f


class YouTube2:
    df: pd.DataFrame
    p_table: pd.DataFrame.pivot_table
    p_table_pro: pd.DataFrame.pivot_table

    def __init__(  # task0
            self,
            trends_df_path: str = 'RUvideos_short.csv',
            categories_df_path: str = 'RU_category_id.json'
    ):
        self.trends_df = pd.read_csv(
            trends_df_path, parse_dates=['trending_date'],
            date_parser=(
                lambda x: pd.to_datetime(x, format='%y.%d.%m')
            )
        )

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        self.df = self.trends_df.merge(self.categories_df, left_on='category_id', right_on='id')
        return self.df

    def task2(self) -> pd.DataFrame:
        self.p_table = pd.pivot_table(self.df, index='name', columns='trending_date', values='views', aggfunc=np.sum)
        return self.p_table

    def task3(self) -> Figure:
        sns.heatmap(self.p_table.apply(lambda x: x / 1e6), annot=True)
        plt.title('heatmap')
        return plt.gcf()

    def task4(self) -> pd.DataFrame:
        self.df.trending_date = self.df.trending_date.dt.day
        self.p_table_pro = pd.pivot_table(self.df, index='name', columns='trending_date', values='views',
                                          margins=True, margins_name='Всего', aggfunc=np.sum)
        return self.p_table_pro

    def task5(self):  # -> Figure:
        mask = np.zeros((16, 9))
        mask[:, 8] = True
        mask[15, :] = True
        mask2 = np.zeros((16, 9))
        mask2[15, 8] = True
        self.p_table_pro = self.p_table_pro.apply(lambda x: x / 1e6)
        sns.heatmap(self.p_table_pro, alpha=0, cbar=False, annot=True, annot_kws={'color': 'black'},
                    mask=mask2, fmt='.1f')
        sns.heatmap(self.p_table_pro, vmax=5, mask=mask, annot=True, fmt='.1f',
                    cbar_kws={'label': 'Количество просмотров (млн)'})

        plt.title('Тепловая карта просмотров')
        plt.ylabel('Категория видео')
        plt.xlabel('Число (ноябрь 2017)')
        # return plt.gcf()
