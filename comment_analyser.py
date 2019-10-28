import google_services as gs
import datamodel as dm
import DB_helper as dbm
from json_paser import get_properties as properties

# Parse comments with google api
def entity_maker(comment):
    entities = gs.get_nlp_entities(comment.comment)
    for entity in entities:
        entity_obj = dm.Entity(entity=entity.name,
                               magnitude=entity.sentiment.magnitude,
                               score=entity.sentiment.score,
                               comment=comment,
                               salience = entity.salience,
                               type=entity.type
                               )
        entity_obj.weight = entity_analyser(entity_obj)
        dbm.create_entity(entity_obj)
    print(entities)


# Give every entity a score of weight to find out the most valuable ones
def entity_analyser(entity):
    note = entity.comment.note
    score = entity.score
    # To find out what makes customers happy
    if note >= 8:
        note = 10 - note
    # If the magnitude is too big while the score is too small, it requires a manual operation
    if entity.magnitude > 0.3 and abs(entity.score) < 0.3:
        return -1
    # If can not get values from google api, it requires a manual operation, or it is not valuable at all
    if entity.magnitude < 0.1 and abs(entity.score) < 0.1:
        return -1
    # It's better to concentrate more on what makes customer disappoint
    if entity.score< 0:
        score = abs(score)*properties('param_negative')
    weight = (10 - note) * entity.salience*properties('param_salience')\
             * ((score*properties('param_score')
                + entity.magnitude*properties('param_magnitude')))
    return weight

