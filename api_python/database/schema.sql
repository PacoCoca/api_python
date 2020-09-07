DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `public`;
DROP TABLE IF EXISTS `private`;

CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `email` TEXT UNIQUE NOT NULL,
  `password` TEXT NOT NULL,
  `name` TEXT,
  `type` TEXT  CHECK(`type` IN ('user', 'admin')) NOT NULL DEFAULT 'user',
  `iat` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  `passwordToken` VARCHAR(16) DEFAULT ''
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

/* test user, the password is bar */
INSERT INTO `user`(`email`, `password`, `name`, `type`)
  VALUES(
    'foo@foo.foo',
    'pbkdf2:sha256:150000$pPvRhOB6$cf2ead387415b8d3484940a81d5819460bff0ca8506c4211bd0e1f2dc72003e1',
    'admin',
    'admin'
  );