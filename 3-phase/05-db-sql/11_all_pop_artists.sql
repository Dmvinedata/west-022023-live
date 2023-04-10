SELECT artists.name
FROM artists
JOIN albums
  ON albums.artistId = artists.artistId
JOIN tracks
  on albums.albumId = tracks.albumId
JOIN genres
  ON tracks.genreId = genres.genreId
WHERE genres.name = "Pop";