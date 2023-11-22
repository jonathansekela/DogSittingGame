create table ethnicities (
	eth_id int not null auto_increment,
    eth_description varchar(255),
    primary key (eth_id)
);

insert into ethnicities (eth_description)
values ("American Indian or Alaskan Native");

insert into ethnicities (eth_description)
values ("Asian / Pacific Islander");

insert into ethnicities (eth_description)
values ("Black or African American");

insert into ethnicities (eth_description)
values ("Hispanic");

insert into ethnicities (eth_description)
values ("White / Caucasian");

insert into ethnicities (eth_description)
values ("Multiple ethnicity/ Other (please specify)");

create table player_address (
	address_id int,
    street1 varchar(1000),
    street2 varchar(1000),
    city varchar(255),
    state varchar(255),
    zip varchar(5),
    country varchar(255),
    primary key (address_id)
);

create table player_demographics (
	user_id int,
    last_name varchar(255),
    first_name varchar(255),
    middle_name varchar(255),
    address_id int,
    age int,
    eth_id int,
    gender varchar(255),
    primary key (user_id),
    foreign key (user_id) references player_access(user_id),
    foreign key (eth_id) references ethnicities(eth_id),
    foreign key (address_id) references player_address(address_id)
);