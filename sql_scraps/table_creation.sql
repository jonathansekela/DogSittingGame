/*create table player_access (
	access_key int not null auto_increment,
	user_id int,
    access datetime,
    primary key (access_key)
);*/
create table game_data (
	data_key int not null auto_increment,
    user_id int,
    time_to_complete int,
    primary key (data_key),
    foreign key (user_id) references player_access(user_id)
);