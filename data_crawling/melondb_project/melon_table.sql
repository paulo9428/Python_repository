CREATE TABLE `Album` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `album_no` int(11) NOT NULL,
  `album_name` varchar(45) NOT NULL,
  `publisher` varchar(45) NOT NULL,
  `likecnt` int(11) NOT NULL,
  `rating` float NOT NULL,
  PRIMARY KEY (`id`,`album_no`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;

CREATE TABLE `Singer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `singer_no` int(11) NOT NULL,
  `singer_name` varchar(45) NOT NULL,
  `label` varchar(1024) DEFAULT 'no',
  PRIMARY KEY (`id`,`singer_no`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8;

CREATE TABLE `Song` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `song_no` int(11) NOT NULL,
  `song_name` varchar(1024) NOT NULL,
  `genre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`song_no`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

CREATE TABLE `SongRank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `song_no` varchar(100) NOT NULL,
  `rank` int(11) DEFAULT NULL,
  `rank_dt` varchar(100) NOT NULL,
  `like_cnt` int(11) NOT NULL,
  PRIMARY KEY (`id`,`song_no`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

CREATE TABLE `SongSingMap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `song` int(11) NOT NULL,
  `sing` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

