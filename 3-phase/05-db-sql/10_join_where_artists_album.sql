-- Show the artist name, album name, num of tracks
SELECT artists.name, albums.title
FROM artists
JOIN albums
ON artists.artistId = albums.artistId
-- JOIN tracks
-- ON albums.albumId = tracks.albumId
WHERE artists.artistId =1
;

-- SELECT *
-- FROM artists
-- JOIN albums
-- ON artists.artistId = albums.artistId;