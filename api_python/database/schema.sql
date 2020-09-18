DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `public`;
DROP TABLE IF EXISTS `private`;

CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `email` TEXT UNIQUE NOT NULL,
  `password` TEXT NOT NULL,
  `type` TEXT  CHECK(`type` IN ('user', 'admin')) NOT NULL DEFAULT 'user',
  `iat` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00'
);

CREATE TABLE `public` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `field1` TEXT,
  `field2` TEXT
);

CREATE TABLE `private` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `field1` TEXT,
  `field2` TEXT
);
