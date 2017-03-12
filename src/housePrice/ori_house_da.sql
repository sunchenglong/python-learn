CREATE TABLE  IF NOT EXISTS house.ori_house_da (
id INT(20),
title VARCHAR(128),
alf VARCHAR(128),
href VARCHAR(64),
houseInfo VARCHAR(256),
dealDate VARCHAR(32),
totalPrice VARCHAR(32),
unit VARCHAR(8),
positionInfo  VARCHAR(128),
source  VARCHAR(32),
unitPrice  VARCHAR(32),
dealHouseTxt  VARCHAR(256),
PRIMARY KEY (`id`)
)  DEFAULT CHARSET=utf8;


CREATE TABLE  IF NOT EXISTS house.link_list (
link VARCHAR(128),
status INT not null default 0,
PRIMARY KEY (`link`)
)  DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS house.ods_house_da (
id INT(20),
region VARCHAR(16),
area VARCHAR(64),
struct VARCHAR(64),
room INT(10) not null default -1,
square double not null default -1,
dealDate VARCHAR(32),
dealHouseTxt VARCHAR(256),
five INT(10) not null default -1,
subway INT(10) not null default -1,
PRIMARY KEY (`id`, `region`, `area`))
DEFAULT CHARSET=utf8;


select area, year(timestamp(dealDate)) as y from ods_house_da where ;