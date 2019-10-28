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
    result, need_manual = comment_analyser.find_out_most_valuable_entity()
    result = sorted(result.items(), key= lambda item : item[1], reverse=True)
    return result, need_manual


if __name__ == '__main__':
    res_list, need_manual = parse_comments()
    print('the most valuable entities are as follow: \n')
    for res in res_list:
        print('Entity: '+res[0]+' ,Mentions: '+str(res[1])+'\n')
    print('For a better performance please set the weight for these entities manually: \n')
    for entity in need_manual:
        print('Entity: ' + entity.entity + ' | Entity ID: ' + str(entity.id))
