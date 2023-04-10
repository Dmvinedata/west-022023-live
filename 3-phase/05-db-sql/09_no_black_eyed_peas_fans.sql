-- Return all the Fans that are NOT fanas of BEPs (169)
-- Reutn needs to be the FANS 
-- Dealing TWO TABLES TOGETHER
--  ArtistId on the Fans table is the FORIEGN KEY of the artists table
SELECT fans.fanId, fans.name, artists.name
FROM fans
JOIN artists ON artists.artistid is fans.artistId
WHERE artists.name is not "Black Eyed Peas"
;