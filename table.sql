CREATE DATABASE data_analysis;

# Tips: 在生成这些表之前, 可以先更新

# ######################################################################
# 用户列表
CREATE TABLE `user_profile` (
  `id`        INT(11)     NOT NULL AUTO_INCREMENT,
  `logic_id`  VARCHAR(32) NOT NULL,
  `gender`    TINYINT(1)           DEFAULT NULL,
  `city`      VARCHAR(32)          DEFAULT NULL,
  `join_time` DATETIME    NOT NULL,
  `user_id`   INT(11)     NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `logic_id` (`logic_id`),
  KEY `join_time` (`join_time`),
  CONSTRAINT `user_profile_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 2
  DEFAULT CHARSET = utf8;
# ######################################################################