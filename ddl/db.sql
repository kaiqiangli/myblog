CREATE DATABASE `user` /*!40100 DEFAULT CHARACTER SET utf8 */;

use `user`;

/**
用户表
 */
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL COMMENT '用户名',
  `password` varchar(45) DEFAULT NULL COMMENT '用户密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户表';
SELECT * FROM user.users;

/**
文章表
 */
CREATE TABLE `Article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL COMMENT '标题',
  `summary` varchar(255) DEFAULT NULL COMMENT '简介',
  `content` varchar(45) DEFAULT NULL,
  `userId` varchar(45) DEFAULT NULL COMMENT '用户',
  `viewsCount` int(11) DEFAULT '0' COMMENT '阅读次数',
  `pointsCount` int(11) DEFAULT '0' COMMENT '点赞次数',
  `shareCount` int(11) DEFAULT '0' COMMENT '分享次数',
  `commendsCount` int(11) DEFAULT '0' COMMENT '评论次数',
  `crtTime` datetime DEFAULT NULL COMMENT '创建时间',
  `updateTime` datetime DEFAULT NULL COMMENT '更新时间',
  `submitTime` varchar(45) DEFAULT NULL COMMENT '提交时间',
  `deleted` tinyint(1) DEFAULT NULL COMMENT '是否删除(1 已删除, 0 未删除)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='发表文章';
