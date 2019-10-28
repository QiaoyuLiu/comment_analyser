import DB_helper as dbh
import comment_analyser
import json_paser


def parse_comments():

    current_id = json_paser.get_properties('current_id')
    comment_list = dbh.get_all_comments(current_id)
    for comment in comment_list:
        comment_analyser.entity_maker(comment)
        if current_id < comment.id:
            current_id = comment.id
    json_paser.update_current(current_id)


if __name__ == '__main__':
    parse_comments()
