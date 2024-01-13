select concat("/home/grep/src/", f.board_id, "/", f.file_id, f.file_name, f.file_ext) as FILE_PATH
from used_goods_file f
join (select *
    from used_goods_board
    where views = (select max(views)
              from used_goods_board)) b
on f.board_id = b.board_id
order by f.file_id desc;