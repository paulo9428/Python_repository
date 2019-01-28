import melondb_func as mf
import melondb_rank as mr
import melondb_album as ma
import melondb_singer as ms
import melondb_song as mso
import melondb_songsing as mss

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }


SongRank_insert_list = mr.get_rank_data()
album_insert_lst = ma.get_album_data()
singer_insert_lst = ms.get_singer_data()
sss = ms.get_song_data()
songsing_insert_lst = mss.get_songsing_data()


sql_rank_insert = "insert into SongRank(song_no, rank, rank_dt, like_cnt) values(%s,%s,%s,%s)"
sql_album_insert= "insert ignore into Album(album_no, album_name, publisher, likecnt, rating) values(%s,%s,%s,%s,%s)"
sql_singer_insert = "insert ignore into Singer(singer_no, singer_name, label) values(%s,%s,%s)"
sql_song_insert = "insert ignore into Song(song_no, song_name, genre) values(%s,%s,%s)"
sql_songsing_insert = "insert into SongSingMap(song, sing) values(%s,%s)"


mf.save_data(sql_rank_insert, SongRank_insert_list)
mf.save_data(sql_album_insert, album_insert_lst)
mf.save_data(sql_singer_insert, singer_insert_lst)
mf.save_data(sql_song_insert, sss)
mf.save_data(sql_songsing_insert, songsing_insert_lst)




