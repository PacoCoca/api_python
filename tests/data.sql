/* test users, the password is bar */
INSERT INTO `user`(`email`, `password`, `type`)
  VALUES
  (
    'foo@foo.foo',
    'pbkdf2:sha256:150000$pPvRhOB6$cf2ead387415b8d3484940a81d5819460bff0ca8506c4211bd0e1f2dc72003e1',
    'admin'
  ),
  (
    'foo2@foo.foo',
    'pbkdf2:sha256:150000$pPvRhOB6$cf2ead387415b8d3484940a81d5819460bff0ca8506c4211bd0e1f2dc72003e1',
    'user'
  );

INSERT INTO `public` (`field1`,`field2`)
  VALUES
    ('test 1 field 1', 'test 1 field 2'),
    ('test 2 field 1', 'test 2 field 2');

INSERT INTO `private` (`field1`,`field2`)
  VALUES
    ('test 1 field 1', 'test 1 field 2'),
    ('test 2 field 1', 'test 2 field 2');