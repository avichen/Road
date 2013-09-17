insert into user_info(user_code, password, gender, type, status) values("admin", "e10adc3949ba59abbe56e057f20f883e", "M", 1, 1);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(100, '系统管理', 'Management', '', 0, 1);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(101, '用户管理', 'User Management', '/user/list', 100, 2);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(102, '员工管理', 'Staff Management', '/staff/list', 100, 3);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(200, '假期管理', 'Vacation', '', 0, 4);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(201, '员工假期', 'Staff Vacation', '', 200, 5);

insert into menus(menu_code, memu_name_cn, menu_name_eng, menu_url, menu_parent, order_by)
values(202, '我的假期', 'My Vacation', '', 200, 6);

commit;

insert into group_menu(group_code, menu_code)
	values(1, 100);
insert into group_menu(group_code, menu_code)
	values(1, 101);
insert into group_menu(group_code, menu_code)
	values(1, 102);
insert into group_menu(group_code, menu_code)
	values(1, 200);
insert into group_menu(group_code, menu_code)
	values(1, 201);
insert into group_menu(group_code, menu_code)
	values(1, 202);

commit;