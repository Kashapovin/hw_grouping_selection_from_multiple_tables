import psycopg2
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://demo_netology:pass@localhost:5432/demo')
connection = engine.connect()

# print('название и год выхода альбомов, вышедших в 2018 году')
# pprint(connection.execute(
# """
# SELECT name, year_of_release FROM albums
# WHERE year_of_release = 2018;
#   """).fetchall())
#
# print('название и продолжительность самого длительного трека')
# pprint(connection.execute(
# """
# SELECT name, duration FROM tracks
# ORDER BY duration DESC;
#   """).fetchone())
#
# print('название треков, продолжительность которых не менее 3,5 минуты')
# pprint(connection.execute(
# """
# SELECT name FROM tracks
# WHERE duration > 3.5;
#   """).fetchall())
# #
# pprint(connection.execute(
# """
# SELECT name, duration FROM tracks;
#   """).fetchall())
#
# print('названия сборников, вышедших в период с 2018 по 2020 год включительно')
# pprint(connection.execute(
# """
# SELECT name FROM collections
# WHERE year_of_release BETWEEN 2018 AND 2020;
#   """).fetchall())
#
# print('исполнители, чье имя состоит из 1 слова')
# pprint(connection.execute(
# """
# SELECT name FROM artists
# WHERE name NOT LIKE '%% %%';
#   """).fetchall())
#
# print('название треков, которые содержат слово "мой"/"my"')
# pprint(connection.execute(
# """
# SELECT name FROM tracks
# WHERE name LIKE '%%my%%';
#   """).fetchall())