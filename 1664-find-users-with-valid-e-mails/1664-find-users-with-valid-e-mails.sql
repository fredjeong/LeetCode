select user_id, name, mail
from (select *, trim(trailing '@leetcode.com' from mail) as prefix
from users
where mail like '%@leetcode.com') temp
where substring(prefix, 1, 1) regexp '[A-Za-z]' and substring(prefix, 1, length(prefix)) regexp '^[0-9A-Za-z_.-]+$'