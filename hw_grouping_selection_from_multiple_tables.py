import psycopg2
import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://demo_netology:pass@localhost:5432/demo')
connection = engine.connect()

print("\nколичество исполнителей в каждом жанре")
pprint(connection.execute(
"""
SELECT j.id, COUNT(a.artist_id) FROM jenres j
LEFT JOIN artistjenre a
ON j.id = a.jenre_id
GROUP BY j.id
ORDER BY j.id;
""").fetchall())
#
print("\nколичество треков, вошедших в альбомы 2019-2020 годов")
pprint(connection.execute(
"""
SELECT COUNT(t.album_id) FROM tracks t
LEFT JOIN albums a
ON a.id = t.album_id
WHERE a.year_of_release = 2020
GROUP BY a.name;
""").fetchall())
#
pprint("\nсредняя продолжительность треков по каждому альбому")
pprint(connection.execute(
"""
SELECT a.name, ROUND(AVG(t.duration), 2) FROM albums a
LEFT JOIN tracks t
ON a.id = t.album_id
GROUP BY a.name;
  """).fetchall())
#

print("\nвсе исполнители, которые не выпустили альбомы в 2020 году")
pprint(connection.execute(
"""
SELECT artists.name FROM artists
WHERE artists.name !=
(SELECT artists.name FROM albumartist a
JOIN albums
ON a.album_id = albums.id
JOIN artists
ON a.artist_id = artists.id
WHERE year_of_release = 2020);
  """).fetchall())

print("\nназвания сборников, в которых присутствует конкретный исполнитель")
pprint(connection.execute(
"""
SELECT c.name FROM artists a
CROSS JOIN collections c
WHERE a.name = 'name_7';
  """).fetchall())

print("\nназвание альбомов, в которых присутствуют исполнители более 1 жанра")
pprint(connection.execute(
"""
SELECT name FROM
(SELECT a.name, COUNT(artistjenre.jenre_id) c FROM albums a
INNER JOIN albumartist aa
ON a.id = aa.album_id
INNER JOIN artistjenre
ON aa.artist_id = artistjenre.artist_id
GROUP BY artistjenre.artist_id, a.name) al
WHERE c > 1;
  """).fetchall())

# print("\nназвание альбомов, в которых присутствуют исполнители более 1 жанра")
# pprint(connection.execute(
# """
# SELECT a.name FROM albums a
# JOIN albumartist aa
# ON a.id = aa.album_id
# JOIN artistjenre
# ON aa.artist_id = artistjenre.artist_id
# GROUP BY artistjenre.artist_id, a.name
# HAVING COUNT(*) > 1
#   """).fetchall())

print("\nнаименование треков, которые не входят в сборники")
pprint(connection.execute(
"""
SELECT tracks.name FROM tracks
FULL OUTER JOIN trackcollection
ON trackcollection.track_id = tracks.id
WHERE trackcollection.track_id IS NULL
OR tracks.id IS NULL
ORDER BY tracks.id;
""").fetchall())

print("\nисполнителя(-ей), написавшего самый короткий по продолжительности трек")
pprint(connection.execute(
"""
SELECT name FROM
(SELECT artists.name, MIN(tracks.duration) FROM artists
JOIN albumartist
ON artists.id = albumartist.artist_id
JOIN tracks
ON albumartist.album_id = tracks.album_id
GROUP BY artists.name) a;
""").fetchone())

print("\nназвание альбомов, содержащих наименьшее количество треков")
pprint(connection.execute(
"""
SELECT name FROM
(SELECT albums.name, COUNT(tracks.name) q FROM tracks
JOIN albums
ON tracks.album_id = albums.id
GROUP BY albums.name
ORDER BY q) s
WHERE q =
(SELECT MIN(q) m FROM
(SELECT albums.name, COUNT(tracks.name) q FROM tracks
JOIN albums
ON tracks.album_id = albums.id
GROUP BY albums.name
ORDER BY q) l)
ORDER BY name;
""").fetchall())