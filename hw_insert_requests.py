import psycopg2
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://demo_netology:pass@localhost:5432/demo')
connection = engine.connect()

# connection.execute(
# """
# INSERT INTO tracks(name, duration, album_id)
# VALUES
# ('track_1 my', 3, 291),
# ('track_2', 2, 291),
# ('track_3', 1, 291),
# ('track_4', 5, 292),
# ('track_5', 3, 292),
# ('track_6', 3, 293),
# ('track_7', 5, 294),
# ('track_8', 4,295),
# ('track_9', 5, 296),
# ('track_10', 3, 297),
# ('track_11', 2, 298),
# ('track_12', 3, 298),
# ('track_13', 6, 298),
# ('track_14', 5, 298),
# ('track_15', 2, 298);
# """)

# connection.execute(
# """
# INSERT INTO collections(name, year_of_release)
# VALUES
# ('collection_1', 2020),
# ('collection_2', 2022),
# ('collection_3', 2011),
# ('collection_4', 2019),
# ('collection_5', 2008),
# ('collection_6', 2015),
# ('collection_7', 2018),
# ('collection_8', 2013);
# """)

# connection.execute(
# """
# INSERT INTO trackcollection(track_id, collection_id)
# VALUES
# (660, 283),
# (662, 284),
# (663, 285)
# (665, 286);
# """)

# connection.execute(
# """
# INSERT INTO artistjenre(jenre_id, artist_id)
# VALUES
# (191, 299);
# """)

# connection.execute(
# """
# INSERT INTO albumartist(album_id, artist_id)
# VALUES
# (291, 299),
# (292, 300),
# (293, 301);
# """)














# connection.execute(
# """
# INSERT INTO tracks(name, duration, album_id)
# VALUES
# ('track_1 my', 3, 291),
# ('track_2', 2, 291),
# ('track_3', 1, 291),
# ('track_4', 5, 292),
# ('track_5', 3, 292),
# ('track_6', 3, 293),
# ('track_7', 5, 294),
# ('track_8', 4,295),
# ('track_9', 5, 296),
# ('track_10', 3, 297),
# ('track_11', 2, 298),
# ('track_12', 3, 298),
# ('track_13', 6, 298),
# ('track_14', 5, 298),
# ('track_15', 2, 298);
# """)

# pprint(connection.execute(
# """
# SELECT * FROM tracks;
# """).fetchall())

# connection.execute(
# """
# INSERT INTO collections(name, year_of_release)
# VALUES
# ('collection_1', 2020),
# ('collection_2', 2022),
# ('collection_3', 2011),
# ('collection_4', 2019),
# ('collection_5', 2008),
# ('collection_6', 2015),
# ('collection_7', 2018),
# ('collection_8', 2013);
# """)

# pprint(connection.execute(
# """
# SELECT * FROM collections;
# """).fetchall())
#
# connection.execute(
# """
# INSERT INTO albums(name, year_of_release)
# VALUES
# ('album_1', 2020),
# ('album_2', 2022),
# ('album_3', 2002),
# ('album_4', 2005),
# ('album_5', 2009),
# ('album_6', 2018),
# ('album_7', 2011),
# ('album_8', 2018);
# """)
#
pprint(connection.execute(
"""
SELECT * FROM albums;
""").fetchall())

# connection.execute(
# """
# INSERT INTO artists(name)
# VALUES
# ('name_1'),
# ('name_2'),
# ('name_3'),
# ('name_4'),
# ('name_5'),
# ('name_6'),
# ('name_7'),
# ('name_8');
# """)
#
#
pprint(connection.execute(
"""
SELECT * FROM artists;
""").fetchall())
#
# connection.execute(
# """
# INSERT INTO jenres(name)
# VALUES
# ('jenre_1'),
# ('jenre_2'),
# ('jenre_3'),
# ('jenre_4'),
# ('jenre_5');
# """)
#
pprint(connection.execute(
"""
SELECT * FROM jenres;
""").fetchall())

# connection.execute(
# """
# INSERT INTO trackcollection(track_id, collection_id)
# VALUES
# (585, 283),
# (586, 284),
# (587, 285);
# """)

# #
# pprint(connection.execute(
# """
# SELECT * FROM trackcollection;
# """).fetchall())
#
# connection.execute(
# """
# INSERT INTO albumartist(album_id, artist_id)
# VALUES
# (291, 299),
# (292, 300),
# (293, 301);
# """)
#
# pprint(connection.execute(
# """
# SELECT * FROM albumartist;
# """).fetchall())

# connection.execute(
# """
# INSERT INTO artistjenre(jenre_id, artist_id)
# VALUES
# (187, 299),
# (188, 300),
# (188, 301);
# """)
#
# pprint(connection.execute(
# """
# SELECT * FROM albumartist;
# """).fetchall())