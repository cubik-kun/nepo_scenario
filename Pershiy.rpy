init:

    $ mods["sam_start"]=u"Не по сценарию..."
    $ renpy.config.developer = True

    image bg int_house_of_sl_night = "mods/something_new/image/bg/doma/int_house_of_sl_night.jpg"
    image bg int_house_of_sl_light_night = "mods/something_new/image/bg/doma/int_house_of_sl_light_night.jpg"
    image bg ext_house_of_sl_night = "mods/something_new/image/bg/doma/ext_house_of_sl_night.jpg"
    image bg int_house_of_dv_night_light = "mods/something_new/image/bg/doma/int_house_of_dv_night_light.jpg"
    image bg int_house_of_dv_night_black = "mods/something_new/image/bg/doma/int_house_of_dv_night2.jpg"
    image bg ext_house_of_un_night = "mods/something_new/image/bg/doma/ext_house_of_un_night_7dl.jpg"
    image bg ext_house_of_un_sunset = "mods/something_new/image/bg/doma/ext_house_of_un_sunset1.jpg"
    image bg centr_stolovoy_day = "mods/something_new/image/bg/stolovaya/dva_dish2.jpg"
    image bg ugol_stolovoy_day = "mods/something_new/image/bg/stolovaya/ugol_stolovoy_day.jpg"
    image bg int_dining_hall_table_day_back = "mods/something_new/image/bg/stolovaya/int_dining_hall_table_day_back.jpg"
    image bg ext_musclub_near_sunset = "mods/something_new/image/bg/musclub/ext_musclub_near_sunset.jpg"
    image bg ext_musclub_near_day = "mods/something_new/image/bg/musclub/veranda_muz.jpg"
    image bg int_musclub_night_with_matras = "mods/something_new/image/bg/musclub/int_music_club_mattresses_night.jpg"
    image bg int_musclub_night = "mods/something_new/image/bg/musclub/int_musclub_night.jpg"
    image bg ext_near_musclub_night = "mods/something_new/image/bg/musclub/ext_music_club_verandah_night.jpg"
    image bg ext_dining_door_day = "mods/something_new/image/bg/stolovaya/dct_ext_dining_door_day.jpg"
    image bg int_old_building_day = "mods/something_new/image/bg/old_corpus/int_old_building_day.jpg"
    image bg ext_beach_water_night = "mods/something_new/image/bg/bereg/ext_beach_water_night.jpg"
    image bg zvezdy = "mods/something_new/image/bg/ulica/zvezdy.jpg"
    image bg ext_houses_night = "mods/something_new/image/bg/doma/alley_night.jpg"
    image bg ext_musclub_night = "mods/something_new/image/bg/musclub/ext_musclub_night.jpg"
    image bg int_domik_dv_vecher = "mods/something_new/image/bg/doma/int_house_of_dv_sunset.jpg"
    image bg ext_domik_dv_vecher = "mods/something_new/image/bg/doma/ext_house_of_dv_sunset.jpg"
    image bg ext_house_sem_night = "mods/something_new/image/bg/doma/ext_house_of_lseya_night.png"
    image bg ext_house_of_kostya_day = "mods/something_new/image/bg/doma/ext_house_of_kostya.png"
    image bg int_sklad2_night ="mods/something_new/image/bg/sklad/int_warehouse_night_7dl.jpg"
    image bg ext_sklad_night = "mods/something_new/image/bg/sklad/ext_warehouse_night_7dl.jpg"
    image bg int_sklad2_day = "mods/something_new/image/bg/sklad/int_warehouse_day2_7dl.jpg"
    image bg ext_admin_day = "mods/something_new/image/bg/admin/ext_admins_day_7dl.jpg"
    image bg int_admin_cabinet = "mods/something_new/image/bg/admin/int_admin_boxes_day.png"
    image bg int_admin_hall = "mods/something_new/image/bg/admin/int_admins_7dl.jpg"
    image bg int_director_office_day = "mods/something_new/image/bg/admin/int_chief_office_day_7dl.jpg"
    image bg int_office_day = "mods/something_new/image/bg/admin/int_office_day_nolight.png"
    image bg int_admin_hall2 = "mods/something_new/image/bg/admin/int_admin_corridor.png"
    image bg int_clubs_male_night_light = "mods/something_new/image/bg/clubs/int_clubs_on.jpg"


    
    image dv dontlike pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_dontlike.png'))
    image dv shy2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_shy2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_shy2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_shy2.png'))
    image dv sad_smile pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_3_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_3_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sad_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_3_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_3_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sad_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_3_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_3_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sad_smile.png'))
    image dv sadness pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sadness.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sadness.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_sadness.png'))
    image dv laugh lif = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_laugh.png'))
    image dv smile lif = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_smile.png'))
    image dv normal lif = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_4_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_normal.png'))
    image dv surprise lif = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_1_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_1_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_1_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_1_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/body/dv_1_body.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/odyag/dv_1_underwear_ll.png', (0, 0), 'mods/something_new/image/sprites/normal/dv/emocii/dv_surprise.png')) 
    image dv cry2 pioneer far = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/dv/cili/dv_cry2_pioneer_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/dv/cili/dv_cry2_pioneer_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/dv/cili/dv_cry2_pioneer_far.png'))
    image dv cry2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/cili/dv_cry2_pioneer.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/cili/dv_cry2_pioneer.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/dv/cili/dv_cry2_pioneer.png'))
    
    image sl tender2 naked close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_tender2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_tender2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_tender2.png'))
    image sl cry pioneer far = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/far/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/far/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/far/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/far/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/far/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/far/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/far/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/far/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/far/sl/emocii/sl_4_cry.png'))
    image sl cry pioneer close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'))
    image sl cry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_pioneer.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'))
    image sl cry naked close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'))
    image sl cry swim = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/normal/sl/emocii/sl_4_cry.png'))
    image sl cry swim close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sl/body/sl_4_body.png', (0, 0), 'mods/something_new/image/sprites/close/sl/odyag/sl_4_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sl/emocii/sl_4_cry.png'))
    image un evilsmile2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right_2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right_2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right_2.png'))
    image un evilsmile3 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_right.png'))
    image un evilsmile2 shadow = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_2.png'))
    image un evilsmile3 shadow = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_3.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_3.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_3.png'))
    image un shadow knife = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_silhouette.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_silhouette.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_silhouette.png'))
    image un evilsmile shadow = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_1.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_1.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_shadow_1.png'))
    image un evilsmile2 knife = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_knife.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_knife.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_scary_knife.png'))
    image un anticipation pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_pioneer.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_pioneer.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_pioneer.png'))
    image un anticipation knife = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_knife.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_knife.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/normal/elena/cili/ed_un_d2_smile_knife.png'))
    image un smile naked close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile.png'))
    image un grin naked close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_3_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_3_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_3_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_3_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_3_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_3_laugh.png'))
    image un smile2 naked close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/un/body/un_1_body.png', (0, 0), 'mods/something_new/image/sprites/close/un/emocii/un_1_smile2.png'))
    image un ubv_surprise pioneer close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/close/elena/cili/ed_un_d2_surprise_close.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/close/elena/cili/ed_un_d2_surprise_close.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/close/elena/cili/ed_un_d2_surprise_close.png'))
    image un evilsmile2 pioneer far = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/elena/cili/ed_un_d2_scary_right_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/elena/cili/ed_un_d2_scary_right_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/something_new/image/sprites/far/elena/cili/ed_un_d2_scary_right_far.png'))

    image sh smile swim close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_1_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_1_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_1_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_1_smile.png'))
    image sh serious pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_serious.png'))
    image sh normal pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_normal.png'))
    image sh laugh pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_laugh.png'))
    image sh upset pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_upset.png'))
    image sh smile pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_1_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_1_smile.png'))
    image sh surprise pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/normal/sh/body/sh_3_uniform.png', (0, 0), 'mods/something_new/image/sprites/normal/sh/emocii/sh_3_surprise.png'))
    image sh normal_smile swim close = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_2_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_2_normal_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_2_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_2_normal_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1125, 1080), (0, 0), 'mods/something_new/image/sprites/close/sh/body/sh_2_swim.png', (0, 0), 'mods/something_new/image/sprites/close/sh/emocii/sh_2_normal_smile.png'))
    
    
    
    image cg sl_hentai_1 = "mods/something_new/image/cg/Slavya/d6_sl_hentai_1.jpg"
    image cg d1_dv_hentai_2 = "mods/something_new/image/cg/Alisa/d6_dv_hentai_2.jpg"
    image cg sl_swimming_dal = "mods/something_new/image/cg/Slavya/sl_swimming_dal.jpg"
    image cg sl_swimming_bliz = "mods/something_new/image/cg/Slavya/sl_swimming_bliz.jpg"
    image cg d2_un_hentai_3 = "mods/something_new/image/cg/Lena/d2_un_hentai_3.jpg"
    image cg volelbol_us_sh = "mods/something_new/image/cg/Ulya/volelbol_us_sh.png"
    image cg senya_na_gitare = "mods/something_new/image/cg/Senya/Senya_na_gitare.png"
    image cg d2_un_hentai = "mods/something_new/image/cg/Lena/d2_un_hentai.jpg"
    image cg ubivayut_slavyu = "mods/something_new/image/cg/Lena/ubivayut_slavyu.png"
    image cg poceluy_slavya = "mods/something_new/image/cg/Slavya/poceluy_slavya.png"
    image cg gitara_miku_bereg_sunset = "mods/something_new/image/cg/Miku/Miku_guitar_Coy.png"
    image cg d1_dv_hentai_1 = "mods/something_new/image/cg/Alisa/d6_dv_hentai.jpg"
    image cg alisa_pod_ruku = "mods/something_new/image/cg/Alisa/old_d5_dv_island.jpg"
    image cg reflection_el_un = "mods/something_new/image/cg/El/reflection_el_un.png"
    image cg alisa_day_igraet = "mods/something_new/image/cg/Alisa/alisa_day_igraet.png"
    image cg Semon_electrogitara = "mods/something_new/image/cg/Alisa/Semon_electrogitara.jpeg"
    image cg Ubivasha_noch_alisa_kill = "mods/something_new/image/cg/Lena/Ubivasha_noch_alisa_kill.png"
    image cg ulz_1 = "mods/something_new/image/cg/Ulya/ulz_1.jpg"
    image cg ulz_2 = "mods/something_new/image/cg/Ulya/ulz_2.jpg"
    
    
    
    $ water_ambience = "mods/something_new/listen/ambiance/water_ambiance.mp3"
    
    

    $ vkl = "mods/something_new/listen/sounds/vkl.mp3"
    $ smeh_wom = "mods/something_new/listen/voises/Alisa_hohot.mp3"
    $ nozhom_palcy = "mods/something_new/listen/sounds/nozhom_palcy.mp3"
    $ kill_momento = "mods/something_new/listen/sounds/kill_momento.mp3"
    $ krik_wom = "mods/something_new/listen/voises/krik.mp3"
    $ ston1 = "mods/something_new/listen/sounds/ston_1.mp3"
    $ ston2 = "mods/something_new/listen/sounds/ston_2.mp3"
    $ laugh_male = "mods/something_new/listen/voises/laugh_male.mp3"
    $ zazheg_sigaru = "mods/something_new/listen/voises/zajugoy_i_zatyanulsia.mp3"
    $ clap_1 = "mods/something_new/listen/sounds/aplod_1_wom.mp3"
    $ kurit = "mods/something_new/listen/voises/kurit.mp3"
    $ hihikane = "mods/something_new/listen/voises/igrivyy_laught_woman.mp3"
    $ soul_cry = "mods/something_new/listen/voises/soul_cry.mp3"
    $ sfx_ed_laugh_1 = "mods/something_new/listen/voises/sfx_ed_laugh_1.mp3"
    $ sfx_ed_laugh_2 = "mods/something_new/listen/voises/sfx_ed_laugh_2.mp3"
    $ slomal_palcy = "mods/something_new/listen/sounds/slomal_palcy.mp3"
    $ stuk_v_dver = "mods/something_new/listen/sounds/stuk_v_dver.mp3"
    $ smah_nad_shutkoy_woman = "mods/something_new/listen/voises/smah_nad_shutkoy_woman.mp3"
    $ krik_boli_wom = "mods/something_new/listen/voises/kric_ot_boli.mp3"
    $ vizg_wom = "mods/something_new/listen/voises/vizg_wom.mp3"
    $ sfx_open_door_sklad = "mods/something_new/listen/sounds/sfx_open_door_sklad.mp3"
    $ sfx_skrip_door = "mods/something_new/listen/sounds/sfx_skrip_door.mp3"
    $ plach_14sek = "mods/something_new/listen/voises/plach_14sek.mp3"
    $ svyazka_kluchey = "mods/something_new/listen/sounds/svyazka_kluchey.mp3"
    $ man_otkashlyalsya = "mods/something_new/listen/voises/man_otkashlyalsya.mp3"
    $ el_cough = "mods/something_new/listen/voises/el_cough.mp3"
    $ zatyaga = "mods/something_new/listen/voises/zatyaga.mp3"
    $ krik_uzhasa = "mods/something_new/listen/voises/krik_uzhasa.mp3"
    $ udar_po_golove1 = "mods/something_new/listen/sounds/udar_po_golove1.mp3"
    $ stuk_metal = "mods/something_new/listen/sounds/ud_metal_knock.ogg"
     

    
    
    $ i_drive = "mods/something_new/listen/music/i_drive.mp3"
    $ piano_song_miku_1 = "mods/something_new/listen/music/piano_song_miku_1.mp3"
    $ melonholy = "mods/something_new/listen/music/melonholy.mp3"
    $ tel_aviv  ="mods/something_new/listen/music/tel_aviv.mp3"
    $ still_loving_you_alice = "mods/something_new/listen/music/still_loving_you_alice.mp3"
    $ wire = "mods/something_new/listen/music/wire.mp3"
    $ dlya_alco = "mods/something_new/listen/music/dlya_alco.mp3"
    $ never_gonna_give_you_up = "mods/something_new/listen/music/never_gonna_give_you_up.mp3"
    $ voleyball = "mods/something_new/listen/music/voleyball.mp3"
    $ lonely_man = "mods/something_new/listen/music/lonely_man.mp3"
    $ MeetMeThere = "mods/something_new/listen/music/MeetMeThere.ogg"
    $ sad_piano_miku = "mods/something_new/listen/music/sad_piano_miku2.mp3"
    $ privet = "mods/something_new/listen/music/privet__cover_by_inache.mp3"
    $ schitalochka = "mods/something_new/listen/music/svidetelstvo_o_smerti-schitalochka__cover_by_inache.mp3"
    $ gruppa_krovi_cover_by_Mare = "mods/something_new/listen/music/gruppa_krovi__cover_by_Mare.mp3"
    $ mama_my_soshli_suma = "mods/something_new/listen/music/mama_my_soshli_suma__cover_by_conograi.mp3"
    $ hell = "mods/something_new/listen/music/hell.mp3"
    $ Myuu_Fernweh = "mods/something_new/listen/music/Myuu_Fernweh.mp3"
    $ vintage_labeled_amys_dark_axe = "mods/something_new/listen/music/vintage_labeled_amys_dark_axe.mp3"
    $ tpinf_wn = "mods/something_new/listen/music/tpinf_wn.mp3"
    $ sdl_tpinf_whitecoma = "mods/something_new/listen/music/sdl_tpinf_whitecoma.ogg"
    $ remix = "mods/something_new/listen/music/remix.mp3"
    $ F21LFm = "mods/something_new/listen/music/SanTechnik_F21LFm.mp3"
    $ beat_of_nature = "mods/something_new/listen/music/beat_of_nature.mp3"
    $ just_relax = "mods/something_new/listen/music/just_relax.mp3"
    $ iron = "mods/something_new/listen/music/iron.mp3"
    $ so_cold = "mods/something_new/listen/music/so_cold.mp3"
    $ shape_of_my_heart = "mods/something_new/listen/music/shape_of_my_heart_7dl.ogg"
    $ are_you_there_7dl = "mods/something_new/listen/music/are_you_there_7dl.ogg"
    $ napryagis2 = "mods/something_new/listen/music/napryagis2.mp3"
    $ sdl_tpinf_cu = "mods/something_new/listen/music/sdl_tpinf_cu.ogg"
    $ My_Silent_Angel = "mods/something_new/listen/music/My_Silent_Angel.mp3"
    $ kukla_kolduna = "mods/something_new/listen/music/kukla_kolduna.mp3"
    $ ktoto_nablyadaet = "mods/something_new/listen/music/kto-to_nablyadaet.mp3"
    $ fearmusic_4 = "mods/something_new/listen/music/fearmusic_4.mp3"
    $ creepy = "mods/something_new/listen/music/creepy.ogg"
    $ run = "mods/something_new/listen/music/run.mp3"
    $ Hunx = "mods/something_new/listen/music/Hunx.mp3"
    $ belaya_noch_guitar ="mods/something_new/listen/music/belaya_noch_guitar.mp3"
    $ belaya_noch_cover = "mods/something_new/listen/music/belaya_noch__Koshkina_cover.mp3"
    $ Frightening_Unknown = "mods/something_new/listen/our_music/pmitriy_-_Frightening_Unknown.mp3"
    $ grind = "mods/something_new/listen/music/grind.mp3"
    $ staryy_dom = "mods/something_new/listen/music/staryy_dom.mp3"
    $ General_Release = "mods/something_new/listen/music/General_Release.mp3"
    $ bitva = "mods/something_new/listen/music/bitva.ogg"

    $ timeofday = persistent.timeofday ##НЕ ТРОГАТЬ
    
    
    $ sa_ochki = 0
    $ ma_ochki = 0
    $ dv_ochki = 0
    $ dv_2_ochki = 0  
    $ alisagood_ochki = 0
    $ alisabad_ochki = 0
    $ bd_ochki = 0
    $ ubiv_ochki = 0
    $ sl_ochki = 0
    $ dv3_ochki = 0  
    $ ubiv2_ochki = 0
    $ odin_ochki = 0  
    $ snim_ochki = 0
    $ sl_good_ochki = 0  
    $ sl_bad_ochki = 0
    $ od_ochki = 0 
    $ dv2_ochki = 0

    $ bbl_ochki = 0
    $ muz_ochki = 0
    
    #Функция, делающая сохранение оригинального интерфейса БЛ + включающая наш интерфейс. (её не трогать)
    python:   
        def sam_save_old_and_activate_screens():
            sam_screens_old()
            sam_screens_activ()

label somesing_new_new_cikl:
    $ save_name = ('День 1. Новый цикл.')
    play music lonely_man fadein 3
    play ambience ambience_ext_road_day fadein 2
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg int_bus with dissolve
    "Я неподвижно сижу в салоне Икаруса."
    "Пылинки взмывают вверх и падают вниз в луче света падающем из прикрытого окна автобуса."
    th "Интересно это те же пылинки, что были в прошлом цикле. Они из вчера или сегодня, или они вообще из...{w} Господи... что за бред опять?"
    th "Я схожу с ума?{w} Вроде уже сошёл."
    th "Да точно. В тот момент как устроил резню..."
    th "Интересно, а с кого я тогда начал?"
    th "Чёрт, не помню, старею похоже...{w} То ли рыжая взбесила меня своими приколами, то ли Лена своей скромностью, или обе сразу своей перепалкой?"
    th "Да и неважно."
    th "Зато чётко помню, как после этого весь лагерь перерезал."
    th "Да уж, пожалуй, я перегнул тогда."
    th "Вдруг они не возрождаются как я, а просто на их место ставит лагерь копии? Хотя в чем разница? Ведь это те же куклы, только другие."
    th "А если они действительно умерли, то считай, что я их освободил от бесконечного цикла. Правда, для них это всегда первый раз..."
    th "Мда уж..."
    th "Освободитель хренов..."
    th "Скоро уже у меня совсем остатков совести не останется, буду как тот мой знакомый."
    th "Хотя всё равно...{w} Раньше надо было волноваться, в последние цикла три я эту блондинку сразу же убиваю,{w} и тело в автобус."
    th "Все улики заметает...{w} красавчик в общем."
    th "Так что я уже {i}становлюсь{/i} как {i}тот знакомый{/i}."
    th "А вот, если они умирают, именно от моей руки, то я тоже умру от чужой руки?"
    th "Интересно.{w} Надо будет попробовать, чтобы меня кто-то убил."
    th "А если не сработает?{w} Я буду тут вечность?{w} Хотя с чего я взял, что они умирают безвозвратно?{w} Может это те же люди,{w} а если точнее, куклы."
    th "А может меня на какой-нибудь 410 цикл отпустят?"
    th "Сомневаюсь."
    th "Ведь сколько времени я уже тут?"
    th "Циклов 320-340. Даже не помню точно. Так что, даже если появится какая-то возможность выбраться отсюда с помощью магии чисел, я вряд ли смогу её заметить."
    th "Надоело."
    th "Хочу хоть какое-то разнообразие!"
    show mt angry panama pioneer close with dissolve
    $ save_name = ('День 1. Эээ... что?') 
    mt "Стоп!{w} Ты вообще не отыграваешь свою роль!{w} Какой это уже дубль?!"
    th "Вот тебе на..."
    th "Хотел разнообразие, получай!"
    "Осмотревшись, я заметил камеру, направленную на меня."
    me "Эээ... Первый?"
    mt "Очень смешно!"
    "Вожатая или теперь уже режиссёр, сняла с себя панамку и начала ей обмахиваться."
    show mt normal pioneer with dspr
    mt "Как же жарко..."
    show sh normal pioneer at right with dissolve
    sh "Так лето же."
    "Метко подметил непонятно откуда взявшийся Шурик."
    show mt rage pioneer with dspr
    mt "Без тебя знаю, дурень!{w} За камерой иди следи!"
    hide sh with dissolve
    "Шурик спокойно увернулся от запущенной в него панамки и вернулся на операторское место."
    th "Так... Значит Шурик у нас оператор, интересно..."
    hide mt with dissolve
    scene bg ext_bus with dissolve
    "Я вышел из автобуса."
    th "Вообще, надо бы подумать, что тут происходит, и что мне делать."
    th "..."
    th "..."
    th "Ладно, пока буду играть свою роль. Кто знает, вдруг этот мир на самом деле настоящий."
    "..."
    stop music fadeout 7
    th "Так что, пока буду относиться к этому миру как к настоящему.{w} В любом случае пожить другой жизнью, кроме жизни пионера и маньяка, будет полезно. Так сказать, для общего развития, хах."
    "Я решил, что всё-таки голод не тётка, и стоило бы послушаться Ольгу в кои-то веки. Поэтому я направился в столовую, дабы немного перекусить." 
    scene bg ext_camp_entrance_day with dissolve
    scene bg ext_clubs_day with dissolve
    scene bg ext_square_day with dissolve
    scene bg ext_dining_hall_away_day with dissolve
    scene bg ext_dining_hall_near_day with dissolve
    stop ambience fadeout 3
    play music music_list["dance_of_fireflies"] fadein 3
    play ambience ambience_camp_center_day fadein 1
    $ save_name = ('День 1. Обед.')
    "В дверях я столкнулся с Мику."
    show mi normal pioneer with dissolve
    mi "Как?"
    "Тут я прямо остолбенел."
    "Ладно, что \"Совёнок\" превратился в съемочную площадку, конечно, странно, но чтобы Мику ограничилась ОДНИМ СЛОВОМ, и даже не фразой - это точно предвещает скорый конец света."
    "А потом что? Лена станет кровожадной маньячкой, а Ульяна начнёт цитировать Ницше?"
    me "Эээ... никак, наверное."
    mi "Неудивительно."
    th "Ох, похоже, не с той ноги сегодня встала..."
    me "Я пойду поем."
    show mi smile pioneer with dspr
    mi "Ну пойдём, что ли."
    th "Ну, хоть не одним словом ответила, прогресс. А вообще складывается такое ощущение, что её подменили.{w} Хотя тут... кто знает?"
    stop ambience fadeout 2
    hide mi with dissolve
    "..."
    scene int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 1
    "На обед была лапша быстрого приготовления."
    th "Ого. Хотя даже удивляться не стоит, чего тут только может не быть."
    "Мельком проскочила мысль, что, возможно, тут у нас 21 век, но её прервала Мику... или не Мику?.."
    show mi dontlike pioneer with dissolve
    mi "Я когда-нибудь гастрит заработаю  с такой диетой."
    me "Пожалуй."
    mi "Ты-то тем более уж, весь реквизит выпил с этими деятелями!"
    th "Ахах, видимо, тот, кто был здесь до меня, времени зря не терял!"
    me "Надо же расслабиться иногда. Работа тяжелая, как-никак - главная роль!{w} Ну и не камеры же и светоотражающие плёнки пью!"
    th "Наверное..."
    show mi grin pioneer with dspr
    mi "Как будто на Оскар претендуешь!"
    me "Кто ж знает..."
    th "Хотя думаю если бы действительно вышел бы фильм про мою ситуацию, он бы вышел весьма интересным."
    "Внезапно я обнаружил у себя в карманах сигареты и очень обрадовался этому."
    th "Уже наверное цикла 4 не курил... Всё время в бардачке сиги забывал."
    "Я откинулся на спинку стула и закурил."
    show mi angry pioneer with dspr
    mi "Здесь вообще-то, детский лагерь, если ты не в курсе!"
    me "Правда что ли?"
    "Подумал и сказал я мысль вслух."
    "Мику ничего не ответила и фыркнула."
    "Я решил поддержать беседу и спросил:"
    me "А как тебе фильм кстати?"
    show mi normal pioneer with dspr
    mi "Ни одному нормальному человеку в голову бы не пришло такой бред снимать!"
    th "Ой подруга...{w} Тут ты непременно права. Действительно снимать такой бред в голову пришло не человеку, а лагерю.{w} Так ещё и не снимать, а в жизнь воплотить..."
    show mi scared pioneer with dspr
    "Мику боязливо огляделась, удостоверившись, что, больше никого тут, кроме нас нет, продолжила."
    show mi normal pioneer with dspr
    mi "Только нашей Ольге Дмитриевне."
    th "Похоже поспешил с выводами. Хотя кто знает, вдруг на самом деле тут Ольга всем заведует?"
    th "Нет, не думаю. Я же её убивал, но ничего она мне не сделала, и в следующем цикле никак не отреагировала.{w} Хотя это, скорее всего, была её копия."
    me "А почему ты, кстати, тогда снимаешься? Тебя разве кто-то заставлял...{w} заставляет?"
    th "Убью двух зайцев сразу. Вдруг на самом деле тут все настоящие, а я просто попал во вселенную их фильма?"
    show mi grin pioneer with dspr
    mi "Да-а-а?"
    "Ехидно протянула Мику"
    show mi normal pioneer with dspr
    mi "А что, у меня был выбор, по твоему? Или у тебя? Или у всех остальных?"
    th "Она про что? Они тоже тут застряли? Или она про другое?... Ай, спрошу, терять всё равно мне нечего."
    me "Вас тоже сюда закинула неведомая сила из реального мира?"
    show mi scared pioneer with dspr
    "Мику посмотрела на меня очень удивлёнными и испуганными  глазами."
    "Поняв, какую хрень ляпнул, я решил быстрее перевести тему."
    "Я заметил, что всё это время Мику сыпала перец в кружку и, похоже, не собиралась останавливаться."
    me "Я смотрю, ты любишь поострее."
    "Ухмыльнулся я."
    show mi shocked pioneer with dspr
    mi "Что?"
    "Во взгляде Мику, можно было прочитать очевидную растерянность  и она с ещё большим удивлением уставилась на меня, а я же, в свою очередь, кивнул в сторону её лапши."
    show mi upset pioneer with dspr
    mi "Ну вот..." 
    "Она грохнула перечницу об стол и расстроено уставилась на горку перца, которая, как айсберг, борющийся с глобальным потеплением, никак не хотела растворяться."
    play sound laugh_male
    me "Ахахаха, ну ты даешь!"
    "Сказал я, расхохотавшись на славу."
    show mi sad pioneer with dspr
    mi "Это всё ты виноват..."
    "Сказала Мику чуть не плача."
    "Я ухмыльнулся."
    th "Веселая картина."
    show mi rage pioneer with dspr
    "Мику от такой моей реакции сначала покраснела, потом позеленела, потом посинела и потом снова покраснела от злости."
    "Она взглянула на меня таким взглядом, что если бы, можно было им убить, то смерть моя была бы не из легких."
    show mi scared pioneer with dspr
    play sound sfx_open_door_squeak_2
    stop music fadeout 2
    "Хотела было она уже начать орать на меня, но тут, она неожиданно, с ужасом в глазах, посмотрела на дверь позади меня."
    "Я очень удивился её реакции , а когда обернулся и увидел там Славю, удивился в три раза сильнее."
    th "Как можно так бояться эту милую и трудолюбивую девушку?"
    "Однако через несколько секунд стало ясно."
    show sl laugh pioneer at right with dissolve
    play music music_list["eat_some_trouble"] fadeout 1
    sl "Маша-нян! Семён-кун!"
    "Видимо роль Мику тут играет Славя. А Мику в свою очередь никакая не Мику, а Маша.  Ну, впрочем, я так и предполагал."
    show mi angry pioneer with dspr
    ma "Я же тебе тысячу раз говорила - не называй меня так!"
    "Сквозь зубы проговорила Мик... тьфу ты, Маша."
    show sl smile pioneer at right with dspr
    "Славя рывком пододвинула стул и села рядом со мной. Причём очень близко..."
    "Слишком близко."
    "Хотя, впрочем, я не против."
    ma "Чёртова виабу... Как таких вообще в институт берут..."
    show sl laugh pioneer at right with dspr
    sl "Ня! Ня! А о чём вы тут разговаривали?"
    "Славя, похоже, не услышала реплики о своей профнепригодности."
    me "А мы тут обсуждали как мне стоило поступить с моей лапшой..."
    ma "Я тебе сейчас понякаю тут!"
    "Перебила меня Маша."
    play sound sfx_punch_medium
    "Она попыталась ударить меня в лоб, но я ловко остановил её руку и вернул её отправителю."
    show sl scared pioneer at right with dspr
    "Славя вскрикнула и задрожала."
    me "Видишь, как она недовольна?{w} Пытливая юная душа, не ищущая правоты, готовая к самоотречению и отказа от благ социального общества, и с большой вероятностью, уже готовая, к бегству от общества в лес."
    "Обратился я к Славе."
    show sl tender pioneer at right with dissolve
    sl "Ты такой умный!"
    "Мурлыкнула Славя и обхватила мою руку."
    th "Кайф...{w} Вот если бы Славя так всегда себя вела, может я б тогда на ней женился."
    show mi upset pioneer with dspr
    ma "Нет, ты точно конченый."
    me "Не знал, что нынче девушки разбрасываются комплиментами."
    "Снова ухмыльнулся я."
    "Маша достала телефон из кармана  и посмотрела на время"
    th "Охохо, и вправду 21 век. Жаль, что интернета тут, скорее всего, нет, соскучился уже по нему..."
    show mi normal pioneer with dspr
    ma "Ладно, пора."
    me "А?{w} Куда? Кому?"
    show mi dontlike pioneer with dspr
    ma "Тебе на съёмку, дурень!"
    show sl laugh pioneer at right with dspr
    sl "И мне, и мне!"
    "Славя запрыгала, не отпуская мою руку."
    me "Да, наверное."
    me "Пока."
    ma "Иди уже..."
    "Она фыркнула и отвернулась. Я тоже встал из-за стола и пошел на выход."
    hide sl with dissolve
    hide mi with dissolve
    sl "Иттекимас!"
    ma "Итена..."
    "Послышалось мне вслед, и в ту же секунду мимо меня пролетела Славя, а за ней пустой стаканчик от лапши..."
    stop music fadeout 4
    stop ambience fadeout 1
    scene bg black with dissolve
    scene bg int_bus with dissolve
    $ save_name = ('День 1. Дневные съёмки.')
    play music music_list["get_to_know_me_better"] fadein 2
    play ambience ambience_ext_road_day fadein 2 
    "Я сидел в автобусе и лениво перелистывал сценарий."
    th "Это таки моя история.{w} Со Славей.{w} И надо же, весь сценарий точь-в-точь. Ни капли отклонений."
    th "Может я тоже кукла? Просто мне встроили другую память не про жизнь в СССР, а про жизнь после?.."
    th "Бред какой, точно схожу с ума."
    "Я отложил пачку листов А4, и уставился в окно."
    th "Жарко.{w} Даже без заявлений Шурика - жарко."
    th "Кузнечики стрекочут.{w} И как на монтаже будут исправлять этот момент?"
    th "Ах да... Я же застрял в лагере без интернета, кому тут монтировать.{w} Хотя может Шура или Серега могут, они же тут по технической части, вроде как."
    th "..."
    th "Вот бы лагерь сжалился и дождь запустил. Или хотя бы в автобус кондиционер поставили."
    show mt angry panama pioneer with dissolve
    mt "Эй!{w} Алло!{w} Есть кто дома?"
    me "Абонент временно недост..."
    show mt rage panama pioneer with dissolve
    with vpunch
    mt "ВСЁ!{w} Чтобы это был последний дубль в автобусе!"
    hide mt with dissolve
    "Режиссёр вышла из автобуса."
    me "Я и сам того же хочу."
    scene bg black with dissolve
    "..."
    scene bg ext_bus with dissolve
    "Я сыграл сцену, где я выбегаю из Икаруса."
    "Теперь предстоит следующая сцена, где меня встречает Славя."
    "Я толком не запомнил сценарий, так что вся надежда на импровизацию и на мою память."
    scene bg ext_camp_entrance_day with dissolve
    show mt normal panama pioneer at cright with dissolve
    mt "Наконец-то все пришли, теперь можно снимать."
    mt "Все по местам!"
    mt "Камера!{w} Мотор!"
    hide mt with dissolve
    th "Надо вспомнить как я сюда попал в первый раз, или хотя бы в десятый, всё равно для меня тогда был первый раз." 
    th "Буду стоять, и с огромным удивлением рассматривать всё вокруг."
    "Пока я осматривался, из-за ворот вышла Славя."
    show sl smile2 pioneer far with dissolve
    show sl smile2 pioneer with dissolve
    show sl smile2 pioneer close with dissolve
    sl "Привет, Семён-кун! Меня Славя зовут! Ёрашикинэ!"
    stop music fadeout 1
    stop ambience fadeout 1
    "..."
    "Немая сцена..."
    "..." 
    hide sl with dissolve
    show sl smile2 pioneer at left with dissolve
    show mt sad panama pioneer at cright with dissolve
    play ambience ambience_ext_road_day fadein 1
    mt "Ты вообще читала сценарий?"
    "Грустно сказала Ольга Дмитриевна."
    show sl sad pioneer at cleft with dissolve
    play music music_list["heather"] fadein 2
    sl "Ну, читала, да, но там скучно же!"
    "Ольга закрыла лицо рукой."
    th "Никогда бы не подумал, что буду ТАК понимать Ольгу Дмитриевну."
    mt "Ладно, ладно, ещё раз."
    mt "Только, пожалуйста, придерживайся сценария. У нас итак мало времени."
    sl "Извините... Я попробую ещё раз."
    mt "Попробуй уж..."
    hide mt with dissolve
    hide sl with dissolve
    "Славя скрылась за воротами."
    "Я снова начал удивлённо оглядываться по сторонам."
    "Через несколько секунд Славя вышла из-за ворот."
    stop music fadeout 1
    show sl smile pioneer far with dissolve
    show sl smile pioneer with dissolve
    show sl smile pioneer close with dissolve
    sl "Ты, должно быть, новенький?"
    me "..."
    me "Ну... вроде того..."
    show sl smile2 pioneer close with dspr
    sl "Что же, добро пожаловать!"
    sl "Так тебе к вожатой надо, она всё расскажет!"
    sl "Смотри. Сейчас ты идёшь прямо-прямо, доходишь до площади, затем налево, дальше будут домики."
    sl "Тебе нужно к домику с треугольной крышей."
    sl "Всё понял?"
    me "Я...{w} эээ..."
    sl "Ладно, мне пора."
    "Она помахала рукой и скрылась за воротами."
    hide sl with dissolve
    show mt smile pioneer at right with dissolve
    mt "Стоп!{w} Снято!"
    mt "Можете же когда захотите!"
    "Ольга Дмитриевна сняла панамку и начала использовать её в качестве веера."
    show mt smile pioneer with dspr
    mt "Ладно, пока, пожалуй, всё. Перерыв!"
    me "Ура!"
    scene bg black with dissolve
    stop ambience fadeout 2
    "..."
    scene bg int_dining_hall_sunset with dissolve
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    $ save_name = ('День 1. Ужин.')
    play music music_list["dance_of_fireflies"] fadein 3
    play ambience ambience_dining_hall_empty fadein 3
    show dv normal pioneer at right with dissolve
    show mi normal pioneer at left with dissolve     
    show sl smile2 pioneer with dissolve
    "На ужине я присел за стол к Маше, Славе и Алисе."
    th "Вот блин, казалось бы, братья по разуму, современные люди, но о чём говорить, я так и не придумал."
    "На ужин была жареная картошка с грибами.{w} Очень вкусно, кстати."
    me "Кто это приготовил?"
    show sl shy pioneer with dspr
    sl "Эт-то я..."
    "Смущенно проговорила Славя."
    me "Славечка, это просто великолепно, такой вкусноты, цик... лет 300 не ел!"
    "Славя покраснела так сильно, что сильнее неё краснела, наверное, только Лена."
    show mi upset pioneer at left with dspr
    ma "Славечкой, он обзывается, посмотрите на него!{w} А дальше что? Будешь меня Микуськой называть?{w} Или Роутера Электроничком?"
    show dv laugh pioneer at right with dspr
    "Алиса, судя по всему, представила эту картину и расхохоталась."
    th "Блин, я-то и не подумал, что, если Мику зовут Машей, то и других могут по-другому звать."
    th "И как, тогда мне к этой блондинке с золотыми косами обращаться?{w} Славя-тян?"
    th "А что? Сто лет уже аниме не смотрел.{w} Хотя в моей ситуации можно предположить, что я сам в аниме попал, так зачем его тогда смотреть?"
    th "Риторический вопрос."
    "Славя, точнее неСлавя заступилась за меня."
    show sl angry pioneer with dspr
    sl "Маша! Семён-кун не такой!"
    dv "Да ладно тебе, Сашка! Это же шут-{w}ка."
    sa "Не смешно."
    th "Так значит это Сашка... Ладно буду знать.{w} А вообще она ничего такая, забавная."
    "Мысленно улыбнулся я."
    show dv normal pioneer with dspr
    "Над столом нависла тишина."
    "За это время Маша доела и так же молча ушла."
    stop ambience fadeout 3
    hide mi with dissolve
    "..."
    "В столовую зашла Ольга Дмитриевна и подошла к нашему столу."
    show sl normal pioneer with dspr
    show mt normal pioneer at left with dissolve
    mt "К ночным съёмкам готовы?"
    me "Ночным?{w} А что снимать будем?"
    mt "Сцену в лесу со Славей."
    "Я улыбнулся от воспоминания."
    th "Охохо...{w} Помню я эту сцену, такое не забудешь."
    show sl happy pioneer with dspr
    sa "Нани-нани?"
    "Саша услышала, что речь идёт о её героине, и встряла в беседу."
    mt "Только, пожалуйста..."
    mt "Придерживайся сценария в этот раз."
    sa "Хай-хай!"
    "Такой ответ бывшую вожатую не удовлетворил. Она фыркнула и ушла туда, откуда пришла."
    hide mt with dissolve
    dv "А что там за сцена?"
    me "Ну там я слежу за Славей в лесу возле озера."
    sa "Ня-ня! Как романтично!"
    me "И при этом она раздевается!"
    show sl scared pioneer with dspr
    sa "Ня?"
    "Саша уставилась на меня, в надежде, что я пошутил."
    sa "Ра...{w} раздевается?"
    me "Угу.{w} Полностью."
    show dv laugh pioneer at right with dspr
    dv "Ай да Сенька! Ай да извращюга!"
    me "А то!"
    "Сказал я и ухмыльнулся."
    show sl shy pioneer with dspr
    sa "Ну если это с тобой..."
    th "Ой, Сашка, Сашка..."
    show dv grin pioneer at right with dspr
    dv "А там будет {i}это{/i}?"
    th "Ой, Алиска, Алиска..."
    show sl surprise pioneer with dspr
    sa "Что?"
    me "В {b}этой{/b} сцене не будет."
    show dv smile pioneer at right with dspr
    dv "Ах, вот как..."
    "Алиса ехидно протянула свою реплику."
    dv "Значит будет позже."
    dv "Может, поведаешь, зачем в кино такие сцены добавлять?"
    me "Искусство, все дела..."
    "Задумчиво сказал я."
    "..."
    "..."
    dv "Ладно, я пойду."
    hide dv with dissolve
    "Алиса встала из-за стола, оставив меня наедине с Сашей, которая, судя по всему, ещё не успела отойти от услышанного."
    sa "Что такое {i}это{/i}? Что будет?"
    me "Площадь подметать будем."
    "Саша всё так же непонимающе уставилась на меня."
    me "Ладно, пошли, солнце скоро сядет."
    sa "А?{w} Да-да пошли..."
    hide sl with dissolve
    "Убравши свои тарелки, мы вышли из столовой."
    stop music fadeout 2
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_houses_sunset with dissolve
    "Когда мы направлялись на съёмки меня посетила мысль."
    th "А зачем, собственно говоря, мне это надо?"
    menu:
        "Пойти на съёмки":
            $ snim_ochki += 2
            $ odin_ochki -= 2
        "Сбежать":
            $ odin_ochki += 2  
            $ snim_ochki -= 2
    
    if odin_ochki >= 2:
        jump somesing_new_odinochka_rut
    else:
        jump somesing_new_snimaem
    
    
    
    
label somesing_new_odinochka_rut:
    th "А ведь действительно, мне это к чёрту не сдалось."
    th "Какой-то фильм снимать... зачем, если можно спокойно полежать где-нибудь на берегу реки и не очём не думать."
    "В общем, я решил сбежать."
    me "Саша, иди без меня, мне в туалет надо."
    show sl happy pioneer with dissolve
    sa "Семён-кун, я тебя подожду, ня!"
    me "Иди-иди Саш, я надолго."
    sl "Ничего страшного, я тебя долго подожду, ня!"
    me "Саша."
    "Строго сказал я."
    show sl sad pioneer with dissolve
    sa "Ладно..."
    hide sl with dissolve
    "Саша отвязалась от меня и ушла."
    th "Как же она мозг выедает. Кажется теперь я понимаю, почему Маша её так не любит."
    stop ambience fadeout 4
    "Я подождал пока Саша окончательно скроется из моего поля зрения и пошел в сторону столовой."
    $ save_name = ('День 1. Вечер в одиночестве.')
    scene bg ext_beach_night with dissolve
    play ambience ambience_lake_shore_night fadein 2
    play music shape_of_my_heart fadein 7
    "Я вышел на пляж."
    "Пока я шёл, уже окончательно стемнело."
    "Над пляжем воцарилась атмосфера сумеречного волшебства."
    th "Сейчас бы на песочке полежать и на звёзды смотреть..."
    scene bg zvezdy with dissolve
    th "Ну, а кто мне мешает?{w} Правильно - никто."
    "Я невольно медитировал. Глядел на небо и не о чём ни думал."
    "Но всё же через некоторое время в мою голову пробралась мысль:"
    th "Надо бы закурить..."
    "Я достал сигарету и закурил."
    play sound zazheg_sigaru
    $ renpy.pause(9)
    th "Вот так, ещё лучше."
    th "Делать мне нечего, сниматься где-то, когда можно отдыхать."
    "..."
    play sound kurit
    th "Что же мне делать дальше?"
    th "А вдруг я, в этот раз, действительно уеду в Райцентр или что тут у них?"
    th "Что я тогда буду делать?"
    "..."
    play sound kurit
    th "Не знаю, наверное как-нибудь разберусь с документами, и буду общаться с моими знакомыми отсюда...{w}А главное, что я выберусь."
    th "Хм, забавно... так рассуждаю, будто бы это в самом деле скоро произойдёт."
    "Сигарета кончилась."
    th "Не беда, у меня есть ещё пачка."
    "Я достал пачку, но сигарет в ней не оказалось."
    th "Вот блин..."
    th "Ай чёрт с ними!"
    play sound sfx_cigarette_pack_crumple 
    "Я смял и выкинул пачку сигарет куда-то влево."
    "Я прилёг на песок и решил по медитировать с закрытыми глазами."
    show blink
    th "Хорошо..."
    "Но я немного перестарался и уснул."
    stop music fadeout 2
    stop ambience fadeout 2
    "..."
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    scene bg black
    with fade3
    $ backdrop = "sunset"
    $ new_chapter(2, "День 2.  Я пионер... опять!?")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "sunset"
    $ sunset_time()    
    $ persistent.sprite_time = "sunset"
    window show
    play sound sfx_face_slap
    $ renpy.pause(1, hard=True)
    play sound sfx_face_slap
    play ambience ambience_lake_shore_evening fadein 5
    un "Семён, очнись!"
    "Я почувствовал как кто-то бьёт меня по щекам."
    hide blink
    $ renpy.pause(1, hard=True)
    scene bg ext_beach_sunset
    show un sad pioneer
    show unblink
    $ renpy.pause(1, hard=True)
    un "Семён?"
    play music music_list["trapped_in_dreams"] fadein 5
    "Этим \"кем-то\" оказалась Лена."
    me "М-м-м?"
    "Сонно промычал я."
    un "Ты в порядке?"
    me "Да, я просто вчера съёмки прогуливал и тут уснул."
    un "Съёмки?"
    me "Ну, мы же тут вроде как фильм снимаем?"
    un "О-о-о...{w} Похоже у тебя солнечный удар..."
    me "Что?"
    un "Какие к чёрту съёмки?"
    me "Ну, я же вчера проснулся, а потом, все начали гово...{w} Так стоп, тут нет никаких съёмок?"
    un "Нет."
    me "То есть мы сейчас находимся в Пионерском лагере \"Совёнок\"?"
    un "Да."
    me "А-а-а-а-а..."
    "..."
    play sound laugh_male
    me "Ахахахаха..."
    show un surprise pioneer with dspr
    un "Т-ты ч-чего? У тебя всё в п-порядке?"
    me "Конечно!"
    th "Конечно нет! У меня уже походу память того... или уже начинаю в галлюцинациях жить..."
    th "Хотя может, я уже..."
    me "Ладно, я пойду домой, а то небось вожатая запереживалась уже."
    show un shy pioneer with dspr
    un "Х-хорошо..."
    stop music fadeout 5
    scene bg black with dissolve2
    pause 3.0
    scene bg ext_house_of_mt_sunset with dissolve2
    play ambience ambience_camp_center_day fadein 2
    th "И как мне оправдоваться перед Ольгой?"
    th "..."
    th "Я что, всерьёз сейчас подумал, что мне надо оправдываться перед ней?"
    play sound sfx_open_door_1 
    scene bg int_house_of_mt_sunset with dissolve
    play ambience ambience_int_cabin_evening  fadein 2 
    "Зайдя в домик, оказалось, что Дмитриевна спит."
    th "Это ж сколько сейчас, тогда, времени?"
    "Я посмотрел на часы."
    th "Ох ё...{w} И что ж Лена в такую рань на пляже забыла?"
    "На часах было 4:30 утра."
    th "В любом случае, спасибо ей."
    "Я просто лёг на кровать и опять уснул."
    show blink 
    stop ambience fadeout 2
    window hide dissolve
    pause 3.0
    $ renpy.pause(1, hard=True)
    scene bg black
    $ persistent.sprite_time = "day"
    $ day_time()  
    mt "Семён!{w} Семён линейку проспишь!"
    hide blink
    scene bg int_house_of_mt_day
    show mt angry pioneer
    show unblink 
    "Будто бы я на неё пойду..."
    mt "Просыпайся, умывайся, и шагом марш на линейку!"
    me "Да-да, всё непременно..."
    show mt grin pioneer with dspr
    mt "Вот и славно."
    "Вожатая, развернулась и вышла из помещения."
    hide mt with dissolve
    play sound sfx_open_door_2
    "..."
    play music music_list["your_bright_side"] fadein 6
    th "На линейку я точно не пойду."
    th "Тогда куда?"
    th "..."
    th "В теории можно пойти почитать, давненько этим не занимался."
    th "Или, можно, пока Мику на линейке, пойти подергать струны на гитаре."
    menu:
        "Пойти почитать":
            $ bbl_ochki += 2
            $ muz_ochki -= 2
        "Поиграть на гитаре":
            $ muz_ochki += 2
            $ bbl_ochki -= 2
    if muz_ochki >= 2:
        jump somesing_new_day2_miku
    else:
        jump somesing_new_day2_lena
    

label somesing_new_day2_miku:
    "Лучше поиграю на гитаре, всё таки люблю это дело."
    "Я с твёрдым намеринием поиграть на гитаре отправился в музыкальный клуб."
    stop music fadeout 3
    scene bg black with dissolve2
    pause 3.4
    scene bg ext_musclub_day with dissolve
    $ save_name = ('День 2. Белая ночь.')
    play ambience ambience_camp_center_day fadein 3
    pause 2.0
    scene bg ext_musclub_near_day with dissolve
    th "Надо проверить ручку, вдруг Мику забыла закрыть."
    play sound sfx_open_door_1 
    th "Шик."
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 3
    "Дверь, действительно оказалась открыта."
    th "Недавно одну песню слышал где-то, уж очень мне она понравилась, попробую по памяти сыграть."
    th "Только вот, слов не помню..."
    "{b}Сейчас играет - В. Салтыков — Белая ночь (guitar cover by Paul Starkoshevsky){/b}"
    stop ambience fadeout 3
    play music belaya_noch_guitar fadein 3
    "..."
    $ renpy.pause (13.9, hard=True)
    "{b}Если вы хотите пропустить нажмите на экран.{/b}"
    stop music fadeout 3
    show mi smile pioneer with dissolve 
    play ambience ambience_music_club_day fadein 3
    mi "Здорово! Семён, почему ты не говорил, что играешь на гитаре?"
    th "Упс..."
    me "Я... ну...{w} это...{w} зашёл."
    mi "Ничего страшного, ты же ничего плохого не сделал и вообще это я виновата, что забыла закрыть, вот сейчас вернулась, а ты тут..."
    show mi shy pioneer with dspr
    mi "Играешь..."
    me "Прости.{w} Так можно я поиграю?"
    show mi smile pioneer with dspr
    mi "Конечно-конечно!"
    show mi shy pioneer with dspr
    mi "А можешь...{w} ещё раз сыграть эту мелодию..."
    me "Тебе она так понравилась?"
    show mi normal pioneer with dspr
    mi "Нет, то есть да, то есть не совсем, в смысле я напеть хочу."
    me "Не вопрос."
    "{b}Сейчас играет: В. Салтыков — Белая ночь (cover be Yulya Koshkina) {/b}"
    scene cg d4_mi_sing with dissolve
    play music belaya_noch_cover
    mi " "

    return

label somesing_new_day2_lena:
    th "Думаю для разнообразия стоит пойти почитать."
    th "Частично я из-за книг не тронулся умом окончательно."
    th "Даже не знаю, что будет, когда я всё прочту..."
    "Немного подавленный от этой мысли, я отправился в библиотеку."
    stop music fadeout 3
    scene bg black with dissolve2
    pause 3.4
    scene bg ext_library_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "..."
    th "Чтобы взять на этот раз?.."
    play sound sfx_open_cabinet_1 
    scene bg int_library_day with dissolve
    $ save_name = ('День 2. Мои стихи.')
    play ambience ambience_library_day fadein 3
    "Библиотека, мне на радость, была открытой."
    th "Странно, но это даже к лучшему – не нужно будет заниматься нелегальной деятельностью."
    un "Кто тут?"
    "Из-за шкафов вышла Лена."
    show un normal pioneer far with dissolve
    "Как только меня у видела лена, она улыбнулась и подошла ко мне."
    show un smile pioneer with dspr
    me "Э-э-э{w}, а ты почему не на линейке?"
    show un grin pioneer with dspr
    un "По той же причине, что и ты."
    me "Понятно."



    return 
    
label somesing_new_snimaem:
    "Но я быстро отсёк эту мысль."
    th "Ну уж нет!{w} Вдруг это шанс, чтобы выбраться из лагеря, а я сейчас его истрачу."
    "Я пошёл дальше вместе с Сашей."
    scene bg black with dissolve
    "..."
    stop music fadeout 1
    scene bg ext_polyana_night with dissolve
    $ save_name = ('День 1. Вечерние съёмки.')
    play ambience ambience_forest_night fadein 3
    $ persistent.sprite_time = "night"
    $ night_time()
    "К вечеру похолодало.{w} Даже слишком."
    th "Но мы люди не привередливые, поэтому закаляемся."
    show mi dontlike pioneer at cright with dissolve
    mi "И почему я этим должна заниматься? Меня ведь даже в этой сцене нет!"
    "Маша натягивала светоотражающее полотно."
    show mt normal pioneer at cleft with dissolve
    mt "А кому ещё? У нас нехватка кадров!"
    show mi grin pioneer at cright with dspr
    mi "Вот взяли б больше народу! В съёмках такого шедевра любой бы согласился поучаствовать."
    show mt angry pioneer at cleft with dspr
    mt "Ты чем-то не довольна?"
    "Ольга Дмитриевна грозно посмотрела на неё."
    show mi normal pioneer at cright with dspr
    mi "Н...нет, всё в порядке."
    "Мне даже стало жалко Машу. Всё-таки запрягли снимать фильм, который, скорее всего никогда не выйдет и заставили работать над сценой, где она даже не будет присутствовать."
    "..."
    hide mt with dissolve
    hide mi with dissolve
    scene bg black with dissolve
    scene bg ext_polyana_night with dissolve
    "..."
    show sh normal pioneer at cright with dissolve
    show el normal pioneer at cleft with dissolve
    "Ко мне подошли Шурик и Электроник."
    th "Или как там его Маша назвала?{w} Роутер вроде."
    sh "Как думаешь, снимем за два-три дубля?"
    me "Не знаю, это не от меня зависит, мне-то надо просто стоять и смотреть.{w} Но по правде говоря хотелось бы подольше поснимать."
    show sh laugh pioneer at cright with dspr
    show el laugh pioneer at cleft with dspr
    ro "Хах, понимаю."
    sh "Да уж... От тебя стоило ожидать такого ответа."
    "Посмеиваясь сказал Шурик."
    show sh normal pioneer at cright with dspr
    show el smile pioneer at cleft with dspr
    ro "Ладно, мы пойдём готовиться, скоро уже надо будет снимать."
    me "Давайте, пацаны, удачи."
    hide sh with dissolve
    hide el with dissolve
    "..."
    th "Теперь заняться нечем, остается только ждать..."
    "..."
    th "Не, надоедает."
    th "А времени то ещё, ого-го."
    "Я заметил Сашу, которая стоит и волнуется из-за того, что она будет раздеваться перед людьми."
    th "Может, стоит подойти к ней и поддержать, пока заняться нечем?"
    th "Или вон Маша, мучается с тем полотном, может ей помочь?"
    menu:
        "Чем заняться?"
        "Подойти поддержать Сашу":
                                $ sa_ochki += 2
                                $ ma_ochki -= 2
                                $ dv_ochki -= 2
        "Помочь Маше":
                    $ ma_ochki += 2  
                    $ sa_ochki -= 2
                    $ dv_ochki -= 2
        "Закурить":
            $ dv_ochki += 2
            $ ma_ochki -= 2
            $ sa_ochki -= 2
    
    if ma_ochki >= 2:
        jump somesing_new_masha_rut
    elif dv_ochki == 2:
        jump somesing_new_dvache_rut
    else:
        jump somesing_new_sasha_rut
    
    
label somesing_new_sasha_rut:
    play music beat_of_nature fadein 3
    th "Думаю, пойду подбодрю Сашу, она таки славная малая, но что-то совсем раскисла."
    show sl scared pioneer close with dissolve
    me "Саша, ты нормально себя чувствуешь?"
    sa "М-мне страшно..."
    me "Не переживай ты так, тут все свои, так ещё и большинство  уйдут чтобы тебя лишний раз не смущать."
    sa "А Шурик и Роутер?"
    me "Да неприятно конечно, но ничего же страшного с тобой не произойдёт, ничего от тебя не убудет в конце-то концов..."
    show sl sad pioneer close with dspr
    sa "Да, но... мне будет не приятно, что кто-то кроме тебя, увидит меня..."
    show sl tender pioneer close with dspr
    sa "В таком виде..."
    me "Что?"
    "Искренне удивился я такому признанию."
    show sl shy pioneer close with dspr
    sa "О-ой..."
    mt "Всё готово!{w} Все по местам!"
    sa "М-мне п-пожал-л-луй п-пора..."
    hide sl with dissolve
    "Саша побежала на место съёмки, но через пару секунд развернулась ко мне и громко сказала:"
    show sl shy pioneer far with dissolve
    sa "С-спасибо тебе, я теперь про съёмки так н-не переживаю."
    hide sl with dissolve
    me "Пожалуйста."
    "Я постоял так в ступоре секунд 5, а потом подумал:"
    th "Ещё бы тебе сейчас за съёмки переживать, когда только что, призналась парню, что хочешь перед ним раздеться."
    th "Ой Саша...{w} Тот ещё кадр..."
    stop music fadeout 3
    "..."
    mt "Камера!{w}Мотор!"
    scene cg sl_swimming_dal with dissolve
    stop ambience
    play music music_list["forest_maiden"]
    "Саша разделась и вышла в озеро."
    th "Завораживающе...{w} Как будто в первый раз смотрю..."
    th "Ладно, мой выход."
    scene cg sl_swimming_bliz with dissolve
    "Я тихонечко пошел в сторону озера и засел в кусты."
    th "Хах, отсюда видок, ещё лучше. Вечность бы так провел."
    th "Надо бы быть по аккуратнее со словами, а то помню в первый цикл, хотел остаться тут навечно."
    "Спустя секунд 20 я зашелестел кустами, по сценарию."
    sa "Кто тут?"
    "Саша быстро накинула на себя рубашку и упорхнула в сторону леса."
    stop music fadeout 3
    play ambience ambience_forest_night
    scene bg ext_polyana_night with dissolve
    mt "Стоп!{w} Снято!"
    show mt grin pioneer with dissolve
    mt "Вот всегда бы так! С первого дубля! Тогда бы, может, успели бы за эти 3 недели всё отснять!"
    me "Всё? Я пойду отдыхать."
    show mt smile pioneer with dspr
    mt "Иди."
    "Я неспешно отправился в бывший домик вожатой."
    hide mt with dissolve
    scene bg black with dissolve
    "..."
    scene bg ext_square_night with dissolve
    play music just_relax fadein 2
    play ambience ambience_camp_center_night
    th "Надеюсь, в этом лагере, я живу в нём."
    "На площади я встретил Сашу."
    show sl happy pioneer with dissolve
    sa "Привет, Семён-кун!"
    me "Привет, Сашка-тян!"
    show sl surprise pioneer with dspr
    sa "О-ого."
    show sl laugh pioneer with dspr
    "Саша поначалу удивилась моей реплике, а потом чуть-ли не засияла от радости."
    th "Да, что уж, я сам в шоке, как такое сказал."
    sa "Ура, Семён-кун! Я так рада, меня так ещё никто не называл!"
    "..."
    show sl smile2 pioneer with dspr
    sa "Сашка-тяяян..."
    "Довольно протянула Саша."
    me "Да, ладно тебе."
    show sl laugh pioneer with dspr
    sa "Ну ты омоширои!"
    "Я улыбнулся глядя на смеющуюся Сашу."
    show sl normal pioneer with dspr
    sa "А как тебе сцена? Как я сыграла?"
    show sl shy pioneer with dspr
    sa "Тебе п-понравилось?"
    me "Сашка-тян, как такой вид может не понравиться?"
    sa "С-спасибо."
    me "Да не за что."
    show sl normal pioneer with dspr
    sa "Слу-у-у-ушай, не хочешь ко мне зайти на чай?"
    me "Ну, почему нет?{w} Пошли."
    show sl happy pioneer with dspr
    sa "Ура, ура! Пошли, Сеня-кун!"
    stop music fadeout 1
    hide sl with dissolve
    stop music fadeout 2
    scene bg black
    "..."
    scene bg ext_house_of_sl_night with dissolve
    "Мы подошли к домику Саши."
    show sl shy pioneer with dissolve
    play music beat_of_nature fadein 3
    sa "Я больше не могу..."
    me "Что случилось?"
    show sl tender pioneer with dspr
    sa "Семён-кун, я так больше не могу! Я сильно-сильно тебя люблю! С того момента как я перешла в наш универ сразу в тебя влюбилась, а с того момента как мы приехали в лагерь снимать фильм, я тебя полюбила ещё сильнее!"
    sa "Ты такой милый, заботливый, даже сейчас спрашиваешь что случилось, я знаю ты умный и смелый,{w} я знаю ты крутой и смешной.{w} Я очень хочу о тебе заботиться, готовить, проводить с тобой всё свободное время, я хочу быть с тобой вместе!"
    "..."
    sa "Пожалуйста..."
    th "А как мне надо реагировать в такой ситуации? Когда девушка едва знакомая тебе день признается в любви..."
    th "Нет безусловна она симпатичная, но так быстро да."
    th "..."
    th "И почему я вообще об этом задумываюсь, конечно..."
    me "Хорошо, я буду с тобой вместе, ты мне тоже нравишься."
    "Саша стала настолько счастливой, что даже не знала как её отреагировать и она просто стояла в ступоре."
    "Я же времени зря не терял. Подошел к ней, взял за руку, притянул к себе и..."
    scene cg poceluy_slavya with dissolve 
    "И поцеловал..."
    "..."
    "Время на несколько секунд, как бы это парадоксально не звучало, действительно остановилось."
    "Казалось что есть только Я и Она.{w} Есть только Мы."
    "За эти секунды, я наконец-то ощутил счастье, которого мне так не хватало."
    "Которого, много кому, так не хватает..."
    "Я наконец-то решил отпрянуть от Саши."
    scene bg ext_house_of_sl_night with dissolve
    show sl tender pioneer with dissolve
    me "Ну как?"
    sa "Это...{w} это так...{w} я так счастлива!"
    me "Я тоже."
    "..."
    "Мы минуту стояли и глупо друг другу улыбались."
    sa "Зайдём ко мне?"
    me "А?{w} А да-да пошли."
    stop music fadeout 3
    stop ambience fadeout 1
    scene bg int_house_of_sl_night with dissolve
    play ambience ambience_int_cabin_night fadein 2
    sa "Заходи-заходи, не стесняйся."
    $ persistent.sprite_time = "day"
    $ day_time()
    play sound vkl 
    scene bg int_house_of_sl_light_night with dspr
    show sl tender pioneer with dissolve
    th "Уж кто-бы говорил..."
    show sl normal pioneer with dspr
    "Мы молча сели на одну кровать, и уставились друг на дружку."
    show sl normal pioneer close with dspr
    me "Сашка-тян, а ты хочешь попробовать {i}это{/i}?"
    sa "То самое, о чём вы говорили с Алисой?"
    me "Да."
    show sl shy pioneer close with dspr
    sa "Ну давай."
    me "Раздевайся."
    show sl surprise pioneer close with dspr
    sa "Что?"
    me "Доверься мне, всё будет хорошо. И главное будет приятно."
    show sl shy pioneer close with dspr
    sa "Ну если ты так говоришь..."
    show sl tender swim close with dissolve
    "Саша сняла рубашку и юбку."
    show sl tender2 naked close with dissolve
    "А потом и лифчик."
    me "А те-е-еперь, Сашка, просто ложись на кровать и расслабься."
    sa "Х-хорошо..."
    hide sl with dissolve
    "Саша легла."
    me "Раздвигай ноги."
    sa "Зачем?"
    me "Раздвигай говорю."
    sa "Л-ладно."
    stop ambience fadeout 2
    scene cg sl_hentai_1 with dissolve
    play music music_list["forest_maiden"]
    "Саша всё же послушалась."
    "Я навалился на Сашу и вошел в неё."
    sa "Ааах. Больно."
    me "Сейчас, потерпи немного и станет приятно. Обещаю."
    "..."
    sa "С-семён..."
    sa "Эт-то оч-чень прият-тно..."
    me "Я же говорил."
    "Этот момент был чудесный.{w} Эта ночь была чудесной."
    "Этой ночью Я и Она, окончательно стали Нами."
    scene bg black with dissolve
    "..."
    stop music fadeout 2
    play ambience ambience_int_cabin_night fadein 2
    scene bg int_house_of_sl_light_night with dissolve
    "Мы выдохлись и оба упали на кровать."
    me "Ну как?"
    show sl tender2 naked close with dissolve
    sa "Это был самый лучший момент в моей жизни!"
    me "Вот видишь. А ты переживала..."
    sa "Я спа-а-ать хочу."
    "Зевнула Саша."
    me "Хорошо, сейчас вырублю свет, и спокойной ночи."
    hide sl with dissolve
    "..."
    play sound vkl
    scene bg int_house_of_sl_night with dissolve
    $ persistent.sprite_time = "night"
    "Я выключил свет."
    show sl tender2 naked close with dissolve
    "И лёг обратно к Саше."
    sa "Спокойной ночи..."
    show blink
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    $ backdrop = "days"
    $ new_chapter(2, "День 2. Неспокойный лагерь.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "days"
    $ day_time()    
    $ persistent.sprite_time = "day"
    hide blink
    $ renpy.pause(1, hard=True)
    scene bg int_house_of_sl_day
    show unblink
    window show dissolve
    jump somesing_new_sasha_rut_day2
    
label somesing_new_sasha_rut_day2:    
    play ambience ambience_int_cabin_day
    "Я проснулся поздним утром."
    "Саша всё ещё спала. Спала, кстати на моей руке."
    "Я вытащил руку, из-под Саши и оделся."
    "Хотел уже было закурить, но сигарет в шортах не обнаружил."
    th "Ну и ладно.{w} Теперь у меня есть кое-что, что получше сигарет будет."
    "Я взглянул на Сашу." 
    "Погладил её и решил выйти на улицу, прогуляться, и заодно зайти в свой местный домик."
    stop ambience fadeout 2
    scene bg ext_houses_day with dissolve
    play music music_list["get_to_know_me_better"]
    "..."
    "По дороге я встретил местного Электроника."
    th "Как там его...{w} Маршрутизатор что ли..."
    show el smile pioneer with dissolve
    el "Привет, Семён!"
    me "Ну здоров, что ли. Как у вас дела с подготовкой? Когда будем что-то снимать?"
    el "Не понял. Зачем нам что-то снимать? Нам собрать побыстрее, а не снимать."
    me "Теперь я не понял...{w} Ладно до встречи, позовёте мене если что."
    hide el with dissolve
    el "Ого, с радостью!"
    "Бросил мне, вслед местный Эл."
    th "У меня такое ощущение, что мы друг друга не поняли..."
    scene bg ext_house_of_mt_day with dissolve
    "Я пришёл к своему, я так полагаю здешнему домику."
    th "Ну, надеюсь это не домик Ольги Дмитриевны."
    play sound sfx_open_door_1
    scene bg int_house_of_mt_day with dissolve
    show mt normal pioneer with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Блин.{w} Прогадал."
    mt "Изволишь объясниться?"
    me "А?{w} Что такое?"
    show mt angry pioneer with dspr
    mt "Где ты всю ночь пропадал?!"
    th "Вот тебе на.{w} Видимо, всё-таки не прогадал. Просто и тут моя соседка Ольга Дмитриевна...{w} Даже тут..."
    me "С Сашей."
    th "Ну, мы в конце концов уже взрослые люди, в университете, вроде как, учимся. Так что скрывать незачем.{w} Хотя по Саше, такого, конечно, не скажешь."
    show mt surprise pioneer with dspr
    mt "С кем?"
    "Ольга удивлённо спросила."
    me "С Сашей."
    "Спокойно повторил я."
    show mt angry pioneer with dspr
    mt "И что вы с ним делали?"
    me "А вот это вас уже не должно касаться.{w} И почему это с ним, а не с ней?"
    mt "Семён, как это не моё дело? У меня тут пропал пионер, и он заявляет, что всю ночь был с каким-то Сашей, так это, ещё и девочка!"
    "Тут я, кажется, понял, почему мы с Роутером друг друга не поняли.{w} Точнее с Элом."
    me "Кстати, а не подскажите во сколько сегодня линейка?"
    show mt normal pioneer with dspr
    mt "Ах, да. Хотела предупредить, что линейка сегодня будет в 12."
    th "Теперь ясно. Я снова вернулся в пионерский лагерь. Теперь надо узнать, попал я сюда один, или с Сашей."
    me "Ясно, спасибо, я пойду."
    show mt angry pioneer with dspr
    mt "Так стоп! Зубы мне тут не заговаривай! Такое поведение для образцового пионера..."
    stop ambience fadeout 1
    play sound sfx_close_door_1 
    scene bg ext_house_of_mt_day with dissolve
    stop music fadeout 2
    "Остаток фразы вожатой, я оставил за дверью."
    play ambience ambience_camp_center_day
    play music music_list["trapped_in_dreams"] fadein 3
    th "Итак... Что мы имеем?"
    th "Вчера я попал в другой лагерь, где снимали фильм, а сегодня я уже на старом месте."
    th "Главный вопрос, попала ли сюда, вместе со мной Саша."
    th "А вообще мне вся эта движуха, ой как не нравиться...{w} Плохое предчувствие."
    th "Наверное, это потому что, я могу оказаться тут без моего новообретенного счастья.{w} Пока тут нечего опасаться, конечно же, исключая то что я здесь навсегда."
    th "Но если Сашки тут нет, то я точно устрою резню бензопилой \"Дружба\"."
    th "Ладно, может, я зря панику развёл, может, она сейчас лежит и мирно спит."
    th "В любом случае, не проверю - не узнаю. Так что пойду, проведаю её."
    stop music fadeout 3
    scene bg ext_houses_day with dissolve
    scene bg ext_house_of_sl_day with dissolve
    th "Ну, с богом!"
    scene bg int_house_of_sl_day with dissolve
    play sound sfx_open_door_1
    stop ambience fadeout 1
    play ambience ambience_int_cabin_day fadein 2
    "Я зашёл внутрь."
    show sl cry swim with dissolve
    "И увидел Сашу. Она сидела в углу, вся бледная, плакала, обхватив ноги руками."
    "Я подошёл к ней и спросил:"
    show sl cry swim close with dspr
    me "Саша?"
    show sl cry swim close with dspr
    play music music_list["you_lost_me"]
    sa "С-с-семён? Это ты, не пионер?"
    "Я засиял от счастья, что Саша попала сюда тоже."
    me "Конечно! Я оттуда же, откуда и ты."
    show sl tender swim close with dspr
    "Саша кинулась ко мне в объятья."
    sa "С-с-семён..."
    me "Расскажешь, что случилось?"
    "Саша, отпрянула от меня."
    show sl sad swim close with dspr
    sa "Приходила Таня."
    me "Кто?"
    sa "Ну Таня.{w} Но она вела себя не так как обычно..."
    sa "Да, Таня, конечно, л-любит поворчать, но сегодня слишком уж взъелась на меня."
    me "А что ты ей сказала?"
    sa "Я спросила почему она так рано приехала, и начала расспрашивать, что да как... Потому что как я знала она, вместе с остальными, приедет, только, через пару дней."
    sa "Таня мне грубо ответила, что тут уже неделю как...{w} Но я точно помню, что она с нами не приезжала, и её с нами, эту неделю, не было."
    show sl scared swim close with dspr
    sa "А п-потом она н-начала странно говорить. Говорить про какую-ю-то линейку, каких-то пионерских з-заданиях, и о том, как славно она просидела вчера весь день в библиотеке."
    th "Значит Таня это Женя. Хотя мне уже эта информация ни к чему."
    sa "А ещ-щё он-на почему-то н-назвала меня Славей... Нет я конечно тоже люблю так прикалываться над Машей, но я же шутя, а она на полном с-серьёзе..."
    sa "Эт-то т-точно была не наша Т-таня..."
    "Саша уткнулась мне в плечо, своим личиком."
    me "Саша, у меня для тебя две новости, хорошая и плохая, с какой начать?"
    sa "Н-ну, д-д-давай с х-хорошей..."
    me "Я знаю что тут происходит."
    show sl surprise swim close with dspr
    sa "Что?{w} Откуда?"
    me "Неважно. Теперь вторая новость"
    sa "Ну, г-говор-ри её."
    me "Мы попали в самый, что ни на есть, настоящий, пионерский лагерь \"Совёнок\"!"
    show sl scared swim close with dspr
    sa "Чт-то?{w} Т-то есть как это, попали?"
    me "В мистическое место, в наш фильм, в мою жизнь, называй как хочешь. Нас просто взяла и закинула сюда мистическая сила."
    sa "И к-как ты это понял?"
    me "Неважно. Сейчас важно то, что нам теперь нужно делать."
    sa "И ч-что же нам н-нужно делать?"
    me "Жить обычной пионерской жизнью, до конца смены."
    show sl surprise swim close with dspr
    sa "И всё?"
    me "И всё."
    sa "А потом что?"
    me "А вот это, Ватсон, правильный вопрос!"
    "Саша вопросительно посмотрела на меня."
    me "Загвоздка в том, что мы не вернёмся домой{w} ни-{w}ког-{w}да."
    show sl scared swim close with dspr
    sa "Как? Но такого же не бывает!"
    me "Бывает. А вот как, это уже хороший вопрос."
    me "Мы тут находимся в цикле, так сказать. Всё повторяеться бесчисленное количество раз, и всё одно и тоже из раза в раз."
    sa "Отк-куда т-ты эт-то знаешь?"
    me "Охохо, ты точно хочешь знать это?"
    sa "Д-да."
    me "Я сам прошел тут около 300 циклов."
    sa "Как так?.."
    me "Вот как-то так..."
    sa "И что делать? Мы будем тут до смерти?"
    me "Не знаю, в этот раз всё по другому. Взять хотя бы то, что я проснулся не в \"Совёнке\", а на съёмочной площадке."
    me "И ещё,{w} Ты рядом со мной."
    show sl shy swim close with dspr
    me "А это, может означать, что мы наконец-то сможем выбраться! Вместе!"
    show sl sad swim close with dspr
    sa "Хорошо, я тебе верю, но что нам делать, сейчас?"
    me "Жить, так сказать, в нашем фильме."
    sa "Хорошо...{w} Пойдем куда-нибудь?"
    play sound sfx_dinner_jingle_speaker
    show sl scared swim close with dspr
    sa "Ч-что это?"
    me "Это ответ на твой вопрос. Горн. Он обозначает, то что пора в столовую."
    show sl normal swim close with dspr
    sa "Ну пошли, тогда, что ли..."
    stop ambience fadeout 2
    stop music fadeout 2
    scene bg black with dissolve
    "..."
    
    return

label somesing_new_masha_rut:
    play music sad_piano_miku fadein 3
    "Мне почему-то стало очень жалко Машу."
    th "Она ведь не такая стерва, какой хочет казаться, на самом-то деле."
    show mi upset pioneer with dissolve
    me "Тебе помочь чем-то?"
    show mi dontlike pioneer with dspr
    ma "Посмотри тут, помощничек нашёлся!..."
    "Я продолжил смотреть ей в глаза."
    show mi shy pioneer with dspr
    ma "Д-да п-помоги..."
    me "Тогда дай я залезу на стремянку, а ты слезай и держи её."
    ma "Х-хорошо..."
    "Смущённо сказала Маша."
    hide mi with dissolve
    scene bg black with dissolve
    "..."
    scene bg ext_polyana_night with dissolve
    "Мы справились за пять минут."
    show mi shy pioneer with dissolve
    ma "С-спасибо тебе. Уж н-не знаю сколько ещё бы времени, без тебя тут бы в-возилась."
    me "Пустяки."
    "Невозмутимо сказал я."
    "..."
    me "Хотел, всё тебя спросить."
    show mi normal pioneer with dspr
    ma "Спрашивай."
    me "Почему ты притворяешься стервой?"
    show mi surprise pioneer with dissolve
    show mi angry pioneer with dissolve
    show mi sad pioneer with dissolve
    ma "Я рада, что ты заметил, но это долгая история, если хочешь, можем после съёмок пойти на пляж, там и расскажу."
    th "Похоже, намечается откровенье..."
    me "После съёмок говоришь?"
    ma "Если устанешь, можешь не приходить, я всё понимаю... "
    me "Я приду."
    show mi happy pioneer with dspr
    ma "Спасибо..."
    "Тихо сказала Маша."
    mt "Всё готово!{w} Все по местам!"
    show mi smile pioneer with dspr
    ma "Ладно, тебе пора. И я пойду."
    hide mi with dissolve
    me "Да, пора.{w} До встречи!"
    "Крикнул я Маше вслед."
    th "Мда уж... Мне сейчас девушка, возможно даже настоящая, откровение будет делать, а я сейчас иду за другой подсматривать..."
    th "Неудобно выходит...{w} Хотя чего это я сопли развёл, с какого момента меня подобные вещи беспокоят?"
    th "..."
    th "Видать, раз беспокоят и впрямь старею..."
    stop music fadeout 3
    "..."
    mt "Камера!{w} Мотор!"
    scene cg sl_swimming_dal with dissolve
    stop ambience
    play music music_list["forest_maiden"]
    "Саша разделась и вышла в озеро."
    th "Завораживающе...{w} Как будто в первый раз смотрю..."
    th "Ладно, мой выход."
    scene cg sl_swimming_bliz with dissolve
    "Я тихонечко пошел в сторону озера и засел в кусты."
    th "Хах, отсюда видок, ещё лучше. Вечность бы так провел."
    th "Надо бы быть по аккуратнее со словами, а то помню в первый цикл, хотел остаться тут навечно."
    "Спустя секунд 20 я зашелестел кустами, по сценарию."
    sa "Кто тут?"
    "Саша быстро накинула на себя рубашку и упорхнула  в сторону леса."
    stop music fadeout 3
    play ambience ambience_forest_night
    scene bg ext_polyana_night with dissolve
    mt "Стоп!{w} Снято!"
    show mt grin pioneer with dissolve
    mt "Вот всегда бы так! С первого дубля! Тогда бы, может, успели бы за эти 3 недели всё отснять!"
    me "Всё? Я пойду отдыхать."
    show mt smile pioneer with dspr
    mt "Иди."
    hide mt with dissolve
    scene bg black with dissolve
    "..."
    scene bg ext_square_night with dissolve
    play music piano_song_miku_1 fadein 3 
    play ambience ambience_camp_center_night
    "Я вышел к площади.{w} Там я встретил Машу."
    show mi smile pioneer with dissolve
    ma "Пошли?"
    me "Пошли.{w} Только вот куда пойдём?"
    show mi grin pioneer with dissolve
    ma "На пляж."
    me "Ну, пошли, что ли."
    scene bg black with dissolve
    "..."
    scene bg ext_beach_night with dissolve
    play ambience ambience_lake_shore_night
    "Вскоре мы вышли на пляж."
    show mi smile pioneer with dissolve 
    ma "Какая луна красивая!"
    hide mi with dissolve
    "Маша разделась и побежала в реку."
    "Не знаю, чего я ожидал, потому что под пионерской формой у неё был купальник."
    "Я завороженно наблюдал, как она резвилась в воде, и брызгалась, не то ли в меня, не то ли в воздух, не то ли ещё в кого."
    stop music fadeout 2
    "..."
    "Спустя некоторое время, Маша подошла ко мне и села рядом."
    show mi happy swim with dissolve
    ma "Зря ты не пошел, вода тёплая-тёплая!"
    me "Может, и так..."
    "Мы некоторое время сидели возле друг друга и молчали."
    me "Маша, так ты расскажешь?"
    show mi sad swim with dissolve
    ma "Ладно... расскажу сейчас..."
    play music so_cold fadein 3
    ma "Слушай."
    ma "Раньше, в школе, в классе, наверное восьмом-девятом, я вела себя так, почти как Саша, эдакая, аниме-дурочка.{w} Хотя нет, до такой стадии как Саша, я не деградировала тогда, пожалуй, но со мной было невозможно общаться."
    ma "Я тогда была жизнерадостной девочкой, прямо как Мику из твоего сценария."
    ma "В то время, я как раз начала краситься в циановый. И из-за такого, моего характера и внешности, ко мне сразу относились предвзято, типа \"Чё, пацаны, аниме? Гляньте, аниме идёт, посмотрите на неё!\"."
    ma "Так вот, в те годы, там гормоны шалят, времена первой любви, все дела... и меня это не обошло стороной.{w} Повстречала я одного мальчика, его звали Олег. Мы встречались с ним около года, он был в школе, как оно часто бывает \"Крутой и важной шишкой\"."
    ma "Меня в тот момент, начали наконец-то воспринимать в серьёз.{w} И даже не побоюсь этого слова, авторитет имела. Всегда считали за дурочку, а тут..."
    ma "Ну, собственно, в конце-концов, он меня бросил, сказав, что, я дура несерьёзная, ветряная, глупая, и со мной просто не возможно находиться рядом.{w} И ладно бы на этом всё закончилось... Конечно по классике жанра начали издеваться."
    ma "Девочка-даун, дурочка простоголовая, и прочие оскорбления меня довели, и я сменила школу, город, и имидж."
    ma "Убрала хвостики, заменив их на строгий пучок, начала одеваться в классическом строгом стиле одежды, и, наконец я стала чёрствой, неприступной, и не давала себя в обиду."
    ma "Но, всё равно я не могла постоянно скрывать свои эмоции, а выход нашла в актёрском мастерстве, так и завертелось."
    show mi dontlike swim with dspr
    ma "А тут, теперь я снова должна отыгрывать старую себя. Ну, и как тут, не стервить и не ворчать?"
    ma "И я же тебя просила отдать эту роль Саше! А ты всё равно настоял на своём!"
    return
    
label somesing_new_dvache_rut:
    play music shape_of_my_heart fadein 5
    th "Ага, делать мне нечего, как же." 
    "Я достал сигарету и закурил."
    play sound zazheg_sigaru
    $ renpy.pause(9)
    th "Вот так, намного лучше."
    th "Делать мне нечего, помогать кому-то, когда можно отдыхать."
    "..."
    play sound kurit
    th "И всё-таки, почему я, интересно, попал в {b}этот{/b} \"Совёнок\"?"
    th "Может, местный Демиург сжалился надо мной и выдал хоть какое-то разнообразие?"
    th "Или, быть может, это предвестие о том, что моему времяпровождении, здесь, скоро придёт конец?"
    "..."
    play sound kurit
    th "Опять же,{w} риторические вопросы."
    th "Тем не менее, буду надеяться на последний вариант."
    mt "Всё готово!{w} Все по местам!"
    th "О, а вот и мой выход.{w} Надо же, как-то быстро..."
    "..."
    mt "Камера!{w} Мотор!"
    scene cg sl_swimming_dal with dissolve
    stop ambience fadeout 1
    stop music fadeout 1
    play music music_list["forest_maiden"]
    "Саша разделась и вышла в озеро."
    th "Завораживающе...{w} Как будто в первый раз смотрю..."
    th "Ладно, мой выход."
    scene cg sl_swimming_bliz with dissolve
    "Я тихонечко пошел в сторону озера и засел в кусты."
    th "Хах, отсюда видок, ещё лучше. Вечность бы так провел."
    th "Надо бы быть по аккуратнее со словами, а то помню в первый цикл, хотел остаться тут навечно."
    "Спустя секунд 20 я зашелестел кустами, по сценарию."
    sa "Кто тут?"
    "Саша быстро накинула на себя рубашку и упорхнула  в сторону леса."
    stop music fadeout 3
    play ambience ambience_forest_night
    scene bg ext_polyana_night with dissolve
    mt "Стоп!{w} Снято!"
    show mt grin pioneer with dissolve
    mt "Вот всегда бы так! С первого дубля! Тогда бы, может, успели бы за эти 2 недели всё отснять!"
    me "Я думаю, что успеем, а если и нет, то ничего страшного не произойдёт."
    show mt angry pioneer with dspr
    mt "Как это, ничего страшного? А как тогда вы собрались сессию закрывать? А диплом получать?"
    me "Ладно-ладно... Я могу уже идти?"
    show mt normal pioneer with dspr
    mt "Иди уж..."
    hide mt with dissolve
    stop ambience fadeout 3
    scene bg black with dissolve 
    "..."
    scene bg ext_house_of_dv_night with dissolve
    play ambience ambience_camp_center_night
    "Возле домика Алисы я остановился, услышав весьма интересное предложение."
    show dv grin pioneer2 with dissolve
    $ save_name = ('День 2. За наш фильм! За любовь!.')
    dv "Эй Сеня!{w} Не хочешь зайти ко мне? Культурно отдохнуть и бухнуть, так сказать."
    th "Весьма заманчивое предложение..."
    me "Ну можно, почему бы и нет?"
    show dv laugh pioneer2 with dissolve
    dv "Давай-давай, залетай ко мне."
    me "А кто-то ещё будет, кстати?"
    show dv grin pioneer2 with dissolve
    dv "Шурик."
    th "Охохо... Интересная компания.{w} Ну, в принципе, как говориться, попробовать в жизни надо всё, а в моём случае, этого всего, не так уж и много."
    hide dv with dissolve
    me "Ну пошли, что ли."
    "Сказал я Алисе, которая уже почти зашла в домик."
    stop ambience fadeout 1
    play ambience ambience_int_cabin_night
    play sound sfx_open_door_1
    scene bg int_house_of_dv_night_black with dissolve
    "Я остановился на пороге..."
    play sound vkl
    scene bg int_house_of_dv_night_light with dspr
    $ persistent.sprite_time = "day"
    "И огляделся."
    th "Уютненько тут."
    show dv smile pioneer2 at cright with dissolve
    dv "Проходи, не стесняйся!"
    play music dlya_alco fadeout 2
    play sound sfx_open_door_1
    show sh normal pioneer at cleft with dissolve
    dv "О! А вот и Шурик!"
    sh "Здорова!"
    me "Здоров! А что, собственно говоря пить будем?"
    show dv grin pioneer2 at cright with dissolve
    dv "Будем пить реквизит."
    th "Ахах, а Маша мне говорила, что я, точнее мой двойник до меня, промышлял чем-то таким, вот уж не думал, что удастся поучаствовать в чём-то подобном!"
    sh "И ещё кое-что есть: пару бутылок вина, одна бутылка виски, ну и сама водка  - 2 бутылки."
    me "Ясно."
    me "Ну, народ, давай-те же начнём!"
    "Шурик и Алиса синхронно вскрикнули \"Да!\" и принялись доставать Алисины запасы."
    scene bg black with dissolve
    "..."
    scene bg int_house_of_dv_night_light with dissolve
    show sh smile pioneer at cleft with dissolve
    sh "Так... ну давайте выпьем за наш фильм!"
    show dv grin pioneer2 at cright with dissolve
    dv "За наш фильм!"
    me "За наш фильм!"
    "..."
    "Мы синхронно опрокинули рюмки с водкой."
    me "Ууух. Ядрёная."
    sh "А то! Это же советское качество!"
    dv "Ну между первой и второй..."
    me "Перерывчик небольшой!"
    sh "Ну тогда выпьем за наше с вами счастье!"
    "Мы с Алисой одновременно воскликнули \"Да!\", и всей компанией опрокинули вторую рюмку с водкой."
    scene bg black with dissolve
    stop music fadeout 2
    "..."
    "..."
    "Спустя полтора часа."
    scene bg int_house_of_dv_night_light with dissolve
    play music never_gonna_give_you_up fadein 3
    show dv normal pioneer2 at cleft with dissolve
    dv "Ты м-меня... ик... Увва-важаешь?"
    show sh laugh pioneer2 at cright with dissolve
    sh "Конечно, яч т-тебя юл... л-люблю."
    show dv grin pioneer2 at cleft with dspr
    dv "Как че-человека и-или как дев... вушку?"
    sh "Дуррра! Как человека!"
    show dv normal pioneer2 at cleft with dspr
    dv "Аааа...{w} Ну за это можно вы... ик... выпить!"
    sh "На-ли-вай!"
    "Алиса налила себе и Шурику по рюмке из последней, почти закончившейся бутылки водки и опрокинули её залпом."
    show dv angry pioneer2 at cleft with dspr
    dv "Тааак... подожди. Ты м-мен-ня д-дурой назвал?!"
    show sh upset pioneer2 at cright with dspr
    sh "Да ты...{w} Да не ты, да...{w} то я...{w} да не ты.{w} Я c-случайно л-ляпнул..."
    show dv smile pioneer2 at cleft with dspr
    dv "Н-ну, ладно, ответ за... засчитан."
    dv "А ко... кого любишь как дев... ик... девушку?"
    show sh smile pioneer2 at cright with dspr
    sh "Машку лю... люблю..."
    show dv laugh pioneer2 at cleft with dspr
    dv "Ахахах, Машку?{w} Ну ты даёшь!"
    show sh normal pioneer2 at cright with dspr
    me "Ну, ладно, товарищи алкаши, давайте выпьем за это, и будем сворачиваться."
    "Все выкрикнули тост \"Ну, за любовь!\" и выпили."
    show dv smile pioneer2 at cleft with dspr
    dv "Ну, расскажу вам историю!"
    show dv shocked pioneer2 at cleft with dspr
    dv "Короче, мне нед-давно сон приснился... Там Ленка, короче нас всех пере... перерезала."
    show dv laugh pioneer2 at cleft with dspr
    dv "Вот умора! Правда?"
    show sh serious pioneer2 at cright with dspr
    sh "М-минуточку!{w} Будте добры, пом-медленее...{w} Я зпысываю."
    "Шурик не понятно откуда взял ручку и начал записывать слова Алисы на столе."
    me "Так, Шурик, ты совсем напился. Иди уже домой, наверное."
    show sh normal pioneer2 at cright with dspr
    sh "Л-лады."
    hide sh with dissolve
    "Шурик встал и сразу же плюхнулся на соседнюю кровать."
    stop music fadeout 2
    me "И что нам с ним делать?"
    show dv grin pioneer2 close with dissolve
    dv "Да за... забей т-ты на н-него."
    me "Ладно, и что нам теперь делать?"
    dv "Есть у меня одна идейка..."
    "Игриво сказала Алиса."
    me "Ну?"
    "Алиса начала расстёгивать рубашку."
    me "Ну, раз ты сама предлагаешь, то грех отказываться."
    stop ambience fadeout 3
    "Я сразу же набросился на неё, сразу же сорвал лифчик и юбку и повалил на кровать."
    scene cg d1_dv_hentai_2 with dissolve
    play sound ston1
    play music still_loving_you_alice fadein 1
    dv "Эй!{w} Не так резко!"
    me "Как скажешь..."
    "Я быстренько скинул свою рубашку."
    "И начал мять Алисину грудь."
    "Алиса немного постанывала и повторяла."
    dv "Дав-вай... мни, ах... хорошо..."
    "Через ещё несколько минут гулянию моих рук по её телу, она дала добро."
    scene cg d1_dv_hentai_1 with dissolve
    play sound ston2 
    "В ту минуту мы полностью отдались страсти."
    "Это было приятное ощущение." 
    th "Давненько не испытывал чего-то подобного."
    dv "П-пожалуйста... б-б-быстрее..."
    "Ну, а я, собственно, послушал её и ускорил темп."
    scene bg black with dissolve
    stop music fadeout 2
    "Через минут 20 мы оба свалились и уснули."
    window hide
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    scene bg black
    with fade3
    $ backdrop = "night"
    $ new_chapter(2, "День 2. Ночь.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "night"
    $ night_time()    
    $ persistent.sprite_time = "night"
    $ renpy.pause(1, hard=True)
    jump somesing_new_dvache_rut_night

label somesing_new_dvache_rut_night:
    play ambience ambience_int_cabin_night
    scene bg int_house_of_dv_night_black
    show unblink
    window show
    $ save_name = ('День 2. После пьянки.')
    "Я проснулся посреди ночи."
    "Желания продолжать спать, почему-то особо не было."
    "Я посмотрел на часы и увидел что сейчас 3 часа ночи."
    th "И откуда тогда у меня такая бодрость?.."
    th "Я же всего-то около 2 часов поспал."
    th "Странно."
    "..."
    th "Может пойти прогуляться? Обычно, когда я не могу заснуть, всегда выхожу прогуляться, нагнать на себя сон, так сказать... Но сейчас... когда рядом со мной Алиса... "
    menu:
        "Пойти погулять":
            $ bd_ochki += 2
            $ dv_2_ochki -= 2
        "Остаться с Алисой":
            $ dv_2_ochki += 2  
            $ bd_ochki -= 2

    if dv_2_ochki >= 2:
        jump somesing_new_dvache_rut_day2
    else:
        jump somesing_new_blood_night
    
    
    
    
    
label somesing_new_blood_night:
    $ save_name = ('День 2. Убиваша.')
    th "Ладно, я думаю, что всё равно она так рано не то, что не проснётся сама, её выстрелом из артиллерии не разбудить."
    th "Так что, думаю, можно пройтись недолго по улице."
    stop ambience fadeout 3
    "Я оделся и вышел на улицу."
    play sound sfx_open_door_2
    play ambience ambience_camp_center_night fadein 1
    scene bg ext_house_of_dv_night with dissolve
    "Я глубоко вдохнул свежий воздух."
    th "Ммм... хорошо... Даже похмелья не чувствую, хотя выпил я довольно много."
    th "Наверное, за предыдущие циклы привык."
    "Я направился вниз по улице."
    stop ambience fadeout 1
    scene bg black with dissolve
    "..."
    play ambience ambience_forest_night fadein 2
    scene bg ext_path_night with dissolve
    "Я и не заметил, как вышел на тропу в старый лагерь."
    th "Ну, ещё немного по лесу пройдусь, и обратно."
    "..."
    "Прошёлся ещё не много и услышал..."
    stop ambience fadeout 2
    play sound krik_wom 
    th "..."
    play music remix fadein 2
    th "Крик.{w} В лесу?{w} Ночью?"
    th "Не думаю что это к добру..."
    scene bg ext_path_night:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "Я сию же секунду, рванул с места."
    th "Что-то мне подсказывает, что этот крик точно не может быть от вида какой-нибудь совы."
    th "Та кто его издала, закричала с таким ужасом, будто смерть воплоти увидела."
    scene bg ext_path2_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    th "А если это так, будет жалко пропустить представление."
    th "Хотя стоп...{w} Представление?{w} Я же в лагере киносъёмок, может, снимают что?"
    th "..."
    th "Нет.{w} Слишком уж правдоподобный и громкий."
    th "Уж точно не просто съёмки какой-то сцены."
    th "Слишком поздно, да и Шурик у нас спит, а без оператора никак."
    th "В любом случае, добежим, а там посмотрим."
    "Я уже почти выдохся, но продолжал бежать."
    "Всё таки интерес брал верх над выносливостью."
    scene bg ext_polyana_night with dissolve
    stop music fadeout 2
    "Я наконец-то добежал до поляны, где увидел два силуэта и сразу же бесшумно нырнул в кусты."
    play music tel_aviv fadein 2
    scene cg ubivayut_slavyu with dissolve
    "Присмотревшись, я увидел Славю, то есть Сашу, которая стояла на коленях и плакала от ужаса. И тёмный, девичий силуэт с тесаком за спиной."
    "Выходит, насчёт того, что Саша увидела смерть во плоти, я оказался прав."
    "Силуэт медленно подошёл к Саше, и также медленно прошлась тесаком по её щеке."
    sl "Л-лена, н-не н-н-надо...{w} п-пожалуйс-т-та..."
    "Лена провела пальцами по её новоиспечённому порезу и облизала их."
    un "Твоя кровь на вкус сладкая как сахар."
    un "Славя, ты молодец, уже не кричишь, но ты много плачешь. Раздражает. Кончай."
    "Раздражённо и с насмешкой произнесла Лена."
    th "Славя?{w} Ничего не понимаю... Всё таки съёмки? Но камеры же нету.{w} Да и не будут калечить актрису для одной сцены."
    th "Я снова в обычном лагере? Ну, хотя, не таком уж и обычном...{w} Но как?{w} Цикл перезапустился?{w} Почему?"
    "Лена поднесла свое лицо к Славиному и принюхалась."
    un "А вот, твое тело пахнет почти тёплым мясом."
    sl "Нет...{w} это всё сон... это просто кошмар...{w} это всё не правда... это всё не по настоящему..."
    un "Не права ты, Славяна, мы находимся сейчас на самом, что ни на есть, настоящем яву.{w} Хотя, твоя теория насчёт кошмара мне нравиться. Можешь считать, что я твой личный кошмар."
    sl "..."
    un "Ну что, начнём веселье? Не отвечай, конечно начнём."
    un "Я вырву твое сердце целиком и сразу, чтобы оно точно уже никому не досталось. Кроме меня."
    "Последнюю фразу Лена сказала с дьявольской улыбкой."
    un "Но перед этим..." 
    un "Сначала вырву твои поганые ручки, а потом ножки..."
    sl "З-за ч-что?.."
    "Едва смогла выдавить из себя Славя, тихо плача."
    un "За всё хорошее Славя, за всё хорошее.{w} Ну и за плохое заодно."
    "Я понял, что если сейчас не вмешаться в представление, то Славя, в скором времени, станет лишь кусочками мяса."
    "Я выпрыгнул из кустов."
    scene bg ext_polyana_night
    show sl scared pioneer far at fleft
    show un evilsmile3 pioneer at cleft
    with dissolve
    me "Ми-ну-точ-ку.{w} Я конечно извиняюсь, что прерываю, но всё же..." 
    with vpunch
    me "Что у вас тут, сука, происходит!?"
    show sl cry pioneer far at left with dspr
    sl "С-с-семён...{w} ПОМОГИ МНЕ ПОЖАЛУЙСТА!!!"
    stop music fadeout 4
    "Славя крикнула это с надеждой на спасение, и глазами давала понять, что она будет вселенски мне благодарна, если её спасут."
    show un evilsmile3 pioneer at cleft with dspr
    un "Привет, Сёмчик.{w} А я тут Славю убиваю. Не хочешь посмотреть?"
    menu:
        "Спасти Славю":
                                $ sl_ochki += 2
                                $ ubiv_ochki -= 2
        "Попросить убить Славю":
            $ ubiv_ochki += 2  
            $ sl_ochki -= 2

    if ubiv_ochki >= 2:
        jump somesing_new_ubivasha_rut
    else:
        jump somesing_new_slavya_rut
    
label somesing_new_slavya_rut:
    $ save_name = ('День 2. Бежим!')
    play music hell fadein 5
    "Я сначала растерялся, но через пару секунд, взявши за руку Славю, побежал."
    hide un with dissolve
    scene bg ext_path2_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    play sound sfx_ed_laugh_1
    "Лена расхохоталась.{w} По дьявольски."
    un "Ну куда же ты, Семёёёён..."
    me "Господи,{w} ДА ЧТО, БЛЯТЬ, ТУТ ПРОИСХОДИТ!?"
    "Мы бежали в первую попавшуюся сторону, поэтому я не знал куда мы бежим и добежим ли."
    "Славе нужно было прилагать огромные силы, чтобы бежать не отставая, но она бежала."
    un "Всё равно далеко не убежите!"
    me "Знаю!"
    th "Оптимистичный прогноз..."
    un "Ну тогда..."
    play sound sfx_ed_laugh_2
    un "Давайте поиграем в догонялки!"
    "..."
    me "Славя, что тут произошло?"
    sl "..."
    me "..."
    sl "..."
    me "Ясно."
    th "Надо бы придумать план как оторваться от неё, а то так и правда можно бегать вечно."
    th "В кусты сигануть? Нет, опасно, можно упасть из-за Слави.{w} Тогда что? Славю бросать не вариант."
    th "..."
    th "Придумал!{w} Риск, конечно, большой, но времени придумать что-то ещё нет."
    scene bg ext_path2_night with dissolve
    "Я отпустил руку Слави, резко остановился..."
    show un shadow knife with dissolve
    play sound sfx_lena_hits_alisa
    hide un with dspr
    "И почти вслепую ударил ногой с разворота в Лену. Она упала."
    scene bg ext_path2_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "И сразу же побежал за Славей."
    th "План сработал!"
    "Я быстро нагнал Славю и мы побежали вместе."
    "..."
    scene bg ext_path2_night with dissolve
    "Спустя минут 10 мы окончательно оторвались и остановились."
    stop music fadeout 3
    play ambience ambience_forest_night fadein 3
    me "Хух... Вроде... оторвались..."
    show sl scared pioneer with dissolve
    sl "Д-да..."
    "Я решил осмотреться куда мы прибежали."
    stop ambience fadeout 1
    scene bg ext_old_building_night with dissolve
    play ambience ambience_old_camp_outside fadein 2
    "Мы были прямо возле старого корпуса."
    me "Зайдём? А то не думаю, что оставаться тут, хорошая идея."
    sl "Д-да..."
    scene bg int_old_building_night with dissolve
    "Мы зашли внутрь."
    me "Сейчас."
    play sound sfx_open_metal_hatch
    "Я открыл люк в бункер."
    show sl scared pioneer with dissolve
    me "Залезай."
    hide sl with dissolve
    "Славя молча залезла."
    $ save_name = ('День 2. Ответы в бункере.')
    scene bg int_catacombs_entrance with dissolve
    play ambience ambience_catacombs fadein 2
    play sound sfx_hatch_drop
    "И я за ней."
    me "Блин, темно же.{w} У тебя нету фонарика?"
    sl "У-ур{w}-р-р-{w}ронил-ла..."
    me "Ладно, по памяти найду."
    "Славя пошла за мной."
    "..."
    scene bg int_catacombs_door with dissolve
    me "Пришли."
    
    "Я покрутил вентиль..."
    play sound sfx_open_metal_hatch
    "И открыл дверь."
    scene bg int_catacombs_living with dissolve
    "Мы вошли внутрь, присели на кровать и я начал допрос."
    play music MeetMeThere fadein 4
    show sl scared pioneer with dissolve
    me "Итак, с чего бы начать... Ты Саша или Славя?"
    sl "Ч-что?"
    me "Ты Славя?"
    sl "Н-ну, д-да."
    me "Расскажи всё с самого начала, что тут произошло."
    sl "..."
    "Славя до сих пор находилась в шоковом состоянии и не верила, что всё происходящие наяву."
    "Она не реагировала."
    "Я дал ей сильную пощёчину. И она, вроде как, зашевелилась."
    play sound sfx_face_slap
    show sl surprise pioneer with dspr
    sl "А?"
    me "Очнись уже!"
    "..."
    "Славя ещё немного времени приходила в себя, а потом кинулась на меня и зарыдала."
    show sl cry pioneer close with dspr
    play sound soul_cry
    sl "Семён..."
    "Она порыдала мне в плечо ещё пару минут, после чего отстранилась от меня и начала свой рассказ."
    show sl cry pioneer with dspr
    sl "Я шла ночью домой с озера, ходила купаться, и вдруг встретила Лену."
    sl "Я хотела было начать её допрашивать, что тут она делает после отбоя, но она внезапно попросила меня помочь."
    sl "А я ведь трудолюбивая, безотказная, всегда всем помогаю, поэтому сразу согласилась."
    sl "Она повела меня в лес... но я не придала этому значения."
    sl "Потом, когда мы прошли половину пути, я поняла, что мы идём в старый лагерь."
    sl "Я возразила ей, мол, за территорию выходить нельзя, но..."
    play sound soul_cry
    sl "Но она ударила меня чем-то тяжёлым и начала рассказывать мне к-как он-на... к-к-как он-на..."
    play sound soul_cry
    sl "Б-буд-дет меня..."
    me "Мучительно убивать."
    "Закончил её фразу я."
    play sound soul_cry
    sl "Д-да..."
    me "Дальше не продолжай я всё видел."
    "Славя кивнула."
    me "Ничего странного в последнее время в Лене не замечала?"
    sl "До этого момента н-нет..."
    show sl scared pioneer with dspr
    sl "Лена!{w} А если она сейчас нас найдёт?.."
    me "Не боись, без битвы тебя не сдам."
    show sl tender pioneer with dspr
    "Славя успокоилась."
    sl "Семён, я ведь тебе теперь жизнью обязана..."
    me "Да забей, будем считать, что своей информацией ты закрываешь эти обязанности."
    stop music fadeout 3
    sl "..."
    me "А с лагерем ничего в последнее время не замечала?"
    show sl sad pioneer with dspr
    sl "Да, замечала."
    me "Расскажи поподробнее."
    play music music_list["into_the_unknown"] fadein 3
    sl "Я начала замечать, казалось бы, мелкие, незначительные детали, то, это, но если сложить их вместе, то выходит довольно странно."
    me "В смысле?"
    sl "Ну, например, полнолуние: как я приехала в лагерь, оно было, и каждый день вплоть до сегодня продолжается.{w} Это, конечно, красиво и величественно, но как-то неправдоподобно."
    th "Неужели она сама догадается, что она ненастоящая?"
    me "Тааак..."
    sl "И ещё кое-что связанное с луной, косвенно, конечно, но..."
    me "Что?"
    show sl shy pioneer with dspr
    sl "Я про {i}эти{/i} дни."
    me "Аааа...{w} Так что с ними? "
    show sl sad pioneer with dspr
    sl "Они... не наступают."
    sl "Это может быть, конечно, связано с переменной климата, волнениями на новом месте, но... я в это уже мало верю."
    sl "Мои вещи. В них ничего нету на данный случай. И вообще, много чего нет, чего я забыть не могла, их как будто не я собирала."
    sl "Это совсем странно, если остальное ещё можно как-то объяснить, то это..."
    me "Ясно. И как ты думаешь с чем это связано?"
    sl "Не знаю, я как раз хотела с тобой этим поделиться, завтра, в смысле сегодня, и подумать вместе."
    sl "Я из-за всего этого начала думать, что со мной что-то не так. Но после сегдняшнего..."
    sl "У меня такое ощущение, что что-то не так не только со мной, а и совсем миром."
    th "Неужели я наконец-то не буду один в этом мире!?"
    me "А когда ты начала замечать все эти несостыковки?"
    show sl surprise pioneer with dspr
    sl "Когда? Хм, наверное, как ты приехал..."
    "Славя недоверчиво взглянула в мою сторону."
    show sl angry pioneer with dspr
    sl "Ты как-то со всем этим связан?"
    me "Я?"
    show sl sad pioneer with dspr
    "Славя приняла виноватый вид из-за того, что не думая, обвинила своего спасителя."
    sl "Извини... Может это Лена во всем винов..."
    stop music
    me "Да я связан."
    show sl surprise pioneer with dspr
    sl "Что?"
    play music sdl_tpinf_whitecoma fadein 4
    me "Да я связан."
    show sl scared pioneer far with dspr
    "Славя сразу вскочила и отошла от кровати."
    th "Ну, не мудрено, особенно учитывая, что я делал с ней в прошлых циклах..."
    me "Нет, я не говорил, что я всё это тут устроил, просто ты метко подметила, что именно связан со всем происходящим, а не виноват."
    sl "..."
    me "Так, как бы начать."
    me "Ну, начну с главного... Я не из этого мира."
    show sl surprise pioneer far with dspr
    sl "Как?"
    me "Как-как... из будущего!"
    sl "Допустим, я уже даже удивляться не буду... И как это связанно с происходящим?"
    me "Как ты думаешь, сколько уже я в этом лагере?"
    sl "Ну, четыре дня..."
    me "А я тут уже около 300 недель."
    show sl angry pioneer far with dspr
    sl "Что?{w} Нет, если в предыдущее ещё можно поверить, то в это я точно не поверю. Я же собственными глазами видела как ты выходил из автобуса!"
    me "Ну конечно же ты не веришь..."
    th "Пустые надежды..."
    me "Я попал в недельный цикл, знаешь, как в \"Дне сурка\", только не день, а неделя. И этих циклов я прошёл уже 320-350, точно не помню, сбился со счёта."
    "Я начал срываться."
    me "И в эту неделю происходит одно и тоже! Чтобы я не делал, я снова просыпаюсь в этом грёбаном автобусе! Чтобы я не делал, вы все ничего не помните и мне не верите, называете сумасшедшим! И всё время делаете одно и тоже! Вы как куклы, вы даже своего города не можете назвать!"
    show sl scared pioneer far with dspr
    me "Да что там! Вы даже не можете сказать в какой мы республике! Где мы?! На Кубани?! В России?! В Украине?!"
    with vpunch 
    with hpunch
    me "ГДЕ, СУКА, НАХОДИТСЯ ЭТОТ ЛАГЕРЬ?!"
    show sl cry pioneer far with dspr
    sl "...{w} Я...{w} я н-не знаю..."
    me "..."
    me "Прости."
    show sl sad pioneer far with dspr
    sl "Но как я могу быть ненастоящей? Я же всё помню, своих родителей, своих братьев, свою школу, свой город, свою жизнь..."
    me "И как зовут твоих братьев?"
    sl "..."
    me "А родителей?"
    sl "..."
    me "А как называется твоя школа или какой у неё номер?"
    sl "Не помню..."
    me "Хорошо, тогда самый лёгкий вопрос, откуда ты?"
    sl "С севера..."
    me "Откуда именно."
    sl "С холодн..."
    with vpunch
    me "С какого города!?{w} Хотя бы с какой области!"
    sl "..."
    show sl sad pioneer with dspr
    "Славя села обратно."
    sl "Выходит...{w} я ненастоящая?.."
    me "Да."
    sl "Но как же? Я же всё чувствую, эмоции, боль, я же могу думать, я же могу любить в конце-концов!"
    me "Правда? Может у тебя ещё и планы на будущее есть?"
    sl "Ну да..."
    me "Не будет у тебя будущего, и даже не из-за Лены, ты часть этого места, ты всегда будешь здесь."
    sl "Но я же... я же хотела быть краеведом... заниматься исследованиями, делать и заметки, писать книги, много путешествовать по миру и многое изучать...  Я хотела бы жить с любящим мужем... Родить двоих детей..."
    me "Но этого всего никогда не будет."
    show sl cry pioneer with dspr
    play sound soul_cry
    sl "Я… Я не могу… Я поняла, что я на самом деле не настоящая, и что ничего этого никогда не случится. У меня нет будущего. Я…"
    "Славя расплакалась."
    sl "Я… Я не могу как-то это изменить, да?"
    th "Исторический момент! Первая кукла на моей памяти, которая осознала себя."
    me "Да."
    sl "Мне так больно, от того, что я не реальная. Я не могу ничего изменить… Я… я… я не знаю… Мне ведь не на что надеяться. Я буду всегда такой…"
    me "Ну поздравляю с пробуждением! Ты первая кукла на моей памяти, которая поняла свою ситуацию."
    sl "С-спасибо..."
    sl "И ты, наверное, обрадовался, что я уже поняла, что не настоящая?"
    me "Ну, если честно то да..."
    sl "Да ладно, я понимаю тебя... Это, наверное, было очень грустно, провести столько времени с теми, кто тебя не понимает, так что я на тебя не злая. Я тоже рада, что мне все-таки удалось чего-то достичь..."
    me "И ты не расстроена?"
    show sl sad pioneer with dspr
    sl "Расстроена, конечно, но все-таки даже если я и не настоящая и у меня нету прошлого и будущего, то все равно я думаю, что это не так уж плохо, как могло быть, я все-таки могу думать, говорить, рассуждать... Я ведь, получается, даже почти могу общаться как человек."
    me "Ну, хорошо, что хоть так. Ладно, нам всё таки надо уже что-то делать, я имею ввиду идти в лагерь или посидеть ещё тут..."
    show sl normal pioneer with dspr
    sl "Семён, я ведь сегодня не спала, и ты, полагаю тоже, может поспим?"
    me "Да, пожалуй. А то с этими пробежками я очень устал."
    show sl smile2 pioneer with dspr
    sl "Тогда, спокойной ночи!"
    "Славя легла."
    me "Спокойной ночи."
    "Я хотел встать и залезть на верхнею кровать, но меня остановила Славя."
    me "М?"
    show sl shy pioneer close with dspr
    sl "Семён...{w} Ляг со мной..."
    me "Что?"
    sl "Куклы ведь не могут любить, а если выходит, что я кукла... может я стану чуточку живее?"
    me "А ты меня любишь?"
    show sl angry pioneer close with dspr
    sl "Эээ... А не нагло так девушку в лоб спрашивать?"
    show sl sad pioneer close with dspr
    sl "Ах, да..."
    me "..."
    show sl tender pioneer close with dspr
    sl "Ты мне понравился как только приехал... Ты такой растерянный был, хотелось взять тебя под крылышко и защитить..."
    th "Это, кстати, жалость называется...{w} Ну, хорошо, что хоть не ко мне, а к тому Семёну, кто был до меня."
    show sl tender pioneer close with dspr
    sl "И сейчас, я убедилась, что люблю тебя... Ты меня спас, рискуя своей жизнью, даже не смотря на то, что я ненастоящая..."
    sl "Но к сожалению, это точно не взаимно, ты не сможешь полюбить того, у кого нет будущего, и кто тебя забудет..."
    me "Я тебя понял."
    "Я лёг к ней."
    show sl happy pioneer close with dspr
    "Славя обрадовалась, что я всё же согласился."
    show sl smile pioneer close with dspr
    sl "Спокойной ночи."
    me "Да..."
    stop music fadeout 2
    show blink 
    $ renpy.pause(3, hard=True)
    "..."
    hide blink
    scene bg int_catacombs_living 
    show unblink
    "Я проснулся и огляделся."
    th "А что я тут делаю?"
    "Потом посмотрел на спящую Славю и вспомнил."
    th "А, точно... {w} Как такое забудешь..."
    "Я разбудил Славю."
    me "Просыпайся, соня!"
    show sl normal pioneer close with dissolve
    sl "Щас, Жень."
    sl "Представляешь мне сегодня сон такой стра..."
    show sl surprise pioneer close with dspr
    sl "Эээ..."
    me "...это не сон, да."
    show sl scared pioneer close with dspr
    sl "То есть вчера меня хотела убить Лена, а потом ты спас меня и мы убежали от неё, а потом..."
    show sl sad pioneer close with dspr
    sl "Я ненастоящая..."
    me "Всё именно так."
    sl "И что нам делать?"
    me "Пойдём в лагерь."
    show sl scared pioneer close with dspr
    sl "А если мы встретим Лену?.."
    me "Не встретим, а если встретим я тебя защищу."
    show sl normal pioneer close with dspr
    sl "Убедил. Пошли."
    scene bg black with dissolve
    "..."
    scene bg int_old_building_day with dissolve
    play ambience ambience_forest_day fadein 2
    $ persistent.sprite_time = "day"
    $ save_name = ('День 2. Что делать Славе?')
    "Мы вышли из Старого корпуса и направились в сторону лагеря."
    sl "Семён..."
    me "М?"
    scene bg ext_path2_day with dissolve
    show sl sad pioneer with dissolve
    sl "Ты ведь говорил, что каждый раз происходит одно и тоже?"
    me "Ну, да."
    sl "Это получается, что меня, или моих кукол предшественников, всё время убивали?"
    me "Нет, в этот раз всё по другому."
    show sl surprise pioneer with dspr
    sl "То есть, меня не убивали?"
    th "И что мне ей ответить? Сказать прости, я тебя пару раз убил, погорячился?"
    me "Ну, наверное..."
    show sl smile pioneer with dspr
    sl "Вот и славно."
    scene bg ext_path_day with dissolve
    show sl scared pioneer with dissolve
    sl "А если Лену встретим?.."
    me "В лагере она точно тебе ничего не сделает."
    sl "Х-хорошо..."
    stop ambience fadeout 2
    scene bg ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day fadein 2
    show sl normal pioneer with dissolve
    sl "И что дальше?"
    me "Не знаю, я бы советовал тебе взять выходной, отвлечься от всего."
    sl "Наверное, так и поступлю..."
    stop ambience fadeout 3
    scene bg black with dissolve
    "Я провёл Славю до домика Ольги Дмитриевны, они о чём-то говорили и спустя минут пять Славя вышла."
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    me "Ну что?"
    show sl normal pioneer with dissolve
    sl "Дала выходной."
    me "Ну и отлично."
    sl "Так чем займёмся?"
    me "А чем ты хочешь?"
    sl "Ну покупаться хотелось бы..."
    me "Где?"
    show sl scared pioneer with dspr
    sl "Не в лесу!"
    th "Мда... а когда-то я её ещё называл лесной девой..."
    me "Ну, не в лесу, так не в лесу."
    "Я пожал плечами."
    scene bg black with dissolve
    stop ambience fadeout 2
    "Мы зашли в домик Слави за купальником и пошли на пляж."
    $ save_name = ('День 2. Пляжный волейбол.')
    scene bg ext_beach_day with dissolve
    play ambience ambience_lake_shore_day fadein 2
    "Вскоре мы пришли."
    show sl normal pioneer with dissolve
    sl "Народу немного."
    me "Вот и славно."
    show sl normal swim with dissolve
    "Славя разделась."
    show sl smile swim with dspr
    sl "О! Смотри там Ульянка, Шурик и Мику в волейбол играют!{w} Давай к ним!"
    th "Хм, не помню такого раньше, видимо, тут даже мелкие события другие."
    me "Да, пойдём."
    hide sl with dissolve
    show sh smile swim close at cright with dissolve
    show us smile swim close at fright with dissolve
    me "Здоров!"
    show sl smile swim at fleft with dissolve
    sl "А можно с вами?"
    us "Нужно!"
    sh "Да-да, конечно."
    me "Шур, неужели ты в кои-то веке решил из своего логова вылезти?"
    sh "Да там... понимаешь... {w} Деталей для робота нет, а всю работу, что можно было сделать с нашим инвентарём уже я сделал."
    sh "Решил пойти отдохнуть в домике, меня по пути перехватила Ульянка и предложила сыграть в волейбол."
    me "И ты что, взял и согласился?"
    show sh normal_smile swim close at cright with dspr
    sh "В обмен на обещание не приближаться к нашему клубу, ближе чем на сто метров."
    me "Ясно. Ну, давайте начнём."
    scene bg ext_beach_day with dissolve
    "Мы поделились."
    "В моей команде: Я, Славя и ещё две девочки из другого отряда."
    "А в команде соперников: Ульяна, Шурик, Мику и ещё один мальчик из среднего отряда."
    play music voleyball fadein 3
    stop ambience fadeout 3
    scene cg volelbol_us_sh with dissolve
    "Мы решили сразу же играть во всю силу."
    "Первая игра далась нам тяжко."
    "Ульянка с Мику всё время разыгрывали в пас, а затем один из них добивал мяч мощным ударом под сетку."
    "И мы ничего не могли с этим поделать."
    "Счёт был 9:4 не в нашу пользу."
    "Но Славя предложила хорошую тактику против них."
    "Предложила она, после первого паса, мне и ей, независимо от того на какой позиции находились, подбегать к центру и готовиться к блоку."
    "И это работало!{w} Мы даже на какое-то время вырвались вперёд. Счёт уже был 12:13, в нашу пользу."
    "Но тут команда Ульяны рассекретила нашу тактику, и стала бить с дальних позиций."
    "Счёт 17:19."
    "Мы всё ещё вели, но нужен был какой-то план."
    "У Слави хорошо получалось принимать все подачи, и я поставил её в центр навсегда, а сами мы с девочками встали по краям и пасовали друг другу на удар."
    "У нас, мягко говоря, получалось - не очень."
    "Сказывалась общая не сыгранность."
    "В итоге первую партию мы продули, со счётом 25:21."
    scene bg black with dspr
    "Мы поменялись сторонами."
    scene cg volelbol_us_sh with dspr
    "Наша команда была не в духе, однако Славя смогла всех подбодрить, и подняла этот самый дух команды."
    "В этой партии мы начали весьма неплохо."
    "В первой половине игры счёт уже был 14:6, в нашу пользу."
    "Девочки из другого отряда начали быстрее и точнее принимать подачи, Славя отдавать отличные пасы, ну а я неплохо добивал их и в конечном итоге мы выиграли эту игру со счётом 25:16."
    scene bg black with dspr
    "Ульянка расстроилась, однако Мику её развеселила сказав, что она \"Не струны на гитаре, чтобы расстраиваться.\"."
    scene cg volelbol_us_sh with dspr
    "В третьей партии была ещё более ожесточённая борьба.{w} Каждый мяч находился в игре порядка нескольких минут."
    "Атака за атакой, защита за защитой, и спустя примерно час, счёт был 17:20 не в нашу пользу."
    "Взяв небольшой перерыв, я указал команде на общие ошибки и подбодрил их не сдаваться."
    "Спустя ещё примерно минут 40 игры, Славя забила последний мяч и мы таки вырвали победу со счётом 29:27."
    scene bg ext_beach_sunset with dissolve
    play ambience ambience_lake_shore_evening fadeout 2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    "Славя чуть ли не прыгала от радости, как малое дитя."
    show sl happy swim close at fright with dissolve
    sl "Да-а-а! Мы лучшие!"
    stop music fadeout 5
    show us angry swim at cleft with dissolve
    us "Не зазнавайся ты! Просто повезло!"
    "Пока мы праздновали победу, Шурик молча ушёл."
    hide sl
    hide us
    with dissolve
    th "Ну и бог с ним."
    th "Да, давно мне не было весело от простых вещей...{w} Кто ж знал, что волейбол мне по душе."
    "Небо уже оранжевело. Долго мы тут играли..."
    "Мику пригласила нас на подстилку поесть арбуз."
    show mi smile swim far at cleft with dissolve
    $ save_name = ('День 2. Музыкальный вечер.')
    mi "Семён, Славя идите к нам арбуз есть!"
    "Особо не раздумывая,я согласился."
    show mi smile swim close at fleft with dissolve
    show sl normal swim close with dissolve
    show us smile swim close at fright with dissolve
    "Мику дала нам cо Славей и с Ульянкой по скибке арбуза."
    th "Никогда его тут не ел."
    show sl smile swim close with dspr
    sl "Вкусно! Мику откуда он у тебя?"
    show mi grin swim close at fleft with dspr
    mi "Места надо знать! Хи-хи."
    us "Знаю я эти твои места!"
    show mi surprise swim close at fleft with dspr
    mi "Откуда?"
    "Вскрикнула Мику."
    show us grin swim close at fright with dspr
    us "Источники надо знать!"
    "Передразнила Ульяна."
    show mi dontlike swim close at fleft with dspr
    mi "Бака!"
    "Все молча уплетали свою долю арбуза."
    "Но вдруг..."
    hide us with dissolve
    "Ульяна встала и побежала куда-то ничего не сказав."
    me "Чего это она?"
    show mi sad swim close at fleft with dspr
    mi "Видимо я её обидела..."
    me "Не думаю... {w} Да что ж сегодня все по-английски уходят? То Шурик, то Ульяна..."
    "..."
    "Мы все доели. Настало напряжённое молчание."
    "Заняться было особо нечем, но мне вдруг пришла идея."
    th "Сыграю-ка на гитаре!"
    me "Мику, можно тебя на секундочку?"
    show mi surprise swim close at fleft with dspr
    mi "Что?" 
    show mi smile swim close at fleft with dspr
    mi "А, да-да, конечно."
    hide sl with dissolve
    hide mi with dissolve
    "Мы встали и чуть-чуть отошли. Славя до жути боялась оставаться одной, вся подрагивала..."
    show mi normal swim at cright with dissolve
    mi "Так что ты хотел сказать?"
    me "Хотел предложить поиграть на гитаре, а то сидим и ничего не делаем, как-то не весело."
    show mi smile swim with dspr
    mi "Конечно-конечно! Отличная идея! А ты сам на гитаре умеешь играть или ты хочешь чтобы я сыграла? Если так, то я с радостью! Хотя может всё-таки ты сам хочешь сыграть?"
    me "Да, я сам хотел бы сыграть."
    mi "Здорово! Я имею в виду здорово, что ты умеешь! А ты на акустике или на электрогитаре играешь? Или может на басу? Или на всех сразу?"
    me "Акустику давай. С Электрогитарой ещё тащить комбик, потом подключать её... да и откуда её подключать?"
    mi "Хорошо-хорошо! Я поняла! Пошли тогда скорее."
    hide mi with dissolve
    "Я повернулся и подошёл к Славе"
    show sl sad swim with dissolve
    me "Славь, мы на минуточку отойдём, подождёшь?"
    show sl scared swim with dspr
    sl "Что?! За-зачем?! А если Лена сюда придёт? Не надо, пожалуйста!"
    me "Не бойся, мы ненадолго, да и на пляже много свидетелей, ничего она тебе не сделает."
    th "Наверное..."
    "На пляже были только редкие пионеры, так что \"свидетелей\" будет немного..."
    sl "Л-ладно, но, пожалуйста, постарайтесь б-быстрее..."
    me "Постараемся!"
    hide sl with dspr
    show mi smile pioneer with dissolve
    "Я развернулся к Мику, которая уже успела одеться."
    "Мы, сразу же, направились к музклубу."
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_camp_center_evening
    "Мы уже почти пришли, но внезапно Мику остановилась."
    play music music_list["orchid"] fadein 3
    show mi shocked pioneer with dissolve
    mi "Смотри!"
    me "Ну что там..."
    "Без интереса ответил я."
    mi "Там Ульянка..."
    me "И что? Никогда Ульянок не видела?"
    mi "Она стоит, смотрит куда-то в одну точку и не двигается...{w} Надо подойти и спросить всё ли у неё в порядке."
    "Мику уже хотела пойти к Ульяне, но я схватил её за руку."
    me "Стой! Я пообещал Славе, что мы быстро вернёмся."
    stop music fadeout 3
    mi "Но..."
    me "Да ничего с ней не случилось! Небось, стоит и ждёт жертву для своего розыгрыша."
    show mi sad pioneer with dspr
    mi "Да...{w} наверное ты прав..."
    scene bg ext_musclub_near_sunset with dissolve
    "Мы наконец пришли."
    th "Славя, наверное, {b}уже{/b} заждалась..."
    show mi smile pioneer with dissolve
    mi "Сень, подожди-ка тут чуть-чуть. Не бойся я быстро, одна нога там, другая здесь! Тебе медиатор нужен или нет? А гитару настроить? Хотя она может и так настроена... Надо проверить."
    me "Давай, иди уже, а то так Славя точно нас не дождётся."
    show mi upset pioneer with dspr
    mi "Ой, прости, что-то я заболталась."
    hide mi with dspr
    play sound sfx_open_door_1
    "Мику, наконец, забежала в клуб."
    th "Неужели!"
    scene bg black with dissolve
    "..."
    "..."
    "Спустя минут пять, Мику вышла."
    play sound sfx_close_door_1 
    scene bg ext_musclub_near_sunset with dissolve
    show mi normal pioneer with dissolve
    th "Я уж думал, что она там испарилась."
    me "Что ты там так долго делала?"
    show mi upset pioneer with dspr
    mi "Я медиатор искала."
    me "Зачем? Ладно, с ним сыграю, не пропадать же добру."
    show mi sad pioneer with dspr
    "Мику погрустнела."
    mi "Я не нашла..."
    me "Подожди, ты что, потерянный медиатор искала?"
    mi "Да..."
    play sound laugh_male
    me "Ахахаха, Мику, вроде музыкантка, а ищешь потерянный медиатор."
    mi "Ну, вдруг бы нашёлся..."
    me "Ладно-ладно, пошли уже и так тут задержались."
    mi "Угу."
    play ambience ambience_lake_shore_evening fadein 3
    scene bg ext_beach_sunset with dissolve
    "Пока мы ходили за гитарой, все кроме Слави ушли с пляжа."
    th "Нелегко пришлось ей..."
    show sl scared swim with dissolve
    sl "Т-ты ж-же г-говорил, что вы б-быстро..."
    me "Знаешь как говорят: Время относительно..."
    sl "Я ч-чуть с ума не с-сошла от с-страха..."
    me "Прости. Но ничего же не произошло."
    sl "Н-ну да."
    me "Ну тогда начнём."
    show sl surprise swim with dspr
    sl "Что начнём?"
    me "Музыкальный вечер."
    "Сразу как я это сказал Мику из-за спины достала гитару."
    sl "Так вот зачем вы ходили..."
    show sl smile swim with dspr
    sl "Ну тогда вперёд и с песнями!"
    th "Буквально."
    "Я присел на бревно возле подстилки, проверил гитару, чуть поднастроил и начал играть."
    scene cg senya_na_gitare with dissolve
    "{b}Сейчас играет: Свидетельство о смерти - Привет (cover by inache){/b}"
    stop ambience fadeout 2
    play music privet fadein 2
    "..."
    "..."
    "..."
    me "Привет всем не проснувшимся, оставшимся во сне, глядевшим накануне сквозь стеклянные глаза..." 
    me "Тем, кто любил ходить, смотреть на звёзды по весне, тем, кто любил ласкать и гладить нежно волоса."
    me "Отсюда, на тот свет в кирзовых сапогах, я не хотел..."
    me "Ты не жалей меня, мозоли на ногах – я не успел..."
    me "Паркетный пол трещит под моей крышкой черепной. Сегодня я узнал, что стал не нужен никому.{w} Когда настанет утро, я опять уйду домой и буду всё равно идти наперекор всему."
    me "Отсюда, на тот свет, забыв в кармане страх... я не хотел..." 
    me "Ты не жалей меня, мозоли на ногах – я не успел..."
    me "Я помню, как сплетались наши жаркие тела. Мне говорили, что все ощущали тот пожар."
    me "Как лучик из-под двери видел я свои дела и с болью замечал, что мир стал безнадёжно стар..."
    me "Отсюда, на тот свет, забыв в кармане страх, я не хотел..."
    me "Ты не жалей меня, мозоли на ногах – я не успел..."
    me "Отсюда, на тот свет, в кирзовых сапогах, я не хотел..."
    me "Ты не жалей меня, мозоли на ногах – я не успел..."
    "..."
    stop music fadeout 2
    scene bg ext_beach_sunset with dissolve
    "После окончания первой песни все звуки затихли. {w} Казалось, что даже шум воды затих."
    show sl normal swim at cleft with dissolve
    "Славя шепотом сказала:"
    sl "Ты успел..."
    show mi sad swim at cright with dissolve
    mi "Грустная песня... Я её никогда не слышала. Откуда ты её знаешь?"
    me "Скажем так... эта песня группы из моих краёв."
    sl "Семён, давай ещё."
    me "Окей."
    scene cg senya_na_gitare with dissolve
    "{b}Сейчас играет: Свидетельство о смерти - Считалочка (cover by inache){/b}"
    stop ambience fadeout 1
    play music schitalochka fadein 1
    "..."
    me "Мне надоело нюхать тухлый труп, он мне махал призывно из окна. Я знал, что человек настолько туп, что будет ждать до самого конца."
    me "Раз и два — будем там, три, четыре — салю я, пять и шесть — потолок, семь и восемь — вот петля."
    me "Всю жизнь мечтал купить я пулемёт, чтоб из окна стрелять по черепам.{w} Раскиданным по улице вокруг, пылящимся по засранным углам."
    me "Раз и два — будем там, три, четыре — салю я, пять и шесть — потолок, семь и восемь — вот петля."
    me "Я буду кирпичом по голове, я буду как подножка за углом, как будто невзначай и невпопад, когда-нибудь ты не вернёшься в дом."
    me "Раз и два — будем там, три, четыре — салю я, пять и шесть — потолок, семь и восемь — вот петля."
    me "Раз и два — будем там, три, четыре — салю я, пять и шесть — потолок, семь и восемь — вот петля."
    "..."
    stop music fadeout 3
    scene bg ext_beach_sunset with dissolve
    show sl sad swim at cleft with dissolve
    show mi sad swim at cright with dissolve
    "Лица девочек заметно погрустнели."
    th "Неудивительно.{w} С такой-то песней..."
    mi "Это уже что-то совсем грустное..."
    sl "Давай что-то по позитивнее..."
    me "Ну, как хотите."
    "Я пожал плечами."
    "{b}Сейчас играет: Кино - Мама мы все сошли с ума (cover by conograi){/b}"
    play music mama_my_soshli_suma
    scene cg senya_na_gitare with dissolve
    "..."
    me "Зёрна упали в землю, зёрна просят дождя...{w} им нужен дождь."
    me "Разрежь мою грудь, посмотри мне внутрь. Ты увидишь, там всё горит огнём."
    me "Через день будет поздно, через час будет поздно, через миг будет уже не встать..."
    me "Если к дверям не подходят ключи - вышиби двери плечом!"
    me "Мама, мы все тяжело больны... Мама, я знаю мы все сошли с ума..."
    "..."
    me "Сталь между пальцев, сжатый кулак!"
    me "Удар выше кисти, терзающий плоть."
    me "Но вместо крови в жилах застыл яд,{w} медленный яд."
    me "Разрушенный мир, разбитые лбы, разломанный надвое хлеб!"
    me "И вот кто-то плачет, а кто-то молчит, а кто-то так рад, кто-то так рад."
    me "Мама, мы все тяжело больны... Мама, я знаю мы все сошли с ума..."
    "..."
    me "Ты должен быть сильным, ты должен уметь сказать:{w} Руки прочь, прочь от меня!"
    me "Ты должен быть сильным!{w} Иначе зачем тебе быть?"
    me "Что будут стоить тысячи слов, когда важна будет крепость руки?"
    me "И вот ты стоишь на берегу... и думаешь плыть или не плыть?"
    me "Мама, мы все тяжело больны, мама, я знаю мы все сошли с ума."
    me "Все тяжело больны, мама я знаю, мы все сошли с ума..."
    stop music fadeout 3
    scene bg ext_beach_sunset
    show sl normal swim at cleft
    show mi surprise swim at cright
    with dissolve
    "Девочки какое-то время просто тихо сидели..."
    "А потом Славя захлопала мне в ладоши."
    play sound clap_1
    "Мику же была в таком восторге, что не могла пошевелиться."
    sl "Потрясающе! Сколько же ты тренировался..."
    th "Учился играть на гитаре я довольно долго. С музыкой можно какое-никакое разнообразие добавлять. Даже пару раз концерты устраивал."
    "Мику наконец отошла от восторга."
    mi "А как ты..."
    me "Так хорошо играю?"
    show mi shy swim at cright with dspr
    mi "Д-да..."
    me "Просто у меня был хороший учитель."
    "Я мило улыбнулся."
    show mi smile swim at cright with dspr
    mi "У тебя был отличный учитель! Даже я так не смогу сыграть эту песню!"
    th "Забавно выходит..."
    me "Может ты тоже что-то сыграешь?"
    show mi surprise swim at cright with dspr
    mi "Я?"
    me "Ты."
    mi "Ну, можно наверное...{w} Только вот что?"
    me "Давай тоже какую-нибудь песню Витьки."
    show mi smile swim with dspr
    mi "Ну давай!"
    "Я отдал гитару Мику."
    scene cg gitara_miku_bereg_sunset with dissolve
    "{b}Сейчас играет: Кино - Группа крови (cover by Mare){/b}"
    play music gruppa_krovi_cover_by_Mare fadein 2
    "..."
    "..."
    mi "Тёплое место, но улицы ждут отпечатков наших ног."
    mi "Звёздная пыль...{w} на сапогах."
    mi "Мягкое кресло, клетчатый плед, не нажатый вовремя курок."
    mi "Солнечный день в ослепительных снах."
    mi "Группа крови на рукаве, мой порядковый номер на рукаве..."
    mi "Пожелай мне удачи в бою.{w} Пожелай мне..."
    mi "Не остаться в этой траве...{w} не остаться в этой траве."
    mi "Пожелай мне удачи...{w} Пожелай мне...{w} удачи."
    "..."
    mi "И есть чем платить, но я не хочу{w} победы любой ценой."
    mi "Я никому{w} не хочу ставить ногу на грудь."
    mi "Я хотел бы остаться с тобой.{w} Просто остаться с тобой."
    mi "Но высокая в небе звезда... зовёт меня в путь."
    "..."
    mi "Группа крови на рукаве, мой порядковый номер на рукаве..."
    mi "Пожелай мне удачи в бою.{w} Пожелай мне..."
    mi "Не остаться в этой траве...{w} не остаться в этой траве."
    mi "Пожелай мне удачи...{w} Пожелай мне...{w} удачи."
    stop music fadeout 2
    scene bg ext_beach_sunset with dissolve
    "..."
    me "Прекрасно!"
    show sl smile swim at cright with dissolve
    sl "Согласна, это было здоровски."
    scene bg black with dissolve
    "Мы ещё немного поиграли около десятка песен на гитаре, вместе с Мику, и закончили уже когда стемнело."
    scene bg ext_beach_night with dissolve
    play ambience ambience_lake_shore_night fadein 2
    $ persistent.sprite_time = "night"
    $ night_time()
    show mi normal swim at cleft with dspr
    mi "Поздно уже, пора бы по домам..."
    me "Да, пожалуй..."
    show sl normal swim at cright with dspr
    sl "А может ещё немного посидим?"
    me "Ну, мы сюда за этим и пришли..."
    show mi serious swim at cleft with dspr
    mi "Простите ребят, но мне нужно ещё в клуб гитару отнести и ещё кое-что там сделать, поэтому оставайтесь без меня, ладно?"
    me "Хорошо, иди."
    show mi smile swim at cleft with dspr
    "Мику напоследок одарила нас своей улыбкой и удалилась."
    hide mi with dspr
    "..."
    $ save_name = ('День 2. Ночью на пляже.')
    show sl smile2 swim with dspr
    sl "Может искупаемся?"
    me "Ну... можно, в принципе."
    show sl happy swim with dspr
    sl "Тогда пошли!"
    hide sl with dspr
    "Славя сразу побежала в воду."
    "Я недолго думаю разделся и пошёл к ней в воду."
    scene bg ext_beach_water_night with dissolve
    stop ambience fadeout 2
    play music music_list["confession_oboe"]
    play ambience water_ambience fadein 4 
    "Вода была прохладной, но мне не привыкать.{w} Славя плескалась, наслаждаясь водой."
    "Она грациозно нырнула в воду, изящно с легкостью плавала уже на глубине."
    "Я и не заметил как она приблизилась ко мне и цапнула за ногу."
    me "Ааааа!"
    show sl laugh swim close with dspr 
    play sound hihikane
    sl "Хихи, ты меня и не заметил."
    me "Да... залюбовался малость."
    show sl smile2 swim close with dspr 
    "После моего ответа повисло неловкое молчание."
    "Славя решила его прервать, плеснув в меня водой."
    show sl happy swim close with dspr 
    me "Эй! Ты чего?"
    "Славя вместо ответа провернула тоже самое."
    me "Ах ты..."
    "Я решил отомстить, поэтому, как следует замахнувшись, я сотворил мини-цунами."
    scene bg black with dissolve
    "Мы, весело плескаясь, смеялись и создавали сверкающие брызги, мы наслаждались...{w} наслаждались этим волшебным моментом."
    "Внезапно наши взгляды пересеклись. Лунный свет освещал Славино личико, создавая умиротворенное волшебство."
    "Мы замерли, просто глядя друг другу в глаза."
    "В её глазах отражалась луна...{w} Не знаю, что, но что-то в этот момент почувствовал."
    "Хотя понять, что это было, я не смог."
    "Я бы так стоял ещё очень долго, но Славя прервала момент."
    scene bg ext_beach_water_night
    show sl shy swim close 
    with dissolve
    sl "Пойдём?.."
    me "..."
    sl "Сень?"
    me "Д-да?.."
    sl "Пойдём."
    "Мы вышли из воды."
    scene bg ext_beach_night
    show sl sad swim 
    with dissolve
    sl "А что теперь?"
    me "Не знаю... наверное давай пойдём в твой домик, в моём - вожатая спит."
    show sl smile2 swim with dissolve
    sl "Хорошо."
    stop music fadeout 3
    play ambience ambience_camp_center_night fadein 3
    "..." 
    scene bg ext_house_of_sl_night with dissolve
    show sl surprise pioneer with dissolve
    sl "Подожди, а как же Женя?"
    me "А мы тихонечко."
    show sl sad pioneer with dspr
    sl "Нет, так не пойдёт..."
    "Видимо, моя шутка не выдалась."
    me "Ну, не знаю, предупреди её как-нибудь..."
    show sl surprise pioneer with dspr
    sl "Предупредить? Прямо посреди ночи? И что я ей скажу? \"Жень, можешь, пожалуйста, сегодня вне домика переночевать, я парня хочу привести\"?"
    me "Ну..."
    "Я замялся."
    me "И что тогда делать?"
    show sl normal pioneer with dspr
    sl "Давай сходим к тебе, ты возьмёшь фонарик в домике, а потом пойдём переночуем на склад, там на куче матрасов можно поспать."
    me "А ко мне зачем? Там что света нет?"
    sl "Он-то есть, но нас так могут заметить, если долго будем искать всё необходимое."
    me "Ладно."
    scene bg ext_houses_night with dissolve
    $ save_name = ('День 2. Все пропали!?')
    play music sdl_tpinf_cu fadein 5
    "Подойдя к домику мы увидели Электроника, который о чём-то на повышенных тонах спорил с... Леной."
    "Я прошептал Славе:"
    me "В кусты."
    show sl surprise pioneer close at cright with dissolve
    sl "Что?"
    "Я без лишних слов, взял её за руку и потянул в кусты."
    me "Смотри, там Лена и Эл."
    show sl scared pioneer close at cright with dspr
    sl "Л-лена?"
    me "Да, только тише ты! Дай же послушать о чём они спорят."
    "Славя кивнула."
    hide sl with dissolve
    "..."
    scene bg ext_house_of_mt_night_without_light with dissolve
    show el angry pioneer far at cleft
    show un angry pioneer far at cright
    with dissolve
    un "А что ты знаешь?!"
    el "Да я-то что?! Я вообще своего друга тут ищу, а ты вот что делаешь?! И вообще иди к себе домой!"
    show un rage pioneer far at cright with dspr
    with vpunch
    un "А ТЫ В КУРСЕ, ЧТО МЫ, ПОХОЖЕ, ОСТАЛИСЬ В ЛАГЕРЕ ВДВОЁМ!?"
    show el surprise pioneer far at cleft with dspr
    el "Что?!"
    "Пыл Электроника резко угас и сменился на удивление."
    un "Что слышал!"
    show el normal pioneer far at cleft with dspr
    "Кибернетик о чём-то задумался."
    el "И правда... как-то слишком уж тихо..."
    "Через пару мгновений Алиса прибежала вся впопыхах."
    show dv scared pioneer far at fright with dissolve
    dv "Что... у вас... тут случилось?"
    show el angry pioneer far at cleft with dspr
    el "Ты же говорила, что мы остались в лагере вдвоём!?"
    show un shy pioneer far at cright with dspr
    un "Эээ..."
    "Пока Лена замялась, к ним вышла ещё и Мику."
    show mi normal pioneer far at fleft with dissolve
    mi "О! Ребята, привет! Вы нигде не видели Лену, а то она до сих пор не вернулась. Я за неё очень переживаю, даже вот искать пошла..."
    dv "Я многих обошла, похоже, что кроме нас, в лагере и правда никого нет..."
    show mi scared pioneer far at fleft with dspr
    mi "Что?!"
    show un serious pioneer far at cright with dspr
    un "Что слышала!"
    show dv angry pioneer far at fright with dspr
    dv "Не заводитесь вы! Сейчас не время для ссор! И ещё - может хватит уже притворяться?"
    th "Притворяться?{w} Она что... тоже!?"
    show el sad pioneer far at cleft with dspr
    el "Да... простите..."
    show un rage pioneer far at cright with dspr
    with vpunch
    un "ДА ТЫ! Да ты!" 
    show un normal pioneer far at cright with dspr
    un "Да ты...{w} Да, ты права..."
    "По интонации Лены было видно, что со своими словами она абсолютно не согласна."
    show mi sad pioneer far at fleft
    show dv sad pioneer far at fright
    with dspr
    mi "Так, что же нам делать, если кроме нас и вправду никого больше нет? А что если с ними что-то случилось? Что-то очень-очень плохое... Нет даже думать такого не хочу."
    show el normal pioneer far at cleft with dspr
    el "Сначала нам надо убедиться, что действительно все пропали."
    un "Хорошо, тогда я схожу, проверю домики всех пионеров и столовую."
    show el surprise pioneer far at cleft with dspr
    dv "Ау!{w} Я же вроде попросила. Сейчас не время для шуток!"
    el "Одна?"
    "Слова Алисы, все пропустили мимо ушей."
    show un grin pioneer far at cright with dspr
    un "Да, а что? Хочешь сопроводить даму?"
    show el scared pioneer far at cleft with dspr
    el "Ну... нет..."
    show un normal pioneer far at cright with dspr
    un "То-то же."
    hide un with dissolve
    "Лена развернулась и пошла проверять домики."
    "Как только Лена ушла, нависла полная тишина."
    th "Чёрт!{w} Я понял - Алиса, похоже, вместе со мной переместилась в {b}этот{/b} лагерь."
    scene bg ext_houses_night with dissolve
    $ persistent.sprite_time = "night"
    "Я развернулся к Славе."
    th "Надо им всем рассказать, кто такая Лена на самом деле!"
    me "Славь, надо бы предупредить всех про Лену."
    show sl scared pioneer close at cright with dissolve
    sl "М-может не надо?"
    me "Что? Почему это не надо?"
    sl "А что будет, если она внезапно вернётся и увидит нас? Как ты думаешь, что она сделает? Или ещё хуже, нам не поверят и расскажут Лене про нас."
    th "Ну если рассуждать логически, она права... но всё же..."
    stop music fadeout 5
    th "Всё же для ребят она представляет опасность."
    menu:
        "Как поступить?"
        "Рассказать пионерам про Лену":
            $ sl_bad_ochki += 2
            $ sl_good_ochki -= 2
        "Молча уйти":
            $ sl_good_ochki += 2  
            $ sl_bad_ochki -= 2
    
    if sl_good_ochki >= 2:
        jump somesing_new_good_sl
    else:
        jump somesing_new_bad_sl

    
label somesing_new_good_sl:
    $ save_name = ('День 2. Делаем ноги.')
    play music napryagis2 fadein 23
    th "И что? Эти ребята, это просто куклы, а Славя...{w} она уже перестала быть ей."
    th "И зачем, спрашивается, мне рисковать единственным дорогим мне человеком ради каких-то кукол."
    th "Правильно - незачем."
    th "..."
    th "Стоп! Как я только что назвал Славю?!{w} Я... что...{w} влюбился?.."
    th "Вот уж не думал, что ещё способен на это."
    me "Да, ты права, лучше пойдём."
    show sl normal pioneer close at cright with dspr
    sl "Хорошо. Только куда вот?"
    me "Давай дождемся Лену, и пойдём к тебе в домик. Всё равно Женя исчезла."
    show sl sad pioneer close at cright with dspr
    sl "Надеюсь с ней всё в порядке..."
    me "..."
    show sl normal pioneer close at cright with dspr
    sl "Хорошо, поступим так как ты предложил."
    scene bg ext_house_of_mt_night_without_light 
    show el scared pioneer far at cleft
    show mi sad pioneer far at fleft
    show dv sad pioneer far at cright
    with dissolve
    "Мы начали пристально наблюдать за всеми."
    "Лена небыстро, но всё же вернулась."
    show un normal pioneer far at fright with dspr
    el "Ну что?"
    un "Никого."
    show mi shocked pioneer far at fleft with dspr
    mi "Как это никого? Прям вообще-вообще никого?"
    un "Да."
    el "И куда все пропали?"
    mi "Может их инопланетяне похитили?.."
    show el scared pioneer far at cleft with dspr
    el "Инопланетяне?{w} Но это же антинаучно!"
    un "А какие у тебя тогда варианты? Скептик ты наш..."
    show el surprise pioneer far at cleft with dspr
    show mi pioneer far at fleft with dspr
    el "У меня?"
    "Лена кивнула."
    show el scared pioneer far at cleft with dspr
    el "Н-не знаю я! Может разыграть нас решили..."
    dv "Все до единого пионера?"
    show el sad pioneer far at cleft with dspr
    el "Ну..."
    "Электроник замялся."
    mi "Тогда где все?"
    un "Выходит, что они бесследно исчезли."
    show el scared pioneer far at cleft with dspr
    el "И что нам делать?"
    show mi sad pioneer far at fleft with dspr
    mi "А вдруг мы...{w} тоже исчезнем?"
    dv "Надо держатся вместе..."
    show un evil_smile pioneer far at fright with dissolve
    show un normal pioneer far at fright with dissolve
    un "Хорошая мысль."
    show el surprise pioneer far at cleft with dspr
    el "И где тогда спать будем?"
    show dv normal pioneer far at cright with dspr
    dv "Можно прямо здесь."
    show un rage pioneer far at fright 
    show el scared pioneer far at cleft 
    with dspr
    un "НЕТ!{w} Это дом Семёна, вы не имеете права входить туда, без его разрешения!" with vpunch
    show dv sad pioneer far at cright with dspr
    dv "Л-ладно ты... не кипятись... Не будем к твоему Семёну заходить."
    show un grin pioneer far at fright with dspr
    un "То-то же."
    "Удовлетворённо сказала Лена."
    el "Тогда где спать будем?"
    show un smile3 pioneer far at fright with dspr
    un "Да хоть у тебя."
    el "Ну... можно, наверное..."
    dv "На том и решили..."
    hide dv
    hide mi
    hide un
    hide el
    with dissolve
    "Все направились к домику Электроника, я полагаю."
    scene bg ext_houses_night with dissolve
    me "Ну...{w} двигаем?"
    show sl surprise pioneer close with dissolve 
    sl "Что?"
    me "Пошли говорю."
    show sl normal pioneer close with dspr
    sl "А, да, пойдём"
    "Мы опять направились к домику Слави."
    scene bg ext_house_of_sl_night with dissolve
    stop music fadeout 3
    $ save_name = ('День 2. Запасы.')
    "Когда мы пришли я кое-что вспомнил."
    me "Блин..."
    show sl surprise pioneer with dissolve
    sl "Что такое?"
    me "Нам бы надо едой запастись..."
    show sl sad pioneer with dspr
    sl "Точно...{w} Завтра ведь они скорее всего первым делом пойдут в столовую..."
    me "Да, поэтому нам лучше запастись заранее, чтобы случайно лишний раз не попасться кому-нибудь на глаза."
    sl "Подожди тут секунду я возьму какой-нибудь рюкзак и пойдём."
    me "Да, рюкзак бы не помешал."
    hide sl with dissolve
    play sound sfx_open_door_1 
    "Славя зашла в домик."
    "..."
    play sound sfx_close_door_1 
    show sl normal pioneer far with dissolve
    "И действительно через пару секунд, она вышла."
    me "А ты быстро."
    show sl smile pioneer with dissolve
    sl "На это и был расчёт."
    me "Ладно, пойдём наконец."
    sl "Ага."
    scene bg black with dissolve 
    window hide dissolve
    pause 2.0
    scene bg ext_dining_hall_away_night with dissolve
    window show dissolve
    play music melonholy fadein 3
    "Через несколько минут, мы уже подходили к столовой."
    me "У тебя же ключи с собой?"
    show sl smile pioneer with dissolve
    sl "Да, конечно.{w} Как же я, помощница вожатой могу быть без ключей."
    "Славя, видимо, попыталась пошуть."
    scene bg ext_dining_hall_near_night with dissolve
    me "Ну фонарик ты же потеряла..."
    show sl sad pioneer with dissolve
    sl "Ох..."
    me "Пришли."
    show sl surprise pioneer with dspr
    sl "А...{w} ага."
    "..."
    "Мы просто стояли и смотрели на дверь."
    me "Ключи у тебя, если что."
    show sl shy pioneer with dspr
    sl "Ой, да...{w} Секунду..."
    show sl normal pioneer far at cright with dspr
    "Славя порылась в карманах, достала ключ и принялась открывать дверь."
    play sound sfx_alisa_picklock 
    $ renpy.pause(4.0, hard=True)
    play sound sfx_open_door_1
    sl "Тут открыто!{w} Заходи!"
    hide sl with dissolve
    "Славя зашла в столовую."
    "Я тоже не медля зашёл во внутрь"
    scene bg int_dining_hall_night with dissolve 
    stop ambience fadeout 3
    "..."
    show sl normal pioneer with dissolve 
    sl "Давай так: Я пойду на кухню, наберу еды, а ты пока, чтобы не терять времени сходи на склад возьми что-нибудь, что может понадобиться."
    me "Хорошо."
    show sl smile pioneer with dissolve 
    hide sl with dissolve 
    "Славя мило улыбнулась и пошла на кухню."
    "..."
    th "Что можно взять на складе?"
    th "Наверное оружие и...{w} и что?"
    th "..."
    th "Ладно, остановимся на оружии."
    "Я направился на склад."
    scene bg black with dissolve 
    window hide dissolve 
    pause 2.0
    scene bg ext_sklad_night with dissolve 
    window show dissolve
    play ambience ambience_camp_center_night fadein 4
    "Подойдя к складу я остановился."
    th "..."
    th "А тут красивый вид..."
    th "..."
    th "Тьфу ты! Я же за оружием пришёл!"
    th "Блин..."
    th "А ключей-то нет!"
    th "В таком случае, надеюсь, что он как и столовая открытый."
    play sound sfx_open_door_sklad
    stop ambience fadeout 2
    "Дёрнув ручку, мои надежды сбылись - склад оказался открытым, поэтому я вошёл."
    scene bg int_sklad2_night with dissolve
    th "Ну, склад я на изусть знаю, поэтому я тут не надолго надеюсь."
    "Однако склад {i}тоже оказался другим.{/i} {w} Не сильно кончно, но почти всё было на других местах."
    "Пошарив по нему минут 10 я нашёл пару вещей которыми можно нанести ущерб."
    ##Чеховское ружьё(фомка поможет открыть дверь в бункер)
    th "Фомка и молоток..."
    play sound stuk_v_dver
    "Внезапно в дверь постучали."
    "Я насторожился."
    "Однако из-за двери раздался знакомый голос."
    sl "Семён, это я...{w} Я войду?"
    me "А, ты. Заходи конечно."
    play sound sfx_open_door_squeak_2
    show sl surprise pioneer with dissolve
    sl "Ого...{w} Вот это у тебя приоритеты, конечно..."
    me "Знаешь как говорят предпреждён - вооружён, так вот... мы теперь буквально." 
    show sl smile pioneer with dspr
    sl "Да... точно."
    me "Молоток твой, кстати."
    "Я протянял Славе руку с молотком."
    show sl surprise pioneer with dspr
    sl "Это мне?"
    me "Да, вдруг меня рядом не будет."
    sl "Спасибо, наверное..."
    "Славя положила его к себе в рюкзак."
    "..."
    me "Так, ладно, теперь спать?"
    show sl normal pioneer with dspr
    sl "Спать."
    stop music fadeout 3
    scene bg black with dissolve
    "Вышев со склада, мы направились обратно."
    "..."
    scene bg int_house_of_sl_light_night with dissolve
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_night fadein 2
    "..."
    show sl smile pioneer with dissolve
    sl "Поспим вместе?"
    th "Примерная пионерка спрашивает {i}такое{/i} и не краснеет - а-я-я-й..."
    me "Да."
    hide sl with dissolve
    "Примерная пионерка разделась и лягла в постель."
    sl "Выключи свет!"
    me "Сейчас."
    play sound vkl 
    $ persistent.sprite_time = "night"
    scene bg int_house_of_sl_night with dspr
    "После того, как я погасил свет, я также снял одежду и устроился рядом со Славей."
    show sl tender swim close with dspr
    sl "Спойной ночи..."
    me "Спокойной."
    stop ambience fadeout 5
    window hide dissolve
    show blink
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    scene bg black
    with fade3
    $ backdrop = "days"
    $ new_chapter(3, "День 3. Прятки.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "days"
    $ renpy.pause(1, hard=True)
    $ persistent.sprite_time = 'day'
    $ day_time()
    pause 1.5
    window show dissolve
    play ambience ambience_int_cabin_day fadein 2
    hide blink
    scene bg int_house_of_sl_day
    show unblink 
    $ save_name = ('День 3. Полупустой лагерь.')
    "Я проснулся. Славя ещё спала."


    




    
    
    return
    
label somesing_new_bad_sl:
    $ save_name = ('День 2. Лена - Убийца.')
    play music are_you_there_7dl fadein 5
    th "Ну как это нет? Они же будут находиться в одном окружении с маньячкой!"
    me "Славя, а представь какого им будет, если например они просыпаются, а на утро перед входом Алиса в состоянии фарша, какого им будет? А какого будет Алисе?"
    sl "..."
    show sl sad pioneer close at cright with dspr
    sl "Действительно, что это на меня нашло, конечно же надо предупредить всех!"
    scene bg ext_house_of_mt_night_without_light 
    show el shocked pioneer at cleft
    show mi scared pioneer at fleft
    show dv scared pioneer at cright
    with dissolve
    "Мы со Славей вышли к ребятам."
    "Вся компания синхронно вздрогнула."
    show sl sad pioneer at fright with dissolve
    me "Слушайте все! Срочно!"
    show mi shocked pioneer at fleft 
    show el surprise pioneer at cleft 
    show dv surprise pioneer at cright 
    with dspr
    dv "С-семён?{w} Са... Славя?{w} Так вы тоже не исчезли?"
    me "У нас мало времени, поэтому, пожалуйста, помолчите."
    "Алиса и остальные всё же решили выслушать нас."
    me "Вчера ночью Лена хотела убить Славю, но я застал её за этим и спас Славю."
    show mi scared pioneer at fleft with dspr
    show dv sad pioneer at cright with dspr
    show el scared pioneer at cleft with dspr
    me "Вам нельзя находиться рядом с ней, пошлите скорее отсюда пока Лена не вернулась!"
    el "Что!?"
    dv "Теперь ещё и это..."
    show mi dontlike pioneer at fleft with dspr
    mi "Что!? Чтобы Лена? Быть такого не может, она же такая тихоня... она и кузнечика испугается, не говоря уже об убийствах..."
    me "Я вас прошу... быстрее пойдёмте, Лена может скоро вернуться, и, кто знает, что ей на ум придёт..."
    dv "Семён."
    me "Да?"
    dv "Я вам верю. Пошлите."
    show mi sad pioneer at fleft with dspr
    mi "Алиса? И ты в это веришь?"
    dv "Я уже во что угодно поверю... и рисковать не хочу."
    "Вдали начал вырисовываться силуэт с двумя хвостиками по бокам."
    me "Пошлите же вы! Разве вы не понимаете, что, оставаясь сейчас тут, подписываете себе смертный приговор?!"
    show el angry pioneer at cleft with dspr
    el "Хватит ерунду всякую молоть! Она не способна на... такое."
    stop music fadeout 7
    me "Ладно, я вас предупреждал! Только прошу... не говорите о нас Лене."
    el "То есть ты у нас похищаешь Алису и нам ещё об этом молчать? Ну уж нет!"
    "Не ответивши ему ничего, я взял девочек за руки и побежал."
    stop ambience fadeout 2
    play music iron fadein 2
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "Мы побежали куда глаза глядят."
    th "Клятый Электроник!"
    dv "Куда мы бежим?"
    me "Не знаю! Лишь бы подальше от Лены!"
    th "Чёрт..."
    th "Лишь бы они не рассказали про нас Лене."
    scene bg ext_path_night with dissolve
    "Мы забежали в лес и на пару секунд остановились."
    show sl scared pioneer at cleft with dissolve
    show dv scared pioneer at cright with dissolve
    me "Этот лес слишком близко, к домикам бежим дальше!"
    "Девочки кивнули."
    scene bg ext_path2_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "Не теряя времени, мы помчались вперёд."
    "..."
    scene bg ext_path_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "..."
    "Спустя несколько минут, мы выбежали на какую-то тропинку."
    "..."
    scene bg ext_musclub_night with dissolve
    play ambience ambience_camp_center_night fadein 2
    "Мы остановились, когда перед нами показался Музыкальный клуб."
    me "Думаю...{w} нормально...{w} отбежали..."
    show dv sad pioneer at cright with dissolve
    dv "И куда теперь?"
    show sl sad pioneer at cleft with dissolve
    sl "Надо где-то переночевать..."
    me "Может, как мы сначала и хотели?"
    show dv surprise pioneer at cright with dspr
    dv "Как вы хотели?"
    show sl normal pioneer at cleft with dspr
    sl "На склад."
    show dv scared pioneer at cright with dspr
    dv "А там не опасно?"
    stop music fadeout 7
    me "Точно не опаснее, чем в домиках."
    show dv sad pioneer at cright with dspr
    dv "Ладно, пойдёмте."
    scene bg black with dissolve 
    window hide dissolve 
    pause 2.5
    scene bg int_sklad2_night with dissolve
    window show dissolve 
    play ambience ambience_int_cabin_night fadein 3
    show dv sad pioneer at cright with dissolve
    show sl normal pioneer at cleft with dissolve
    me "Подождите, я достану пару матрасов и на пол постелю."
    sl "Я тебе помогу."
    me "Как знаешь."
    hide sl
    hide dv 
    with dissolve
    "Славина помощь действительно пришла кстати, поэтому мы управились за пару минут."
    me "Готово."
    show dv sadness pioneer at cleft with dissolve
    show sl smile pioneer at cright with dissolve
    sl "А почему только два, там же есть ещё?"
    "Я ничего не сказал, а просто хитро улыбнулся."
    show sl shy pioneer at cright with dspr
    "Пока Славя смущалась, меня позвала Алиса."
    dv "Семён, можно тебя на минутку?"
    show sl surprise pioneer at cright with dspr
    me "Зачем?"
    dv "Я хочу спросить кое-что."
    me "Ладно.{w} Славя мы ненадолго."
    sl "Я поняла."
    scene bg ext_sklad_night with dissolve
    play ambience ambience_camp_center_night fadein 3
    show dv sad pioneer with dissolve
    dv "Семён, а ты помнишь фильм?"
    th "Выходит, мои догадки оправдались."
    me "Помню, но если ты думаешь, что я из твоего мира, то нет, этот лагерь мне роднее будет."
    me "Хотя, впрочем, это тоже не мой мир."
    dv "Вот как...{w} Ещё вчера, я даже подумать не могла, что со мной бухает пришелец из другого мира..."
    me "..."
    show dv shy pioneer with dspr
    dv "А вы со Славей...{w} встречаетесь?"
    me "О-о-ой...{w} Хороший вопрос.{w} Не знаю даже..."
    dv "Ясно..."
    me "А почему спрашиваешь?"
    show dv shocked pioneer with dspr
    dv "Я э-э-э-э...{w} ну это..."
    show dv shy pioneer with dspr
    dv "Неважно."
    me "Как знаешь."
    "..."
    me "Может спать пойдём?"
    dv "А?{w} А да, давай."
    play sound sfx_open_door_sklad
    scene bg int_sklad2_night with dissolve
    play ambience ambience_int_cabin_night fadein 3
    me "Не заждалась?"
    show sl normal pioneer far at cright with dissolve
    sl "Нет-нет, вы быстро..."
    me "Ну и отлично."
    "Алиса легла на пустой матрас, а я лёг к Славе."
    show sl smile2 pioneer close with dissolve
    sl "Спокойной ночи?"
    dv "Спокойной."
    me "Ага."
    stop ambience fadeout 5
    window hide dissolve
    show blink
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    scene bg black
    with fade3
    $ backdrop = "days"
    $ new_chapter(3, "День 3. Прятки.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "days"
    $ renpy.pause(1, hard=True)
    $ persistent.sprite_time = 'day'
    $ day_time()
    pause 1.5
    window show dissolve
    play ambience ambience_int_cabin_day fadein 2
    hide blink
    scene bg int_sklad2_day
    show unblink  
    th "Доброе утро."


    




    
    return
    
label somesing_new_ubivasha_rut:
    $ save_name = ('День 2. Кровавое утро.')
    th "Ну, рыбак рыбака, как говорится. Похоже, я нашёл настоящую Лену. Ну, по крайней мере точно не обычную Лену."
    th "Теперь наконец, можно повеселиться с кем-то."
    me "Леночка, а что ты сделаешь, если я попрошу тебя дать мне её убить."
    un "Обрадуюсь, что мой возлюбленный, такой же сумасшедший как и я."
    me "Тогда возрадуйся! Я тебя прошу, дай мне её убить!"
    play music wire fadein 3
    "Славя молча слушала как Семён просит её убить, она не могла поверить, что это всё, действительно происходит."
    "Лена же, поначалу приятно удивилась и всё же предоставила Семёну эту возможность."
    un "Ого..."
    un "В таком случае, прошу."
    "Лена жестом пригласила идти к Славе."
    "Я молча пошёл к Славе."
    hide un with dissolve
    show sl cry pioneer at left with dspr
    sl "С-с-семён?"
    me "..."
    show sl cry pioneer close at cleft with dspr
    sl "Эт-то же шутка, да?{w} Это же у т-тебя т-такой план, чтобы спасти меня?"
    "Я взял её руку и сломал 4 пальца, одним движением."
    play sound slomal_palcy
    pause 0.3
    play sound krik_boli_wom
    sl "А-а-а-а-а-а-а-а-а-а-а-а-а-а!"
    "Славя закричала от боли."
    me "Нет, Славя. Это не план, ты умрёшь. Умрёшь мучительной смертью."
    "Я попытался выдавить на своём лице, подобие милой улыбки."
    "Славя, уже больше не могла издать даже звука. Она находилась в полном отчаянии."
    me "Славя хочешь сыграем в игру?"
    show sl scared pioneer close at cleft with dspr
    "Славя со смесью страха и отчаяния, вопросительно посмотрела на меня."
    me "Сыграем в \"Камень, ножницы бумагу\"?"
    sl "..."
    me "Ставка будет твои пальцы на правой руке."
    me "Если я выиграю, когда у тебя будет бумага, отрываю пять пальцев, если когда ножницы - два, если когда камень - нисколько."
    me "Если я проиграю, то дам тебе возможность убежать и фору в 30 секунд."
    me "Заметь, если ты выкинешь камень, то мы будем считать, что этой игры не было и просто оставим пальцы в покое."
    me "Согласна?"
    "Славя кивнула."
    me "Ну начнём.{w} Камень, ножницы, бумага!"
    "Славя и я выкинули ножницы."
    me "Что ж, ничья, продолжаем."
    me "Камень, ножницы, бумага!"
    "Славя на этот раз выкинула бумагу, а я не изменил свой выбор - ножницы."
    "Славя с ужасом посмотрела на свою руку, а потом на меня,{w} а потом снова на руку,{w} а потом снова на меня."
    me "Славя давай сюда ручку."
    "Славя спрятала свою руку за спину."
    me "Славя."
    "Строго сказал я."
    "Славя не отреагировала."
    with vpunch
    me "ТЫ{w} ДОЛЖНА МНЕ{w} ПЯТЬ ПАЛЬЦЕВ!"
    sl "..."
    "Я попросил у Лены тесак, взял Славю за руку и резко отрезал ей все пальцы." 
    play sound nozhom_palcy
    pause 0.2
    play sound krik_boli_wom
    sl "ААААААААААААААААААААААА!!!"
    me "Ну, у тебя был шанс."
    "..."
    me "Такс...{w} Продолжаем!{w} Какую руку тебе сломать первой?{w} Или может, отрубить?{w} Выбирай! Либо же я сначала сломаю, а потом отрублю."
    "Хитрым голосом, предложил я."
    show un evilsmile2 pioneer at right with dissolve
    un "Хорош уже, я поняла, что ты тот ещё подонок, даже, возможно, похлеще чем я. Заканчивай, скоро рассвет."
    me "Ладно-ладно."
    hide un with dissolve
    sl "..."
    me "Слышала? Нам пора закругляться, так что прощай.{w} Может  скажешь последние слова напоследок?"
    sl "..."
    me "Как знаешь."
    scene bg black with dissolve
    "Я хмыкнул и отрубил ей, сначала левую руку, потом левую ногу, потом правую руку. Славя в этот момент визжала так, как будто она свинья, которую, режут."
    th "Интересно почему?"
    play sound kill_momento
    "И наконец, я отрубил Славе голову."
    stop music fadeout 5
    play ambience ambience_forest_evening fadein 3
    scene bg ext_polyana_sunset with dissolve
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    "Я обернулся и увидел как мне аплодирует Лена."
    show un anticipation pioneer with dissolve 
    play sound clap_1
    un "Браво! Браво художник! Браво!"
    me "Спасибо! Спасибо!"
    "Я наигранно покланялся."
    me "А почему художник то?"
    show un evilsmile2 pioneer with dspr
    un "Ну, как же? Как же?{w} Разве ты не видел картину, которую сотворил?{w} Тогда обернись и любуйся!"
    "Я обернулся."
    hide un with dissolve
    stop ambience fadeout 1
    play music F21LFm
    scene cg epilogue_mi_2 with dissolve
    th "..."
    th "Твою мать..."
    th "Славя..."
    th "Это {b}Я{/b} сделал?"
    th "..."
    th "..."
    th "..."
    th "Нет, ну, вообще, если так подумать, то картина и впрямь шикарная.{w} Я бы даже сказал..."
    me "Шедевр..."
    un "И не говори..."
    "..."
    un "Ладно, пошли уже в лагерь."
    me "Да..."
    stop music fadeout 3
    stop ambience fadeout 3
    scene bg black with dissolve
    "..."
    $ save_name = ('День 2. Утро с Леной.')
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 2
    me "А куда мы идём?"
    show un smile pioneer with dissolve
    un "Ко мне в домик."
    me "А как же твоя соседка?"
    un "Не беспокойся об этом."
    me "Л-ладно."
    scene bg ext_house_of_un_sunset with dissolve
    show un smile pioneer with dissolve
    un "Пришли."
    me "Ага..."
    show un smile pioneer far with dspr 
    un "Проходи."
    stop ambience fadeout 1
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_un_day with dissolve
    me "Чем займёмся?"
    play music music_list["lets_be_friends"] fadein 2
    $ persistent.sprite_time = "day"
    show un laugh pioneer with dspr 
    un "Семё-ё-ён...{w} Вроде уже большой мальчик, а такой недогадливый."
    th "Поня-я-ятно..."
    me "Вот такой вот я. Безумный, глупый и недогадливый."
    play sound smah_nad_shutkoy_woman
    "Лена посмеялась."
    un "Ну, я тебя, и за это тоже, люблю..."
    show un smile pioneer with dspr
    un "Но если хочешь формальностей, можем чайку выпить."
    me "..."
    me "А давай!"
    show un smile3 pioneer with dspr
    un "Как хочешь, любимый."
    hide un with dissolve
    "Лена заварила чай, достала печенье и села рядом со мной."
    show un smile pioneer close with dspr
    me "Вкусное."
    un "Да."
    "Мы допили чай и я прилёг."
    me "Оххх..."
    show un sad pioneer close with dspr
    un "Ты наверное устал, бедненький ты мой."
    me "Пожалуй."
    un "Семён."
    me "М?"
    un "Закрой глаза и расслабься."
    stop music fadeout 1
    stop ambience fadeout 2
    th "Надеюсь ты меня не убьёшь..."
    show blink
    play music music_list["i_dont_blame_you"] fadein 2
    "Я почувствовал как Лена начала расстёгивать мою рубашку и водить своими руками по моему торсу."
    th "Ну, не убила."
    "Я улыбнулся."
    "Лена сняла с меня шорты и наляглась на моего дружка своей грудью."
    "Я решил открыть глаза."
    scene cg d2_un_hentai_3
    hide blink
    show unblink
    "И не пожалел..."
    un "Я же говорила закрой глаза, ещё рано."
    me "Прости."
    show blink 
    un "Не открывай, пока я не скажу!"
    me "Хорошо. Не открою, пока не скажешь."
    "Лена помассировала мой член ещё пару минут и я кончил."
    un "Погоди секунду."
    me "Хорошо."
    "Лена пошуршала одеждой, я полагаю, полностью разделась."
    play sound ston2
    "И оседлала меня."
    un "Можешь открывать."
    scene cg d2_un_hentai
    hide blink 
    show unblink
    "Я увидел перед собой шикарную картину."
    th "Уж точно получше, чем ту которую я \"сотворил\"."
    "В этот момент я чувствовал, искреннею страсть и любовь Лены."
    "Алиса даже в подмётки не годиться по сравнению с Леной."
    th "Может, я влюбился?"
    th "Забавно.{w} Двое маньяков искренне полюбили друг друга.{w} Звучит как название какого-то дешевого американского сериала."
    scene bg black with dissolve
    "Через ещё минут 15, мы упали на кровать и молча лежали в обнимку."
    scene int_house_of_un_day with dissolve
    stop music fadeout 2
    play ambience ambience_int_cabin_day
    "..."
    show un smile naked close with dissolve
    un "Тебе понравилось?"
    me "Лен, я тебя люблю."
    show un smile2 naked close with dspr
    un "А я тебя в трижды больше."
    me "Ладно-ладно."
    play sound hihikane
    show un grin naked close with dspr
    "Лена победоносно хихикнула."
    un "..."
    me "Лен, можно я посплю, а то всю ночь, как ты говоришь \"творил\"."
    un "Можно, конечно.{w} А я буду оберегать твой сон."
    me "Спасибо Ленусь."
    show blink 
    $ renpy.pause(3, hard=True)
    "..."
    play sound sfx_dinner_jingle_speaker
    hide blink
    scene int_house_of_un_day 
    show unblink
    th "О, уже и завтрак! А то я такой голодный, что готов слона съесть."
    show un smile pioneer with dissolve
    un "Ты уже проснулся? Доброе утро, любимый!"
    me "Доброе, Лен."
    un "А я тебе одежду принесла, а то та вся в крови была."
    me "Спасибо, чтобы я без тебя делал!"
    un "Пойдём на обед?"
    me "Обед?"
    un "Ты так сладко спал, что я не хотела тебя будить."
    me "Ничего.{w} Да, сейчас пойдём, подожди только."
    "Я оделся в новую одежду."
    th "Ляпота..."
    un "Пошли?"
    me "Идём."
    scene bg black with dissolve
    "..."
    scene bg ugol_stolovoy_day with dissolve
    play ambience ambience_dining_hall_full fadein 2
    $ save_name = ('День 2. Обед.')
    "Мы с Леной пришли на обед и сели за столик в углу."
    show un smile pioneer at right with dissolve
    me "Приятного."
    un "Спасибо, тебе тоже."
    "..."
    me "Как думаешь скоро заметят пропажу Слави?"
    show un evil_smile pioneer at right with dspr
    un "Что я тебе уже не подхожу? К Славе тебя отправить?"
    me "Нет-нет, ни в коем случае, просто если её найдут у нас есть алиби?"
    show un normal pioneer at right with dspr
    un "У меня нету, у тебя не знаю. Думаю её найдут... где-то после обеда."
    me "И меня нету..."
    un "Тогда, скажем, что вместе ночевали."
    me "Ааа может, что-то другое?"
    un "А у тебя есть идеи?"
    me "..."
    un "Вот и всё."
    "..."
    play music Myuu_Fernweh fadein 3
    show dv sad pioneer at left with dissolve 
    dv "Семён?"
    "Алиса без разрешения, села к нам за стол."
    me "М?"
    "Промычал я, не отрываясь от пищи."
    dv "Ты меня помнишь? И почему все притворяются пионерами?"
    "Я аж поперхнулся.{w} И даже не от вопроса, а от, что она, может рассказать Лене про..."
    me "В смысле?"
    dv "В смысле, как мы с тобой и с Шуриком вчера бухали, а потом переспали."
    with vpunch
    show un rage pioneer at right with dspr
    un "ВЫ ЧТО?"
    th "Не было печали..."
    dv "А потом ещё Шурик проснулся и удивился, что он тут делает и начал нести какой-то пьяный бред про робота и пионерию. Я подумала, что у него из-за похмелья бред, но все, почему-то стали притворяться пионерами."
    th "И что мне ответить?"
    menu:
        "Сказать правду":
                                $ ubiv2_ochki += 2
                                $ dv3_ochki -= 2
        "Притвориться пионером":
            $ dv3_ochki += 2  
            $ ubiv2_ochki -= 2
    if dv3_ochki >= 2:
        jump somesing_new_ubivasha_good_rut
    else:
        jump somesing_new_ubivasha_bad_rut
    
label somesing_new_ubivasha_good_rut:
    $ save_name = ('День 2. Я - пионер!')
    me "Ты совсем с ума сошла? Чтобы я, с тобой... да не в жизни."
    dv "Да хрен с тобой, почему все притворяются пионерами?"
    me "Даже не знаю... Может потому, что мы находимся в пионерском лагере?"
    dv "Ч-что?..{w} И ты тоже..."
    show dv cry pioneer at left with dspr
    "Алиса расплакалась и убежала прочь."
    hide dv with dissolve
    un "Изволишь объясниться?!"
    me "Я понятия не имею о чём она говорит!"
    un "А что ты тогда делал возле дорожки в старый лагерь, там рядом как раз её домик!"
    me "Я ночью не мог уснуть, вышел погулять, нагнать сон, так сказать. Потом услышал крик и побежал на него."
    with vpunch
    me "И в конце концов, кому ты больше веришь, мне или этой умалишённой, которая напилась, так, что даже не помнит, что находится в пионер лагере!?"
    show un shy pioneer at right with dspr
    un "Да, ты прав, прости."
    stop music fadeout 1
    me "Прощаю."
    "..."
    stop ambience fadeout 3
    "Мы доели и пошли к выходу."
    play sound sfx_close_door_campus_1 
    scene bg ext_dining_door_day with dissolve
    play ambience ambience_camp_center_day
    "Однако нас на выходе остановила вожатая."
    show mt angry pioneer at cright with dissolve
    mt "Стоять!"
    "Мы остановились."
    show un normal pioneer at cleft with dissolve
    me "Что такое?"
    mt "Где вы были прошлой ночью?"
    th "Вот блин..."
    me "Какая разница..."
    "Я пожал плечами."
    show mt rage pioneer at cright with dspr
    mt "Такая! Вы знаете что пропала Славя?"
    me "Нет, не слышали."
    show mt scared pioneer at cright with dspr
    mt "Я отправилась её искать и...{w} нашла!"
    "Вожатая пыталась сдержать слёзы."
    me "Так это хорошо же."
    mt "Пойдёмте, я вам покажу."
    "Тихо сказала она."
    th "Вот влипли...{w} Ну, ладно, оправдание у нас, вроде как, есть, так что бояться, особо, нечего. Главное хорошо отыграть когда увидим её."
    "Я посмотрел на Лену."
    show un grin pioneer at cleft with dissolve
    "Она хитро, даже коварно, ухмыльнулась."
    "Я ухмыльнулся ей в ответ и мы пошли."
    scene bg ext_polyana_day with dissolve
    $ save_name = ('День 2. Картина маслом.')
    stop ambience fadeout 2
    "Вскоре мы вышли на ту самую поляну."
    show mt scared pioneer with dspr
    play music vintage_labeled_amys_dark_axe fadein 2
    mt "Там..."
    "Она показала за дерево."
    "Я сделал несколько шагов в ту сторону..."
    scene cg epilogue_mi_2 with dissolve
    "И снова увидел свой шедевр."
    th "Всё-таки Лена права, и вправду очень красивый вид."
    "..."
    th "И всё же, что происходит с сознанием куклы, когда она \"умирает\"?"
    th "Ах, да, какое там сознание... Это же такие же вещи как стол. Просто запрограммированные на движения. Прямо-таки как куклы."
    th "Куклы они и есть..."
    play sound krik_wom
    "Лена выглянула у меня из-за плеча и в ужасе заорала."
    th "Молодец.{w} Хорошая актёрская игра."
    "Лена даже смогла заплакать." 
    "Она бросилась в объятья Ольги Дмитриевны."
    th "А ведь пару часов назад, она была в таком же состоянии только подвижная."
    th "А может, это таки, был человек? В связи с последними событиями может даже и так...{w} Хотя, мне до одного места."
    th "Всё равно меня никто не накажет."
    th "Ведь ни мистического райцентра, ни мистической милиции не существует."
    "Я ещё немного полюбовался и вернулся назад."
    scene bg ext_polyana_day with dissolve
    show mt scared pioneer at right with dissolve
    show un cry pioneer at left with dissolve
    me "Кто это сделал?.."
    mt "Мне откуда знать!"
    me "..."
    mt "Во всём лагере алиби нет только у вас."
    th "Влипли таки..."
    show un cry pioneer close at left with dspr
    "Лена отстранилась от Ольги и начала хныкать уже на моем плече."
    me "Вы что, серьёзно думаете, что мы способны на... такое?!"
    "Я посмотрел на неё взглядом полным ненавистью."
    mt "Ну, нет..."
    "Ольга замялась."
    mt "Ну кто-то же это сделал!"
    me "Я бы сказал, что это дикие животные какие-то. Не знаю, волки, медведи."
    mt "Тут отродясь диких зверей не водилось..."
    me "То есть, по вашему, это сделал человек?!"
    mt "Ну а больше некому..."
    me "Нет, такого быть не может."
    "..."
    mt "В общем, надо звонить в милицию."
    me "Конечно надо! Пойдёмте!"
    stop music fadeout 2
    "..."
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening
    $ sunset_time()
    "Мы с Леной вышли на площадь."
    "Смеркалось."
    th "В прошлый раз я даже и не понял, насколько сильно я её разорвал."
    th "Да уж, человек в состоянии безумия обретает сверхсилу, хех."
    $ persistent.sprite_time = "sunset"
    show un normal pioneer with dissolve 
    un "Семён..."
    me "А?"
    show un shy pioneer with dspr
    un "А ты бы смог, убить кого-то за меня без причины."
    play sound laugh_male
    me "Лена, я же уже это сделал."
    show un evil_smile pioneer with dspr
    un "А ещё раз, смог бы?"
    me "Это приглашение?"
    un "Может быть..."
    "Мы молча сидели на скамейке в обнимку."
    show un smile3 pioneer with dspr
    un "Может, у меня сегодня переночуешь?"
    me "Давай. Только я приду когда Ольга Дмитриевна уснёт."
    show un normal pioneer with dspr
    un "Ладно..."
    "Мы ещё немного посидели и пошли по домам."
    stop ambience fadeout 2
    "..."
    $ save_name = ('День 2. Пропажа.')
    scene bg int_house_of_mt_night2 with dissolve
    play ambience ambience_int_cabin_night
    "..."
    $ persistent.sprite_time = "night"
    $ night_time()
    th "Странно, уже отбой как полтора часа, а Ольги всё нет."
    th "Хотя не мудрено, у неё тут как-никак пионерку жестоко убили."
    play sound sfx_door_squeak_light 
    "Я услышал как дверь немного приоткрылась."
    th "Неужели, блин!"
    "Однако, вопреки ожиданию никто не вошел."
    "Я подождал ещё несколько секунд, не выдержал и пошёл к двери."
    play sound sfx_open_door_strong
    "И рванул дверь со всей силы на себя."
    "Послышался приглушенный вскрик, и на пороге показалась Алиса."
    show dv scared pioneer with dissolve
    me "Что тебе надо?"
    "Раздражённо сказал я."
    show dv sad pioneer with dspr
    dv "Ульяна пропала." 
    th "Так вот зачем Лена меня позвала... Видимо не дождалась."
    show dv guilty pioneer with dspr
    dv "Так ладно ещё только Ульянка..."
    show dv cry pioneer with dspr
    dv "Я прошлась по домикам, всех кого знаю и никого не нашла."
    "Алиса заплакала."
    th "Действительно, Ольги и впрямь нету..."
    th "Лена постаралась?"
    th "Нет, не думаю."
    th "Без меня она, ничем таким глобальным не занималась бы."
    th "..."
    th "Тогда что?{w} Опять проделки лагеря?"
    "Я подошёл к часам и посмотрел время."
    "Почти полночь. Да, в такое время уже должны сидеть по домам."
    me "Пойдём выйдем?{w} На свежем воздухе подумаем."
    show dv sad pioneer with dspr
    dv "Угу..."
    stop ambience fadeout 2
    scene bg ext_house_of_mt_night_without_light
    "Мы вышли.{w} Я сел на ступеньки и задумался."
    show dv sad pioneer with dissolve
    "Алиса стояла рядом, страдальчески заломив руки, смотрела на луну."
    dv "Надо звонить в полицию."
    "Я еле сдержал смех."
    th "Ахахах, теперь у нас есть ещё и мистическая \"полиция\"."
    me "Не поможет."
    dv "И что нам тогда делать?"
    me "Думать."
    th "Но всё же тут что-то происходит. Не может же такого быть, чтобы Лена, в одиночку, весь отряд зарезала...{w} Или может?"
    "Вокруг нас царила спокойная летняя ночь - ни дуновение ветра, ни шелеста травы, ни шелеста листвы.{w} Ничего."
    "Лишь отблеск луны в домиках, редкие облака на ночном небе да непроглядная тьма."
    "Да такая, что если в неё долго всматриваться, кажется, что не ты смотришь в тьму, а что тьма смотрит в тебя."
    "И звуки кузнечиков!{w} Как же они меня достали!"
    th "Хотя бы тем, что их нет!{w} Сколько же времени я угробил, чтобы найти хоть одного...{w} Но их нигде нет!{w} Кажется, что звук прямиком из травы издаётся."
    th "Только того, находил, которого, Ульянка в начале цикла перед лицом Лены трясёт."
    show dv scared pioneer close with dspr
    dv "Слышишь?"
    "Алиса села рядом и прижалась ко мне. Она вся дрожала."
    me "Что?{w} И не так близко."
    show dv scared pioneer with dspr
    "Алиса так же дрожа отпрянула от меня."
    "Я прислушался."
    "Кажется, кто-то медленно шёл по дорожке в нашу сторону."
    "Разглядеть не удавалось, но шаги становились отчетливее."
    hide dv with dissolve
    "Я решил пойти посмотреть кто идёт."
    "Вскоре силуэт стал чётче. Небольшого роста, странная причёска, юбка..."
    th "Лена!"
    me "Лена!"
    show un scared pioneer far with dissolve
    "Что удивительно, Лена была напуганной."
    me "Ты за мной?"
    show un sad pioneer with dspr
    un "Я... думала ты тоже исчез..."
    th "Да... это точно не её рук дело..."
    me "Я тут.{w} И Алиса кстати. Пришла потому, что тоже никого не нашла."
    me "Пойдём."
    hide un with dissolve
    "Я отвёл её к Алисе."
    "Лена начала рассказывать."
    show un sad pioneer at cleft with dissolve
    show dv sad pioneer at cright with dissolve
    un "Я сидела в домике и ждала пока придёт Мику... а её всё нет... и я... а тут такое со Славей... и я..."
    "..."
    dv "Семён?"
    me "Да?"
    dv "Тебе не кажется, что в лагере слишком тихо?"
    "Я прислушался. Действительно, кроме этих проклятых звуков кузнечиков, больше никаких звуков."
    "Ну, то есть, вообще никаких!"
    me "Ну... да..."
    th "Обычно тихо... но не на столько!"
    th "Мда... на моей памяти такого точно ещё не было."
    th "Переброс меня с Алисой из одного лагеря в другой, настоящая Лена или Лена убийца, так теперь ещё все куклы исчезли."
    me "Ладно, давайте подумаем, что будем делать дальше."
    show un evil_smile pioneer at cleft with dspr
    "Лена уже хотела предложить расправиться с \"кое-кем\"..."
    play sound sfx_bush_leaves
    "...Но её прервал шорох кустов." 
    show un shocked pioneer with dspr:
        linear 1 xalign 0.75
    show dv scared pioneer with dspr:
        linear 1 xalign 1.25
    "..."
    show el smile pioneer at left with dissolve
    el "Ах, вот вы где!"
    "Этим шорохом оказался Электроник."
    "Казалось, его всё происходящее не особо волнует..."
    me "Не пугай ты так, девочек инфаркт схватит."
    show el scared pioneer at left with dspr
    el "Извините, да..."
    me "Чего пришёл?"
    el "Вы не видели Шурика?"
    me "Нет."
    el "Странно..."
    el "Да и слишком тихо как-то тут..."
    el "Нигде не горит свет, тишина..."
    me "Спасибо, что подметил! Мы то и не заметили!"
    me "Между прочим у нас тут весь лагерь пропал, сквозь землю провалился!"
    show el surprise pioneer at left with dspr
    el "Как?"
    me "А мне по чём знать!"
    
    
    return
    
label somesing_new_ubivasha_bad_rut:
    $ save_name = ('День 2. Не было печали...')
    me "Это было всего один раз, и то по пьяни!"
    with vpunch
    un "ДА Я ЕЁ У..."
    with vpunch
    me "ТИХО! Не надо кричать о своих планах на всю столовую."
    show un angry pioneer at right with dspr
    show un normal pioneer at right with dissolve
    dv "Да хрен с тобой, использовал уже, так использовал. Почему все притворяются пионерами?"
    me "Ты в наш фильм попала."
    show dv shocked pioneer at left with dspr
    dv "Ч-что..."
    show dv angry pioneer at left with dspr
    dv "И т-ты такой спокойный?"
    me "Да.{w} У меня же есть Лена."
    show dv cry pioneer at left with dspr
    dv "Д-да ты...{w} козлина."
    "Алиса заплакала и убежала."
    hide dv with dissolve
    "..."
    show un serious pioneer at right with dspr
    un "Не хочешь объясниться?"
    me "Я ещё тогда тебя не знал,{w} да и вообще она меня напоила, а потом соблазнила!"
    show un rage pioneer at right with dspr
    with vpunch
    un "Не знал?!{w} А кто знал?{w} Твой брат близнец?!"
    me "А если так?"
    un "Ты совсем с ума съехал?{w} Хотя, впрочем, не мне об этом говорить."
    me "..."
    show un evil_smile pioneer at right with dspr
    un "Ладно, сделаешь для меня, и для себя в первую очередь, кое-что, и считай что ты прощён."
    me "Что?"
    un "Потом,{w} всё потом."
    stop music fadeout 1
    me "Ладно..."
    th "Я догадываюсь..."
    "..."
    stop ambience fadeout 3
    "Мы доели и пошли к выходу."
    scene bg ext_dining_door_day with dissolve
    play sound sfx_close_door_campus_1 
    play ambience ambience_camp_center_day
    show mt angry pioneer at cright with dissolve
    "Однако нас на выходе остановила вожатая..."
    mt "Стоять!"
    "Мы остановились."
    show un normal pioneer at cleft with dissolve
    me "Что такое?"
    mt "Где вы были прошлой ночью?"
    th "Вот блин..."
    me "Какая разница..."
    "Я пожал плечами."
    show mt rage pioneer at cright with dspr
    mt "Такая! Вы знаете что пропала Славя?"
    me "Нет, не слышали."
    show mt scared pioneer at cright with dspr
    mt "Я отправилась её искать и...{w} нашла!"
    "Вожатая пыталась сдержать слёзы."
    me "Так это хорошо же."
    mt "Пойдёмте, я вам покажу."
    "Тихо сказала она."
    th "Вот влипли...{w} Ну, ладно, оправдание у нас, вроде как, есть, так что бояться, особо, нечего. Главное хорошо отыграть когда увидим её."
    "Я посмотрел на Лену."
    show un grin pioneer at cleft with dissolve
    "Она хитро, даже коварно, ухмыльнулась."
    "Я тоже ухмыльнулся ей и мы пошли."
    scene bg ext_polyana_day with dissolve
    $ save_name = ('День 2. Картина маслом.')
    stop ambience fadeout 2
    "Вскоре мы вышли на ту самую поляну."
    show mt scared pioneer with dspr
    play music vintage_labeled_amys_dark_axe fadein 2
    mt "Там..."
    "Она показала за дерево."
    "Я сделал несколько шагов в ту сторону..."
    scene cg epilogue_mi_2 with dissolve
    "И снова увидел свой шедевр."
    th "Всё-таки Лена права, и вправду очень красивый вид."
    "..."
    th "И всё же, что происходит с сознанием куклы, когда она \"умирает\"?"
    th "Ах, да, какое там сознание... Это же такие же вещи как стол. Просто запрограммированные на движения. Прямо-таки как куклы."
    th "Куклы они и есть..."
    play sound krik_wom
    "Лена выглянула у меня из-за плеча и в ужасе заорала."
    th "Молодец.{w} Хорошая актёрская игра."
    "Лена даже смогла заплакать." 
    "Она бросилась в объятья Ольги Дмитриевны."
    th "А ведь пару часов назад, она была в таком же состоянии только подвижная."
    th "А может, это таки, был человек? В связи с последними событиями может даже и так...{w} Хотя, мне до одного места."
    th "Всё равно меня никто не накажет."
    th "Ведь ни мистического райцентра, ни мистической милиции не существует."
    "Я ещё немного полюбовался, нацепил на себя испуганное лицо и вернулся назад."
    scene bg ext_polyana_day with dissolve
    show mt scared pioneer at right with dissolve
    show un cry pioneer at left with dissolve
    me "Кто это сделал?.."
    mt "Мне откуда знать!"
    me "..."
    mt "Во всём лагере алиби нет только у вас."
    th "Влипли таки..."
    show un cry pioneer close at left with dspr
    "Лена отстранилась от Ольги и начала хныкать уже на моем плече."
    me "Вы что, серьёзно думаете, что мы способны на... такое?!"
    "Я посмотрел на неё взглядом полным ненавистью."
    mt "Ну, нет..."
    "Ольга замялась."
    mt "Ну кто-то же это сделал!"
    me "Я бы сказал, что это дикие животные какие-то. Не знаю, волки, медведи."
    mt "Тут отродясь диких зверей не водилось..."
    me "То есть, по вашему, это сделал человек?!"
    mt "Ну а больше некому..."
    me "Нет, такого быть не может."
    "..."
    mt "В общем, надо звонить в милицию."
    me "Конечно надо! Пойдёмте!"
    stop music fadeout 2
    "..."
    scene bg ext_square_sunset with dissolve
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    play ambience ambience_camp_center_evening
    "Мы с Леной вышли на площадь."
    "Смеркалось."
    th "В прошлый раз я даже и не понял, насколько сильно я её разорвал."
    th "Да уж, человек в состоянии безумия обретает сверхсилу, хех."
    show un evil_smile pioneer with dissolve
    un "Видел как эта сучка плакала?"
    me "Да... весело..."
    "Хмыкнул я."
    "..."
    show un normal pioneer with dspr 
    un "Семён..."
    me "А?"
    show un shy pioneer with dspr
    un "А ты бы смог, убить кого-то за меня без причины."
    play sound laugh_male
    me "Лена, так я уже."
    show un evil_smile pioneer with dspr
    un "А ещё раз, смог бы?"
    me "Думаю, что да."
    un "Поня-я-я-ятно."
    "Мы молча сидели на скамейке в обнимку."
    show un smile3 pioneer with dspr
    un "Может, у меня сегодня переночуешь?"
    me "Давай. Только я приду когда Ольга Дмитриевна уснёт."
    show un normal pioneer with dspr
    un "Ладно..."
    "Мы ещё немного посидели и пошли по домам."
    stop ambience fadeout 2
    scene bg black with dissolve
    "..."
    $ save_name = ('День 2. Пропажа.')
    scene bg int_house_of_mt_night with dissolve
    play ambience ambience_int_cabin_night
    "..."
    th "Странно, уже отбой как полтора часа, а Ольги всё нет."
    th "Хотя не мудрено, у неё тут как-никак пионерку жестоко убили."
    play sound sfx_door_squeak_light 
    "Я услышал как дверь немного приоткрылась."
    th "Неужели, блин!"
    "Однако, вопреки ожиданию никто не вошел."
    "Я подождал ещё несколько секунд, не выдержал и пошёл к двери."
    play sound sfx_open_door_strong
    "И рванул дверь со всей силы на себя."
    "Послышался приглушенный вскрик, и на пороге показалась Алиса."
    show dv scared pioneer with dissolve
    me "Чё тебе надо?"
    "Раздражённо сказал я."
    show dv sad pioneer with dspr
    dv "Ульяна пропала." 
    th "Так вот зачем Лена меня позвала... Видимо не дождалась."
    show dv guilty pioneer with dspr
    dv "Так ладно ещё только Ульянка..."
    show dv cry pioneer with dspr
    dv "Я прошлась по домикам, всех кого знаю и никого не нашла."
    "Алиса заплакала."
    th "Действительно, Ольги и впрямь нету..."
    th "Лена постаралась?"
    th "Нет, не думаю."
    th "Без меня она, ничем таким глобальным не занималась бы."
    th "..."
    th "Тогда что?{w} Опять проделки лагеря?"
    "Я подошёл к часам и посмотрел время."
    "Почти полночь. Да, в такое время уже должны сидеть по домам."
    me "Пойдём выйдем?{w} На свежем воздухе подумаем."
    show dv sad pioneer with dspr
    dv "Угу..."
    stop ambience fadeout 2
    scene bg ext_house_of_mt_night_without_light
    "Мы вышли.{w} Я сел на ступеньки и задумался."
    show dv sad pioneer with dissolve
    "Алиса стояла рядом, страдальчески заломив руки, смотрела на луну."
    dv "Надо звонить в полицию."
    "Я еле сдержал смех."
    th "Ахахах, теперь у нас есть ещё и мистическая \"полиция\"."
    me "Не поможет."
    dv "И что нам тогда делать?"
    me "Думать."
    th "Но всё же тут что-то происходит. Не может же такого быть, чтобы Лена, в одиночку, весь отряд зарезала...{w} Или может?"
    "Вокруг нас царила спокойная летняя ночь - ни дуновение ветра, ни шелеста травы, ни шелеста листвы.{w} Ничего."
    "Лишь отблеск луны в домиках, редкие облака на ночном небе да непроглядная тьма."
    "Да такая, что если в неё долго всматриваться, кажется, что не ты смотришь в тьму, а что тьма смотрит в тебя."
    "И звуки кузнечиков!{w} Как же они меня достали!"
    th "Хотя бы тем, что их нету!{w} Сколько же времени я угробил, чтобы найти хоть одного...{w} Но их нигде нет!{w} Кажется, что звук прямиком из травы издаётся."
    th "Только того, находил, которого, Ульянка в начале цикла перед лицом Лены трясёт."
    show dv scared pioneer close with dspr
    dv "Слышишь?"
    "Алиса села рядом и прижалась ко мне. Она вся дрожала."
    me "Что?{w} И не так близко."
    show dv scared pioneer with dspr
    "Алиса так же дрожа отпрянула от меня."
    "Я прислушался."
    "Кажется, кто-то медленно шёл по дорожке в нашу сторону."
    "Разглядеть не удавалось, но шаги становились отчетливее."
    hide dv with dissolve
    "Я решил пойти посмотреть кто идёт."
    "Вскоре силуэт стал чётче. Небольшого роста, странная причёска, юбка..."
    th "Лена!"
    me "Лена!"
    show un scared pioneer far with dissolve
    "Что удивительно, Лена была напуганной."
    me "Ты за мной?"
    show un normal pioneer with dspr
    un "Тут это...{w} все исчезли..."
    th "Да... это точно не её рук дело..."
    me "Я тут.{w} И Алиса кстати. Пришла потому, что тоже никого не нашла."
    me "Пойдём."
    hide un with dissolve
    "Я отвёл её к Алисе."
    "Лена начала рассказывать."
    show un sad pioneer at cleft with dissolve
    show dv sad pioneer at cright with dissolve
    un "Я сидела в домике и ждала пока придёт Мику... а её всё нет... и я... а тут такое со Славей... и я..."
    "..."
    dv "Семён?"
    me "Да?"
    dv "Тебе не кажется, что в лагере слишком тихо?"
    "Я прислушался. Действительно, кроме этих проклятых звуков кузнечиков, больше никаких звуков."
    "Ну, то есть, вообще никаких!"
    me "Ну... да..."
    th "Обычно тихо... но не на столько!"
    th "Мда... на моей памяти такого точно ещё не было."
    th "Переброс меня с Алисой из одного лагеря в другой, настоящая Лена или Лена убийца, так теперь ещё все куклы исчезли."
    me "Ладно, давайте подумаем, что будем делать дальше."
    show un evil_smile pioneer at cleft with dspr
    "Лена уже хотела предложить расправиться с \"кое-кем\"..."
    play sound sfx_bush_leaves
    "...Но её прервал шорох кустов." 
    show un shocked pioneer with dspr:
        linear 1 xalign 0.75
    show dv scared pioneer with dspr:
        linear 1 xalign 1.25
    "..."
    show el smile pioneer at left with dissolve
    el "Ах, вот вы где!"
    "Этим шорохом оказался Электроник."
    "Казалось, его всё происходящее не особо волнует..."
    me "Не пугай ты так, девочек инфаркт схватит."
    show el scared pioneer at left with dspr
    el "Извините, да..."
    me "Чего пришёл?"
    el "Вы не видели Шурика?"
    me "Нет."
    el "Странно..."
    el "Да и слишком тихо как-то тут..."
    el "Нигде не горит свет, тишина..."
    me "Спасибо, что подметил! Мы то и не заметили!"
    me "Между прочим у нас тут весь лагерь пропал, сквозь землю провалился!"
    show el surprise pioneer at left with dspr
    el "Как?"
    me "А мне по чём знать!"
    
    return
    
label somesing_new_dvache_rut_day2:
    th "Ну нет, вдруг я задержусь из-за чего нибудь, Алиса проснётся, а меня нет. Неудобно выйдет...{w} Особенно для Шурика..."
    th "Да и даже если я не усну, то полежать в обнимку с голой девушкой поприятнее будет, чем гулять."
    th "Так что, решено! Остаюсь на месте."
    stop ambience fadeout 3
    "Немного поворочившись, я уснул."
    window hide dissolve
    show blink
    $ renpy.pause(1.5, hard=True)
    stop sound_loop fadeout 3
    scene bg black
    with fade3
    $ backdrop = "days"
    $ new_chapter(2, "День 2. Старый-добрый лагерь.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "days"
    $ renpy.pause(1, hard=True)
    $ persistent.sprite_time = 'day'
    $ day_time()
    pause 1.5
    window show dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Проснулся я от крика."
    play sound vizg_wom
    us "А-а-а-а-а-а-а!"
    "Я нехотя разомкнул глаза."
    window hide dissolve
    hide blink
    scene bg int_house_of_dv_day
    show unblink
    pause 0.5
    window show dissolve
    show sh surprise pioneer2 at right 
    show us surp2 pioneer at fright
    hide unblink
    with dissolve
    play music music_list["glimmering_coals"] fadein 3
    "Как только резкость моих глаз стала приемлимой для того, чтобы что-то увидеть, я узрел довольно интересную картину."
    "Ульяна била кулаками по груди нашего спящего оператора.{w} Ну, Шурика то бишь."
    sh "А-а-а? Что?"
    "Шурик проснулся в полном недоумении, хотя нет, даже в шоке, оттого что тут произошло и оттого, что он в центре событий."
    show sh serious pioneer2 at right with dspr
    sh "Что? Что я тут делаю?..{w} Я же вчера ходил за деталями, а потом...{w} не помню..."
    show dv laugh lif at fleft with dissolve
    show us normal pioneer with dspr
    play sound smeh_wom
    dv "А-ха-ха, Шурик... за-за какими дета-деталями!"
    "Алиса чуть ли не разрывалась от смеха."
    sh "Так, а что я тут делаю?!"
    dv "Ну Шурик... ну ты даёшь..."
    show sh normal pioneer2 at right with dspr
    "Шурик вопросительно взглянул на неё." 
    show dv smile lif with dspr
    dv "Мы вчера вечером пьянку устроили!"
    show sh surprise pioneer2 at right with dspr
    sh "{b}И я согласился?!{/b}"
    dv "Ты нам помогал её устроить!"
    "Шурик удивлённо замолк, видимо пытался вспомнить, что вчера произошло."
    "..."
    sh "Ладно, тогда я не на линейку пойду, а пойду в клуб, прикройте меня перед Ольгой Дмитриевной."
    me "Э-э-э...{w} окей?.."
    hide sh with dissolve
    play ambience ambience_camp_center_day fadein 3
    play sound sfx_open_door_2
    "Шурик кивнул и удалился из домика."
    "..."
    show dv surprise lif with dspr
    dv "Так стоп… А ты что тут делаешь?"
    show us dontlike pioneer with dspr
    us "Если бы кто-то меня хотя бы предупредил, то тогда бы меня тут не было!"
    dv "Так тебя не было, когда мы начинали! Ты вообще должна была приехать только через пару дней!"
    show us sad pioneer with dspr
    us "О-о-о-о...{w} Совсем допилась..."
    hide us with dissolve
    play sound sfx_open_door_1
    stop music fadeout 3
    "Ульянка тут же пулей выскочила на улицу."
    th "\"Мда...\" - подумал Штирлиц."
    th "..."
    th "И что это сейчас было?.."
    dv "И что это сейчас было?.."
    me "Самому б знать...{w} но стоит пойти разобраться."
    dv "И куда пойдём?"
    me "Ну, не знаю... {w} Что ты обычно с утра делаешь?"
    dv "Я имела ввиду куда пойти чтобы найти Ульянку."
    show dv normal lif  with dspr
    me "А-а-а-а..."
    me "Ну...{w} может умываться пошла?"
    dv "Тогда пошли посмотрим."
    hide dv with dissolve
    "Я вместе с Алисой, оделся и вышел из домика."
    window hide dissolve
    play sound sfx_open_door_2
    scene bg ext_house_of_dv_day with dissolve
    pause 2.0
    scene bg black with dissolve
    pause 2.0
    scene bg ext_washstand_day with dissolve
    window show dissolve
    "Мы пришли."
    play music music_list["my_daily_life"] fadein 3
    "Ульянки тут не было, но была Мику."
    show mi normal pioneer far at right with dissolve
    th "Тьфу... Маша!"
    "Алиса окликнула Машу."
    show dv normal pioneer at left with dissolve
    dv "Эй, Маш! Не знаешь, где Ульянка может ошиваться?"
    hide mi with dissolve
    "Но она никак не отреагировала и молча ушла."
    dv "Вот зараза!"
    me "Ага..."
    dv "Хотя это в её стиле! Сразу видно! Машку никто не подменял!"
    th "В отличии от Шурика..."
    scene bg ext_washstand2_day with dissolve
    play sound sfx_open_water_sink
    $ renpy.pause(1, hard=True)
    play sound_loop sfx_water_sink_stream loop
    "Я принялся умываться."
    "Вода, как всегда, ледяная."
    th "Хотя бы что-то осталось неизменным..."
    "Пару раз брызнув себе в лицо водой, или, точнее, немного попытав себя водой, я закончил нехитрые водные процедуры." 
    stop sound_loop
    play sound sfx_close_water_sink
    scene bg ext_washstand_day
    show dv normal pioneer
    with dissolve 
    "Алиса тоже закончила умываться, через мгновение вдали послышался горн из столовой…"
    play sound sfx_dinner_horn_processed
    stop music fadeout 2
    show dv surprise pioneer with dspr
    dv "Что? Они смогли поставить горн!?"
    me "В смысле?"
    "Я не сразу понял Алису, но через несколько секунд до меня дошло..."
    play music music_list["no_tresspassing"] fadein 1
    th "Твою мать!" with vpunch
    th "Я же не в обычном лагере!" with hpunch
    th "Так откуда здесь горн? {w} И Шурик... И Мику не отозвалась на имя - Маша..."
    me "Чёрт..."
    show dv scared pioneer with dspr
    dv "Что?"
    me "Похоже, мы попали в пионерлагерь \"Совёнок\"..."
    dv "Что!?"
    me "Что слышала!"
    dv "Ты что за бред несёшь?! То Шурик, теперь вот ты..."
    me "Ну хорошо, пошли в столовую - проверим."
    show dv sad pioneer with dspr
    stop music fadeout 5
    dv "Пошли."
    "С грустным осадком сказала Алиса."
    "..."
    scene bg ext_dining_door_day with dissolve
    "Мы подошли ко входу в столовую."
    me "Ну что, готова поделить свою жизнь на до и после?"
    show dv dontlike pioneer with dissolve
    dv "Харе чушь нести! Открывай давай!"
    "Раздражённо сказала Алиса."
    me "Ну как хочешь..."
    "Я открыл дверь, и мы зашли."
    play sound sfx_open_door_campus_1 
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 3
    "Столовая была битком набита пионерами."
    show dv shocked pioneer with dissolve
    dv "Твою мать..."
    me "И как? До сих пор мне не веришь?"
    dv "Верю... Я поверила."
    th "А?{w} Серьёзно что-ль?"
    show dv laugh pioneer with dspr
    "Алиса несколько секунд выдерживала молчание и во всю расхохоталась."
    play sound smeh_wom
    dv "Ну ты и кадр! Массовку завезли пока я дрыхла! Так вот зачем горн поставили!"
    th "Ага, конечно...{w} {i}серьёзно...{/i}{w} мда..."
    th "Ладно, успеет ещё поменять своё мнение."
    "Мы взяли завтрак и присели за один стол." 
    scene bg ugol_stolovoy_day with dissolve
    show dv smile pioneer at cright with dissolve
    dv "Наконец! Наконец-то нормальная еда!"
    me "Ещё один аргумент в пользу моей версии."
    show dv normal pioneer at cright with dspr
    dv "Да заткнись ты уже, а?"
    me "Лады."
    dv "Москвичи блин..."
    play music music_list["your_bright_side"] fadein 9
    "..."
    show un normal pioneer at cleft with dissolve
    "Через некоторое время к нам подсела Лена."
    dv "О, Лен! И ты уже сюда приех..."
    "Я наступил ей на ногу."
    show dv surprise pioneer at cright with dspr
    dv "Ауч! Ты чего?"
    "Я нахмурился."
    show dv normal pioneer at cright with dspr
    dv "Ладно-ладно, поиграю по твоим правилам."
    show un evil_smile with dspr
    un "Вы про что?"
    dv "Лен?"
    show un shy pioneer with dspr
    un "Что?.."
    dv "Ничего..."
    "..."
    show un normal pioneer with dspr
    un "Кстати, вы слышали про то, что Славя пропала?"
    dv "Кто?"
    th "Что? Такого же не было... выходит, что и {i}это{/i} не обычный лагерь?"
    un "Славя..."
    me "Нет, не слышали."
    un "Как думаете, куда она могла пропасть?"
    me "Не знаю, может быть в лесу заплутала? Уж очень она любит туда одна ходить."
    un "Не знаю..."
    stop music fadeout 3
    stop ambience fadeout 3
    "..."
    "Мы с Алисой доели, и, попрощавшись с Леной, направились в сторону площади."
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_away_day with dissolve
    window hide dissolve
    pause 1.0
    scene bg ext_square_day with dissolve
    window show dissolve
    show dv sad pioneer with dissolve
    play music music_list["goodbye_home_shores"] fadein 3
    dv "И куда теперь?.."
    $ save_name = ('День 2. Игра на эстраде.')
    me "А ты умеешь на гитаре играть?"
    show dv smile pioneer with dspr
    dv "Спрашиваешь!"
    "Алиса заметно оживилась, а в глазах загорелся огонёк."
    me "Тогда пойдём, на сцену поиграем."
    dv "А ты что, умеешь?"
    me "Умею."
    dv "А чего тогда не рассказывал?"
    me "Неважно. Пошли уже."
    dv "На сцену?"
    me "В муз-клуб сначала, за гитарой."
    dv "Так там же ничего не..."
    "..."
    dv "Ах да, тут же теперь \"пионерский лагерь\"  ,да?"
    me "Вот ты сейчас шутишь, а потом…. " 
    "Я не успел договорить фразу, как Алиса меня перебила."
    show dv sadness pioneer with dissolve
    dv "Слушай потом будет потом, я не хочу сейчас об этом думать... и верить в это не хочу."
    me "Ладно, пошли тогда к Мику."
    show dv surprise pioneer with dspr
    dv "Куда?"
    me "Ты сценарий читала?"
    show dv normal pioneer with dspr
    dv "А, поняла."
    scene bg ext_musclub_near_day with dissolve
    "Через пару минут, мы уже стояли перед музыкальным клубом."
    play sound sfx_knock_door2 
    "Я постучался."
    mi "Да-да, заходите!"
    play ambience ambience_music_club_day fadein 2
    play sound sfx_open_door_1 
    scene bg int_musclub_day with dissolve
    show mi smile pioneer at right 
    show dv normal pioneer at cleft 
    with dissolve
    mi "Ой, Алиса! Семён! А вы пришли ко мне в клуб записаться? Или вы пришли меня послушать? На чём вы хотите, чтобы я сыграла? На пианино или может на..."
    show dv surprise pioneer at cleft with dspr
    me "Стой-стой-стой, Мику!"
    show mi serious pioneer with dspr
    mi "Ой, простите, я опять вас заболтала..."
    me "Ничего."
    show mi normal pioneer with dspr
    mi "Так, а зачем вы, тогда, зашли?"
    me "Мы хотим поиграть на гитаре на сцене. Сможешь нам дать две гитары?"
    mi "Конечно-конечно, а вам электро или акустику? Хотя стойте… я смогу дать только одну акустику или одну электро гитару, а хотя могу обе сразу! Но если вы буд..."
    me "Стой!{w} Опять ты не туда уходишь. Дай нам те, которые можешь."
    show mi upset pioneer with dspr
    mi "Простите...{w} секунду."
    play sound sfx_open_door_2
    hide mi with dissolve
    "..."
    play sound sfx_close_door_1 
    show mi smile pioneer at right with dissolve
    "Мику зашла в кладовку, покопалась там пару минут и дала нам гитары, струны и медиаторы."
    mi "Вот. Хорошей вам игры!"
    dv "С-спасибо..."
    "Алиса по всей видимости не смогла успеть проследить за нитью разговора."
    play ambience ambience_camp_center_day fadein 3
    play sound sfx_close_door_1 
    scene bg ext_musclub_near_day with dissolve
    "Когда мы покинули логово этого разговорчивого музыкального чуда, Алиса с удивлением спросила:"
    show dv surprise pioneer with dissolve
    dv "И как ты только с ней разговаривал?.."
    me "Привык."
    show dv grin pioneer with dspr
    dv "Когда успел?"
    me "Пошли давай. А то до обеда так и не дойдём."
    show dv smile pioneer with dspr
    "..."
    scene bg ext_stage_normal_day with dissolve
    stop music fadeout 3
    "Сразу как мы подошли, Алиса выхватила у меня акустическую гитару, и хотела уже залезть на эстраду."
    me "Эй! А настроить?"
    dv "Блин."
    me "Давай сюда."
    "Я немного подшаманил над гитарой, и она стала звучать нормально."
    show dv normal pioneer with dissolve
    me "Принимай!"
    dv "Агась."
    dv "И кто первый?"
    me "Давай ты."
    show dv smile pioneer with dspr
    dv "Ноу проблэм."
    "Cказала Алиса и оживленно закивала."
    "Забравшись на сцену, она начала бегло перебирала струны." 
    th "Наверно вспоминает как играть..."
    "Я сел прямо на краю сцены, устроившись рядом с Алисой." 
    "Через ещё пару секунд, закончивши свой перебор, она начала своё выступление."
    "{b}Сейчас играет: Король и Шут - Кукла колдуна (cover by evisnep).{/b}"
    play music kukla_kolduna fadein 3
    stop ambience fadeout 3
    scene cg alisa_day_igraet with dissolve
    "..."
    dv "Тёмный, мрачный коридор,{w} я на цыпочках, как вор..." 
    dv "Пробираюсь, чуть дыша,{w} чтобы не спугнуть..." 
    dv "Тех, кто спит уже давно,{w} тех, кому не всё равно...{w} в чью я комнату тайком желаю заглянуть..."
    dv "Чтобы увидеть..."
    dv "Как бессонница в час ночной...{w} меняет, нелюдимая, облик твой."
    dv "Чьих невольница ты идей?"
    dv "Зачем тебе охотиться на людей?"
    "..."
    dv "Крестик на моей груди...{w} на него ты погляди..."
    dv "Что в тебе способен он...{w} резко изменить?"
    dv "Много книжек я читал, много фокусов видал..."
    dv "Свою тайну от меня..."
    dv "Не пытайся скрыть!"
    dv "Я это видел!"
    dv "Как бессонница в час ночной...{w} меняет, нелюдимая, облик твой."
    dv "Чьих невольница ты идей?"
    dv "Зачем тебе охотиться на людей?"
    dv "Очень жаль, что ты тогда...{w} не поверить не смогла..." 
    dv "В то, что новый твой приятель{w} не такой, как все!"
    dv "Ты осталась с ним вдвоём...{w} не зная ничего о нём..." 
    dv "Что для всех опасен он..." 
    dv "Наплевать тебе!" 
    dv "И ты попала..."
    dv "К настоящему колдуну!"
    dv "Он загубил таких, как ты,{w} не одну!"
    dv "Словно куклой и в час ночной..."
    dv "Теперь он может управлять тобой!"
    "..."
    stop music fadeout 5
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    th "Хах, иронично, что она поёт про кукл здесь, в этом лагере."
    play sound sfx_simon_applause 
    me "Нехило!"  
    show dv smile pioneer close with dissolve
    dv "А ты чего ожидал?!" 
    me "Не меньшего."
    dv "А то!"
    me "Ладно, теперь я."
    "Я решил, что буду играть на электрогитаре."
    show dv smile pioneer far with dissolve
    "Когда я подключив её, Алиса спрыгнула со сцены и села на лавочку."
    dv "Ну...{w} удиви!"
    me "Не сомневайся."
    stop ambience 
    scene cg Semon_electrogitara with dissolve
    with dissolve
    "{b}Сейчас играет - _ _ (cover by _).{/b}"
    "Текст песни"
    scene bg ext_stage_normal_day 
    show dv smile pioneer
    with dissolve
    me "Ну как?"
    show dv shy pioneer with dissolve
    dv "А ты не так уж и плох..."
    me "Спасибо!"
    "Я покланялся и спрыгнул к Алисе."
    show dv smile pioneer with dissolve
    dv "Ты где так научился?"
    me "Ци...{w} Годы практики!"
    me "А ты?"
    show dv dontlike pioneer with dspr
    dv "Какая тебе разница?.."
    me "Мне интересно о тебе узнать."
    dv "Зачем?"
    th "И правда? Зачем мне это?"
    "..."
    me "Чего ты так вспылила? Я же просто спросил."
    show dv sadness pioneer with dspr
    dv "Извини..."
    "Алиса резко успокоилась."
    me "Так всё же? Расскажешь или нет?"
    dv "Ладно уж...{w} слушай."
    me "Весь во внимании."
    show dv sad pioneer with dspr
    stop ambience fadeout 3
    play music sdl_tpinf_whitecoma fadein 4
    $ save_name = ('День 2. Откровение Алисы.')
    dv "Мои родители умерли когда мне было ещё 7.{w} После этого я попала в дет. дом."
    dv "Меня удочерил один... {w} подонок."
    dv "Я каждый раз убегала из дому, перед тем как он вернётся с работы, дабы не видется с... {w} ним."
    dv "В очередной раз, когда я убежала в соседнем дворе я увидела бабушку, играющую на гитаре. Она играла какую-то красивую мелодию, от которой на душе становилось легко."
    dv "Я слушала её и загорелась идеей научиться играть так же."
    dv "Ведь отдаться музыке и играть во дворах, это куда лучше, чем просто бесцельно ходить по улице или...{w} торчать с ним."
    dv "Я потратила все свои сбережения на хлипенькую гитару и начала ходить в тот двор тренироваться."
    show dv sad_smile pioneer with dspr
    dv "В один вечер меня заметила та бабуля, она не вытерпела слушать то, как я насилую гитару, взяла меня за руку и утащила к себе в квартиру."
    dv "Она начала меня учить простым аккордам и за первый же вечер я смогла сыграть простенькую мелодию."
    dv "Через пару месяцев я уже смогла прилично научиться играть на гитаре. Эта бабушка даже иногда брала меня с собой на свою вечернюю игру."
    dv "Ещё через месяца четыре, я уже свободно играла на акустической гитаре. Поэтому эта бабушка начала меня учить играть на своей электрогитаре."
    "Она пару секунд молчала и в заключение добавила:"
    show dv sad pioneer with dspr
    dv "Как-то так."
    "..."
    me "Вот оно как..."
    play sound sfx_dinner_horn_processed
    show dv sadness pioneer with dspr
    stop music fadeout 8
    dv "Ладно, пошли на обед?"
    me "Ну, пошли чтоль..."
    stop ambience fadeout 2 
    scene bg ugol_stolovoy_day with dissolve
    $ save_name = ('День 2. Обед с Мику.')
    play ambience ambience_dining_hall_full fadein 3
    show dv normal pioneer at cleft with dissolve
    "Зайдя в столовую, мы молча взяли по одному подносу и сели за столик в углу."
    "Нависла неловкая пауза."
    "Однако её прервала Мику."
    show mi smile pioneer at cright with dissolve
    mi "Можно к вам подсесть, у вас один свободный столик, ну то есть он не один, в столовой их-то много, а у вас он свободный, хотя в столовой много свободных столов, но из моих знакомых только у вас."
    show dv surprise pioneer at cleft with dissolve
    "Алиса аж поперхнулась от нахлынувшего на неё словесного потока."
    th "Ещё привыкнет... хотя я так-то и сам ещё не до конца привык... не смотря на мои..."
    th "..."
    th "А чёрт их знает сколько этих циклов..."
    show dv normal pioneer at cleft with dspr
    me "Садись."
    mi "Спасибо-спасибо!"
    "..."
    mi "Семён, как тебе игра Алисы?"
    me "Понравилась."
    "Алиса в этот момент, как мне показалось, немного покраснела."
    show dv shy2 pioneer with dspr
    dv "А сам-то?"
    me "А что я?"
    show dv shy pioneer at cleft with dspr
    dv "Т-ты тоже красиво играешь."
    "Алиса ещё больше засмущалась."
    "За столом воцарилась тишина."
    "Казалось, что Алиса хотела убежать, провалиться под землю, испариться, что угодно только чтобы не быть за нашим столом."
    "Наконец Мику удосужилась прервать тишину."
    show mi sad pioneer at cright with dissolve
    mi "А вы слышали? Славя пропала, ещё со вчерашнего вечера."
    show dv sad pioneer at cleft with dspr
    me "Слышали-слышали."
    mi "Как думаете, она в порядке?"
    me "Не знаю."
    dv "Надеюсь..."
    "..."
    hide mi
    hide dv 
    stop ambience fadeout 3
    with dissolve
    "Мы с Алисой доели и хотели было пойти на эстраду..." 
    play sound sfx_close_door_campus_1 
    scene bg ext_dining_door_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    play music music_list["trapped_in_dreams"] fadein 3
    "Но на крыльце нас остановила Ольга Дмитриевна..."
    show mt angry pioneer with dissolve
    $ save_name = ('День 2. Твою мать...')
    mt "Стоять!"
    me "Что такое?"
    mt "Где вы были прошлой ночью?"
    th "Блин..."
    me "Какая разница..."
    "Я пожал плечами."
    mt "Такая! Вы знаете, что пропала Славя?"
    me "Ну да, слыхали."
    show mt scared pioneer with dspr
    mt "Я отправилась её искать и... {w} нашла!"
    "Вожатая пыталась сдержать слёзы."
    me "Так это хорошо же."
    mt "Пойдёмте, я вам покажу."
    "Тихо сказала вожатая и пошла."
    stop ambience fadeout 3
    stop music fadeout 3
    "Ну а мы пошли за ней."
    scene bg ext_polyana_day with dissolve
    play ambience ambience_forest_day fadein 3
    "Вскоре мы вышли на какую-то поляну."
    mt "Там..."
    "Она показала за дерево."
    "Я сделал несколько шагов в ту сторону..."
    stop ambience fadeout 3
    play music music_list["scarytale"] fadein 4
    "И увидел..."
    scene cg epilogue_mi_2 with dissolve
    th "Твою мать..."
    "Увидел разорванную на куски Славю."
    th "Кто... как... что?.."
    "Все мои мысли путались. Выловить хотя бы одну не представлялось возможным."
    "Алиса, увидев мой шок заинтересовалась, что же я увидел. Она зашагала в мою сторону."
    me "Стой! Не смотри!"
    play sound krik_wom
    "Алиса не послушалась, выглянула у меня из-за плеча и в ужасе заорала."
    "Меня, конечно, напрягала картина, разорванной на куски Слави, но куда больше меня напрягал то факт - что {i}это что-то новенькое{/i}."
    th "Только вот если это теперь будет всегда... терпеть {b}такие циклы{/b} ещё хуже, чем было раньше."
    "Алиса зарыдала." 
    "Она бросилась в объятья Ольги Дмитриевны."
    "Наконец, я смог выловить хоть одну стоящую мысль."
    th "Кто это сделал или как это произошло?"
    th "Может, это был какой-нибудь зверь?{w} Нет, сразу отпадает, их ведь тут никогда не было.{w} Или, может, это был человек?{w} В связи с последними событиями возможно, что кто-то из пионеров стал жестоким убийцей." 
    th "..."
    th "И ведь милиция не приедет -  мистического райцентра не существует."
    "Я ещё немного осмотрел место убийства и вернулся назад."
    scene bg ext_polyana_day with dissolve
    me "Кто это сделал?"
    show mt scared pioneer
    show dv cry pioneer at left
    with dissolve
    mt "Мне откуда знать!"
    mt "Во всём лагере алиби нет только у вас."
    show dv cry pioneer close at left with dissolve
    "Алиса отстранилась от Ольги и начала хныкать уже на моем плече."
    me "Есть у нас алиби! И вообще!{w} Вы что, серьёзно думаете, что мы способны на... такое?!"
    "Я посмотрел на неё взглядом, полным ненавистью."
    show mt sad pioneer with dspr
    mt "Ну, нет..."
    "Ольга замялась."
    show mt scared pioneer with dspr
    mt "Ну кто-то же это сделал!"
    me "Может это дикие животные какие-то. Не знаю, волки, медведи."
    mt "Тут отродясь диких зверей не водилось..."
    th "Точно..."
    me "То-есть вы думаете, что это сделал кто-то из пионеров?"
    "Я очень заинтересованным голосом спросил у неё."
    mt "Ну, а больше некому..."
    "..."
    mt "В общем, надо звонить в милицию."
    me "Пойдёмте звонить тогда."
    stop music fadeout 3
    mt "Идём..."
    scene bg ext_square_sunset with dissolve
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    play ambience ambience_camp_center_evening fadein 3
    "Мы наконец-то вышли из леса и оказались на площадь."
    play music music_list["just_think"] fadein 11
    "Алиса всю дорогу всхлипывала."
    show mt sad pioneer with dissolve
    mt "Я пойду в Админ корпус, а вы сидите по домам."
    hide mt with dissolve
    "Ольга поспешно удалилась."
    show dv sad pioneer with dissolve
    dv "М-может к-ко мне?"
    me "Боишься?"
    stop music fadeout 3
    "Алиса еле заметно кивнула."
    me "Пойдём."
    scene bg ext_domik_dv_vecher with dissolve
    "Мы пришли к домику Алисы."
    play sound sfx_open_door_1
    scene bg int_domik_dv_vecher with dissolve
    $ save_name = ('День 2. Обещаю.')
    "Внутри никого не было."
    th "Ну пришли, а делать что?"
    play music My_Silent_Angel fadein 3
    th "Думаю, сейчас первым делом нужно успокоить Алису."
    me "Как думаешь, кто бы это мог сделать?"
    show dv sad pioneer with dissolve
    dv "Не знаю... надеюсь это был дикий зверь, медведь какой... не знаю..."
    me "Не знаю. Я думаю, что это кто-то из лагеря, но ты не беспокойся, я сделаю всё возможное, чтобы вычислить убийцу."
    dv "Как мне это надоело! Сначала этот фильм дурацкий, потом как ты говоришь \"мы попали в Совёнок\", теперь ещё тут убийца завёлся!" 
    dv "Зачем?.. Зачем я только на это согласилась?.. Думала отдохнём пару недель и поработаем чуть-чуть. А тут... а тут..."
    play sound plach_14sek
    show dv cry pioneer with dspr
    "Алиса ещё сильнее разрыдалась."
    show dv cry pioneer close with dissolve
    "Я обнял её и прижал к себе."
    "Алиса, хныкая мне в плечо, продолжила:"
    play sound plach_14sek
    dv "Сидела бы сейчас дома... смотрела бы сериальчики... и бед бы не знала..."
    me "Ты даже представить себе не можешь, в какой ситуации я..."
    dv "Мы в одной ситуации, дурень!"
    me "Поверь, ты очень ошибаешся."
    dv "Да?.."
    me "Да."
    "..."
    show dv sad pioneer close with dissolve
    dv "Не знаю почему, но я тебе верю."
    me "..."
    me "Спасибо."
    show dv sad_smile pioneer with dissolve 
    "Алиса перестала плакать и наконец отстранилась от меня."
    "Я прервал момент своим вопросом."
    me "Может в картишки?"
    dv "Ну... можно..."
    stop music fadeout 3
    scene bg black with dissolve
    play ambience ambience_int_cabin_night fadein 3
    $ save_name = ('День 2. Где Ульяна?')
    "Следующие несколько часов мы провели за игрой в карты и разговорами ни о чём и обо всём."
    "К часам 11 Алиса заметила, что Ульяна до сих пор не вернулась." 
    scene bg int_house_of_dv_night_light with dissolve
    show dv scared pioneer with dissolve
    dv "Стой, а где Ульянка? Она же по сценарию со мной живёт."
    me "Не знаю..." 
    th "И вправду... где она ? " 
    show dv sad pioneer with dspr
    dv "А что если с ней случилось тоже самое... что и с Сашей ?" 
    me "С кем? " 
    dv "Ну то есть со Славей."
    me "Не знаю..."
    dv "Может пойдём к Ольге Дмитриевне?"
    me "А не поздно?"
    dv "Ну мы же по поводу..."
    me "Ладно, пошли, всё равно там мой дом."
    play sound sfx_open_door_1 
    scene bg ext_house_of_dv_night with dissolve
    pause 1.
    play ambience ambience_camp_center_night fadein 2
    $ persistent.sprite_time = 'night'
    $ night_time()
    scene bg black with dissolve
    "..."
    scene bg ext_houses_night with dissolve
    $ save_name = ('День 2. Пропажа.')
    "На улице мы заметили одну странность."
    show dv sad pioneer with dissolve
    dv "Тебе не кажется, что слишком тихо?"
    th "Действительно... Ночью в лагере, конечно, тихо, но...{w} но не настолько же!"
    th "Только звуки сверчков слышно."
    me "Да, как-то не правдоподобно даже." 
    th "Хотя весь этот лагерь сам по себе не правдоподобный."
    scene ext_house_of_mt_night_without_light with dissolve
    play music sdl_tpinf_cu fadein 7
    "Подойдя к домику вожатой, мы увидели Лену и Электроника спорящих на повышенных тонах."
    show el angry pioneer far at left
    show un angry pioneer far
    with dissolve
    un "А что ты знаешь?!"
    el "Да я-то что?! Я вообще своего друга ищу, а ты вот что тут делаешь?! Вообще иди к себе домой!"
    un "А ТЫ В КУРСЕ, ЧТО МЫ, ПОХОЖЕ, ОСТАЛИСЬ В ЛАГЕРЕ ВДВОЁМ!?" with vpunch
    show el shocked pioneer far with dspr
    el "Что?!"
    "Пыл Электроника резко угас и сменился на удивленние."
    un "Что слышал!"
    show el normal pioneer far with dspr
    "Электроник задумался о чём-то."
    el "И правда...{w} Больно уж тихо..."
    "Через пару мгновений Мику прибежала вся встревоженная."
    show mi shocked pioneer far at right with dissolve
    mi "Что у вас тут случилось?"
    show el angry pioneer far with dspr
    el "Ты же говорила что мы остались в лагере вдвоём!?"
    show un surprise pioneer far with dspr
    un "Эээ..."
    el "Получается, ты меня обмануть хотела?"
    "Пока Лена замялась, мы тоже вышли к ним."
    show el shocked pioneer
    show mi shocked pioneer
    show un scared pioneer
    with dissolve
    me "Вдвоём в лагере вы не остались, но вот кроме всех кто тут есть, похоже, больше никого."
    mi "Что?!"
    show un rage pioneer with dspr
    un "Что слышала!"
    me "Тише! Сейчас не время для ссор!"
    show el sad pioneer with dspr
    show un sad pioneer with dspr
    el "Да... простите..."
    un "Извини..."
    show mi sad pioneer with dspr
    mi "Так, что же нам делать, если кроме нас и вправду никого больше нет? А что если с ними что-то случилось? Что-то очень-очень плохое... Нет, даже думать такого не хочу."
    el "Для начала нужно в этом на сто процентов убедиться!"
    me "Хорошо, тогда я схожу проверю все домики и столовую."
    show dv sad pioneer at fright with dissolve
    dv "Один?"
    me "Ну..."
    dv "Это плохая идея."
    th "Да, пожалуй..."
    menu:
        "Пойти с Электроником":
            $ od_ochki += 2  
            $ dv2_ochki -= 2
        "Пойти с Алисой":
            $ dv2_ochki += 2  
            $ od_ochki -= 2
    if od_ochki >= 2:
        jump somesing_new_odinochka
    else:
        jump somesing_new_dvache_obhod




label somesing_new_odinochka:
    $ save_name = ('День 2. Проверка.')
    me "Электроник."
    show el scared pioneer with dspr
    el "Что?"
    me "Идём."
    el "А может..."
    me "Не может! Ты мужик или кто?" with vpunch
    show el sad pioneer with dspr
    el "Мужик..."
    stop music fadeout 3
    scene bg black with dissolve
    "..."
    scene bg ext_house_sem_night with dissolve
    "Мы проверили около десяти домиков, но вдруг меня окликнул Эл."
    show el sad pioneer
    play ambience ambience_camp_center_night fadein 2
    with dissolve
    el "Семён..." 
    me "Чего тебе?"
    el "Может пошли назад?"
    me "Почему это?"
    el "Я б-бою... то есть устал я, спать охота, а всех кто остался в лагере, можно проверить и завтра на приемах пищи."
    me "Наверное...{w} Слушай, а иногда к тебе толковые мысли приходят!"
    show el smile pioneer with dspr
    el "Спасибо!"
    "Мы двинулись назад ко всем."
    scene bg ext_house_of_mt_night_without_light with dissolve
    show dv scared pioneer at fright
    show mi scared pioneer at cright 
    show un scared pioneer
    with dissolve
    $ save_name = ('День 2. Спокойной ночи.')
    un "Ну как?"
    me "Никого."
    show mi shocked pioneer with dspr
    mi "Вообще-вообще никого?"
    me "Да."
    "..."
    me "Сейчас нам лучше не разделяться, поэтому спать будем в этом домике."
    "Все кивнули."
    play sound sfx_open_door_2 
    scene bg int_house_of_mt_night2 with dissolve
    "Мы зашли внутрь..."
    play sound vkl
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_mt_night with dissolve
    "Включили свет, и вдруг у нас возник вопрос:"
    $ persistent.sprite_time = 'day'
    show un normal pioneer at right with dissolve
    un "А как спать будем?"
    show el normal pioneer with dissolve
    el "Да, кстати... Кровати-то две, а нас пять."
    me "Мику будет спать с Леной, Алиса отдельно."
    el "А я?"
    th "Хм... и вправду?"
    "..."
    th "О!"
    me "А ты занеси шезлонг, который возле домика. Будешь спать в нём."
    el "А ты?"
    me "А я буду дежурить."
    show el smile pioneer with dissolve
    el "Понял! Тогда удачи!"
    me "Спасибо."
    hide el
    hide un
    with dissolve
    "Все лягли в свои кровати."
    me "Всем спокойной ночи."
    "В ответ все что-то сонно проплели и тут же лягли спать."
    "..."
    th "И что ж тут, всё же, твориться?"
    th "Сначала эти съёмки, потом вместе с Алисой-актрисой попал назад в пионерлагерь."
    th "Потом ещё и Славю расчленил кто-то..."
    th "В принципе сам по себе этот момент меня не особо шокирует, шокирует то, что это сделал кто-то кроме меня."
    th "Можно было бы списать это на какого-нибудь пионера из другого отряда ожил, но эта теория отпадает так как тепрь в лагере остались только мы."
    th "Но если это не я, то выходит кто-то из нас?"
    th "Алиса нет, она всё время была со мной."
    th "Электроник тоже на такое не способен."
    th "Мику даже муху не обидит."
    th "Лена?{w} Она, конечно, занималась как-то раз с Алисой любительским боксом, но не более."
    th "Она хоть и девочка с ножом, но ни разу она его не применяла."
    th "..."
    th "Почти..."
    th "В тот цикл когда я резню устроил он отчаянно защищалась своим ножиком..."
    th "..."
    th "И вот зачем я только сорвался..."
    th "Она ведь ничего плохого тогда мне не хотела..."
    th "Ещё и её последние слова..."
    th "\"Я не знаю зачем ты это делаешь, но знай я тебя люблю даже таким. Если ты хочешь чтобы моя судьба закончилась сейчас, то пусть так и будет.\""
    th "А ещё тогда смеялся над ней..."
    th "Какой я всё таки урод."
    th "Странно, что я только что это заметил."
    th "Что же на меня так повлияло?"
    "Глаза уже слипались, поэтому раздумывая об этом, я заснул."
    jump something_new_dv_rut_d3




label somesing_new_dvache_obhod:
    $ save_name = ('День 2. Обход лагеря.')
    me "Тогда пойдём вместе."
    dv "..."
    dv "Х-хорошо..."
    stop music fadeout 3
    scene bg black with dissolve
    "Сначала мы проверили все домики."
    "Проверив все домики мы пошли на склад."
    scene cg alisa_pod_ruku with dissolve
    play music melonholy fadein 3
    "Алисе видимо стало страшно и она схватила меня за руку."
    me "Ты чего?"
    dv "Мне с-страшно..."
    me "Не бойся. Всё будет хорошо."
    dv "Надеюсь..."
    dv "Ты говорил, что твоя ситуация ещё хуже?..{w} Можешь рассказать?"
    me "Ладно, скажу как есть."
    me "Я застрял в вашем, то есть нашем фильме. Так сказать, в цикле."
    dv "Как?"
    me "Почти так же как и попала сюда ты. Через сон.{w} Заснул в автобусе, а проснулся в автобусе уже в \"Совёнке\"."
    me "И когда смена заканчивается, мы садимся в автобус и уезжаем."
    me "Но приезжает он уже на начало смены, где никто ничего не помнит."
    "..."
    me "Как-то так."
    dv "Ясно..."
    me "Ты мне веришь?"
    dv "Да... хоть не очень-то и хочется..."
    scene bg ext_sklad_night with dissolve
    "Возле склада я остановился."
    show dv normal pioneer with dissolve    
    dv "А чего мы вообще на склад забрели? Не лучше ли было сначало заглянуть в столовую например?"
    me "Если честно, мы сюда за оружием."
    show dv scared pioneer with dspr  
    dv "Зачем?"
    me "Ну вдруг мы встретим...{w} того кто убил Славю."
    show dv sadness pioneer with dspr
    dv "Не напоминай..."
    me "Хорошо."
    "Я подергал ручку, проверив не открыт ли склад часом."
    play sound sfx_open_door_sklad
    play ambience ambience_int_cabin_night  fadein 2
    "На удивление он оказался открытым."
    scene bg int_sklad2_night with dissolve
    "Я зашёл и начал шариться по полкам."
    dv "Что там?"
    me "Ищу вот, можешь пока на улице подождать."
    dv "Окей..."
    "Я продолжил поиски и через минут 5, нашёл какую-то монтировку."
    me "О!"
    dv "Что там?"
    me "Да нашёл тут кое-что."
    dv "И что же?"
    me "Заходи - увидишь."
    play sound sfx_door_squeak_light 
    "Алиса зашла."
    show dv normal pioneer with dissolve
    me "Тада-а-ам!"
    show dv surprise pioneer with dspr
    dv "Она поможет?"
    me "Не знаю...{w} Но это всяко лучше чем ходить с голыми руками."
    show dv sad pioneer with dspr
    dv "Надеюсь тот кто..."
    show dv cry pioneer with dspr
    play sound soul_cry
    dv "Тот кто...{w} того Славю...{w} Вообще больше не появится."
    "Я обнял Алису."
    show dv cry pioneer close with dspr
    me "Надежды нет.{w} Надо всегда быть готовым к худшему."
    me "Но это не значит, что надо сдаваться!{w} Поэтому я тебе обещаю - мы выберемся отсюда."
    show dv sad pioneer close with dspr
    dv "В чём-то ты прав..."
    dv "Так ты...{w} обещаешь?"
    me "{i}Обещаю.{/i}"
    show dv sad_smile pioneer with dissolve
    "Она отстранилась от меня."
    me "Пойдём к остальным?"
    dv "П-пошли..."
    scene bg black with dissolve
    "..."
    scene bg ext_house_of_mt_night_without_light with dissolve
    show el scared pioneer at fright
    show mi scared pioneer at cright 
    show un scared pioneer
    with dissolve
    play ambience ambience_camp_center_night fadein 2
    $ save_name = ('День 2. Спокойной ночи.')
    "Мы быстро вернулись к ребятам."
    el "Ну что?"
    me "Никого."
    show un serious pioneer with dspr
    un "Я же говорила!"
    show el sad pioneer at fright with dspr
    el "Ладно, признаю, был не прав, не заводись ты."
    un "Л-ладно."
    "Скрежа зубами ответила Лена."
    show mi sad pioneer at cright with dspr
    mi "Может, нам не стоит разделяться?.. А то, то что было сегодня со Славей... И чтобы не исчезнуть как все..."
    me "Я с тобой согласен."
    show el surprise pioneer at fright with dspr
    el "Но где нам спать?"
    me "Можно прямо тут, у меня в домике."
    show el normal pioneer at fright with dspr
    el "..."
    el "Да, хорошая мысль."
    play sound sfx_open_door_2 
    stop music fadeout 3
    scene bg int_house_of_mt_night2 with dissolve
    play ambience ambience_int_cabin_night fadein 3
    "Мы зашли внутрь..."
    play sound vkl
    scene bg int_house_of_mt_night with dissolve
    "Включили свет, и вдруг у нас возник вопрос:"
    $ persistent.sprite_time = "day"
    show un normal pioneer at right with dissolve
    un "А как спать будем?"
    show el normal pioneer with dissolve
    el "Да, кстати... Кровати-то две, а нас пять."
    me "Мику будет спать с Леной, Алиса отдельно."
    el "А я?"
    th "Хм... и вправду?"
    th "..."
    th "О!"
    me "А ты занеси шезлонг, который возле домика. Будешь спать в нём."
    el "А ты?"
    me "А я буду дежурить."
    show el smile pioneer with dissolve
    el "Понял! Тогда удачи!"
    me "Спасибо."
    hide el
    hide un
    with dissolve
    "Все легли в свои кровати."
    me "Всем спокойной ночи."
    "В ответ все что-то сонно пробубнили и тут же легли спать."
    "..."
    th "И что ж тут всё же творится?"
    th "Сначала эти съёмки, потом вместе с Алисой-актрисой попал назад в пионерлагерь."
    th "Потом ещё и Славю расчленил кто-то..."
    th "В принципе сам по себе этот момент меня не особо шокирует, шокирует то, что это сделал кто-то, кроме меня."
    th "Можно было бы списать это на какого-нибудь пионера из другого отряда, но эта теория отпадает так как теперь в лагере остались только мы впятером."
    th "Но если это не я, то выходит, что это кто-то из нас?"
    th "Алиса точно нет, она всё время была со мной."
    th "Электроник на такое не способен."
    th "Мику даже муху не обидит."
    th "Лена?{w} Она, конечно, занималась как-то раз с Алисой любительским боксом, но не более."
    th "Она хоть и девочка с ножом, но ни разу она его не применяла."
    th "..."
    th "Почти..."
    th "В тот цикл, когда я устроил резню, она отчаянно защищалась своим ножиком, не помогло правда..."
    th "..."
    th "И вот зачем я только сорвался..."
    th "Она ведь ничего плохого тогда мне не хотела..."
    th "Ещё и её последние слова..."
    th "\"Я не знаю, зачем ты это делаешь, но знай, я тебя люблю даже таким. Если ты хочешь чтобы моя жизнь оборвалась сейчас, то пусть так и будет.\""
    th "А я ещё тогда смеялся над ней..."
    th "Какой я всё таки урод."
    th "Странно, что я только сейчас это заметил."
    th "Что же на меня так повлияло?"
    "Глаза уже слипались, поэтому, раздумывая об этом, я заснул."
    jump something_new_dv_rut_d3



label something_new_dv_rut_d3:
    show blink
    window hide dissolve
    $ renpy.pause(1.5, hard=True)
    stop ambience fadeout 1
    stop sound_loop fadeout 1
    scene bg black
    with fade3
    $ backdrop = "days"
    $ new_chapter(3, "День 3. Проспал...")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "days"
    $ renpy.pause(1, hard=True)
    $ persistent.sprite_time = "day"
    $ day_time()
    pause 1.5
    scene bg int_house_of_mt_day
    play ambience ambience_int_cabin_day fadein 3
    show mi normal pioneer far at right 
    show el normal pioneer far at fright
    show un normal pioneer far at fleft
    show dv sad pioneer far 
    show unblink
    window show dissolve
    "Проснувшись, я увидел, что все уже бодрствуют."
    play music sam_menu_achiv_music fadein 2
    "Мику и Электроник сидели на кровати Ольги Дмитриевны и о чем то разговаривали, Лена сидела на моей кровати и витала в облаках, а Алиса не отводя глаз смотрела в окно."
    "Время на часах было - 10:50."
    th "А я так-то дежурить должен был..."
    me "Доброе утро всем."
    el "Ага..."
    show mi upset pioneer far at right 
    mi "Доброе."
    "Растрепанный и не выспавшийся, я протер глаза и подошел к Алисе."
    hide mi
    hide un
    hide el
    with dissolve
    show dv sad pioneer close with dspr
    me "Все хорошо?"
    dv "Я все переживаю… где я, куда все пропали, что вообще происходит?"
    me "Я тебе врать не буду, не знаю как это произошло, но я уверен, что все будет хорошо. Доверься мне."
    "Алиса мило приподняла уголки рта, показав еле заметную улыбку."
    show dv shy pioneer close with dspr
    dv "Спасибо тебе, Сёма..."
    me "Давай лучше решим что делать?"
    dv "Давай."
    hide dv with dissolve
    "Позвав Лену, я с Алисой подошёл к Электронику и Мику."
    show mi normal pioneer at cright 
    show el normal pioneer at fright
    show un normal pioneer at fleft
    show dv normal pioneer at cleft
    with dissolve
    me "Ребят, давайте решать, что будем делать? У кого какие варианты?"
    show el smile pioneer with dspr
    el "В столовую!"
    "Я посмотрел на Алису с Леной и спросил:"
    me "Пойдём?"
    stop music fadeout 2
    "Получив положительный ответ, мы вышли на улицу."
    play sound sfx_close_door_1 
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    $ save_name = ('День 3. Стряпня Алисы.')
    "На улице я почувствовал прохладный ветерок и услышал шелест деревьев."
    th "Хоть что-то успокаивающее..."
    "Мы направились к столовой в полной тишине."
    scene bg black with dissolve
    pause 2.0
    scene bg ext_square_day with dissolve
    "Выйдя на площадь, мы еще раз удостоверились, что здесь мы одни."
    show mi normal pioneer at cright with dissolve
    mi "Никого..."
    scene bg ext_dining_door_day with dissolve
    play music music_list["afterword"] fadein 3
    "Буквально через пару минут мы стояли на пороге столовой."
    "Я потянул за ручку двери."
    play sound sfx_open_door_campus_1  
    "Дверь распахнулась и мы зашли."
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    th "Ещё один плюсик к теории, что все бесследно исчезли."
    show el normal pioneer at fleft with dissolve
    show mi sad pioneer at left with dissolve
    mi "А что есть будем? В лагере никого нет кроме нас. Лично я не умею готовить... А вы?.."
    "Мику с надеждой посмотрела на девочек."
    show un normal pioneer at right with dissolve
    "Лена отрицательно замотала головой."
    me "Про это я не подумал... Наверное возьмём булочек с кефиро..."
    show dv smile pioneer with dissolve
    dv "Да не парьтесь, я умею готовить."
    show mi surprise pioneer
    show un serious pioneer 
    with dspr
    un "Что?! Ты же никогда ничего не готовила!"
    dv "Не переживайте, от моей стряпни ещё пока никто не погиб."
    el "Ещё пока..."
    show dv angry pioneer
    show el scared pioneer
    with dspr
    "Алиса грозно зыркнула на Эла."
    "Он тут же пожалел, что вставил слово."
    hide dv with dissolve
    "Однако Алиса ничего более ему не сделала, она ни сказав ни слова зашла в столовую и начала шариться по шкафчикам."
    scene bg int_dining_hall_table_day_back with dissolve
    "Мы сели на первые попавшиеся места."
    show un normal pioneer at cright
    show mi smile pioneer at cleft 
    show el normal pioneer at fleft
    with dissolve
    mi "Не знала что Алиса умеет готовить."
    me "Я тоже приятно удивлен."
    "..."
    "Мику начала что-то очень быстро рассказывать, но я не успевал следить за нескончаемым потоком слов, поэтому не слушал."
    "Лена сидела молча и все еще была погружена в свои мысли."
    me "Ты как?"
    un "А?{w} А ну я хорошо, да..."
    me "О чём-то задумалась?"
    show un evil_smile with dspr
    un "Да так, о своем."
    show un normal pioneer with dspr
    "Показалось будто лена немного ухмыльнулась."
    me "Всё в порядке?"
    un "Да, спасибо."
    "Через некоторое время, Алиса крикнула с кухни нам, что всё готово."
    show dv normal pioneer at fright with dissolve
    "Алиса поставила тарелки с нехитрым завтраком, в виде сырников, на стол и села к нам."
    dv "Приятного аппетита."
    "Ответив \"Спасибо\", мы попробовали первый кусочек."
    th "Сто лет сырники не ел."
    me "Очень вкусно!"
    mi "Да-да, вкусно!{w} Нет, ну правда! Это очень-очень-очень вкусно!{w} Я, например, так не смогу!"
    show el sad pioneer with dspr
    el "Сойдёт…."
    "Но спустя секунду Электроник изменил свой вердикт."
    show el scared pioneer with dspr
    el "Э-э…. то есть очень вкусно!"
    show dv shy pioneer with dspr
    dv "Да что вы ребят?.. Не льстите, а кушайте, давайте."
    stop music fadeout 7
    "Доев блюдо от шеф-повара Алисы, мы вышли на крыльцо."
    scene bg ext_dining_door_day with dissolve
    play sound sfx_close_door_campus_1 
    play ambience ambience_camp_center_day fadein 3
    show dv normal pioneer close at fright
    show un normal pioneer at cright
    show mi normal pioneer at fleft
    show el normal pioneer at cleft 
    with dissolve 
    $ save_name = ('День 3. Что делать?')
    dv "И что теперь делать?"
    th "Хороший вопрос...{w} Веселится сейчас точно не время, но и работать над чем-то нужным, тоже нечего."
    mi "Может поищем людей?"
    el "А может, ну его?"
    me "А что ты предлагаешь? Не сидеть же просто так."
    show el sad pioneer at cleft with dspr 
    el "Ну...{w} да..."
    "Алиса легонько взяла меня за руку, показывая свое нежелание разделяться."
    me "Тогда давайте ещё раз проверим все домики и...{w} не знаю...{w} Админ корпус может?"
    un "Да, давайте так."
    scene bg black with dissolve
    window hide dissolve
    pause 2.0
    $ save_name = ('День 3. Шорох.')
    scene bg ext_house_of_un_day with dissolve
    window show dissolve
    "Проходя мимо домика Лены, внезапно из кустов донесся шорох."
    play sound sfx_bush_leaves
    play music music_list["no_tresspassing"] fadein 2.5
    show dv scared pioneer at fright
    show un scared pioneer at cright
    show mi scared pioneer at fleft 
    show el scared pioneer at cleft
    with dissolve 
    th "Обычно бы я предал бы этому значение, но в такой-то ситуации..."
    mi "Вы это слышали?"
    dv "Э-э-э... а-а-а..."
    me "Слышали."
    el "И кто это мог быть?"
    un "Может, дикий зверь какой..."
    me "Ещё бы они тут водились..."
    el "Может, тогда это белка?"
    show mi sad pioneer at fleft with dspr
    stop music fadeout 3
    mi "Может..."
    $ save_name = ('День 3. Опять никого.')
    scene bg black with dissolve2
    window hide dissolve
    pause 3.0
    scene bg ext_house_of_kostya_day with dissolve
    window show dissolve
    "Мы обошли оставшиеся домики, но так никого и не нашли."
    show dv sad pioneer at fright
    show un normal pioneer at cright
    show mi sad pioneer at fleft 
    show el sad pioneer at cleft 
    with dissolve
    un "Никого..."
    dv "Ага..."
    me "Пошлите теперь в Админ корпус."
    el "Пойдёмте..."
    scene bg black with dissolve
    window hide dissolve
    pause 2.5
    scene bg ext_admin_day with dissolve
    window show dissolve
    show mi shocked pioneer at fleft
    with dissolve
    $ save_name = ('День 3. Кузнечики из ада.')
    "Когда мы пришли Мику что-то насторожило."
    me "Мику? Что случилось?"
    mi "Вы не слышите?"
    show el surprise pioneer at fright 
    show dv surprise pioneer at cright
    show un surprise pioneer 
    with dissolve
    el "Что не слышим?"
    mi "Ну как же... Я сейчас оглохну от этого звука."
    stop ambience fadeout 1
    play music ktoto_nablyadaet fadein 5
    play sound sfx_hell_crickets_1 loop fadein 1.1
    "Внезапно я тоже услышал этот звук."
    "Звук похожий на стрекотание сверчков, только эти сверчки из ада."
    me "Мику! Успокойся! Всё будет нормально!"
    mi "А-а-а-а-а!"
    show el shocked pioneer 
    show dv shocked pioneer at cright
    show un shocked pioneer 
    with dspr
    "Все остальные застыли с шокированными лицами и просто стояли."
    show mi cry pioneer with dspr
    "Мику схватилась за голову и заплакала."
    me "Мику..."
    mi "Они везде... они везде..."
    hide un
    hide el
    hide dv
    with dissolve
    show mi cry pioneer close at center with dissolve
    "Я молча взял Мику на руки и вошел в здание."
    stop sound fadeout 1.5
    play ambience ambience_int_cabin_day fadein 4
    scene bg int_admin_hall with dissolve
    "Когда я с Мику на руках зашёл в здание звук прекратился."
    show mi cry pioneer close at left with dissolve
    mi "Они везде... они повсюду..."
    me "Мику!"
    "Я начал бить её по щекам."
    stop music fadeout 6
    play sound sfx_face_slap
    me "Очнись всё в порядке!" with hpunch
    play sound sfx_face_slap
    me "Всё уже закончилось!" with vpunch
    "Мику вроде как очнулась и разрыдалась."
    play sound plach_14sek
    "Алиса наконец вышла из шока и с улицы раздался крик."
    dv "Что вы встали?! Вдруг им сейчас помощь нужна."
    mi "Что...{w} что это...{w} что это было?.."
    me "Я не знаю..."
    "Вся компашка глухих вбежала внутрь."
    play sound sfx_open_door_strong  
    show el shocked pioneer at fright
    show dv shocked pioneer at cright
    show un shocked pioneer
    with dissolve
    "На их лицах можно было прочесть недоумение и удивление"
    un "Что это сейчас было?.."
    me "Сейчас она и я услышали звуки, судя по всему из ада."
    el "Что?!"
    mi "Они... они были повсюду!"
    un "Кто они?"
    me "Стрекот адских кузнечиков."
    "На лицах всех, опять застыл шок."
    el "Но на улице же была тишина! Как это возможно?"
    me "А мне по чём знать!?"
    "В воздухе повисло молчание."
    $ save_name = ('День 3. Администрация.')
    "Когда Мику перестала плакать, она заговорила."
    show mi sad pioneer with dspr
    mi "Может... всё же проверим тут наличие людей?"
    show dv sad pioneer
    show el sad pioneer
    show un sad pioneer
    with dspr
    dv "А ты в порядке?"
    mi "Нет, но я справлюсь..."
    el "Ну, вообще, стоило бы."
    me "Да, давайте я с Мику и с Алисой проверим 1 этаж, а вы идите на 2."
    el "Хорошо..."
    hide el
    hide un 
    with dissolve
    "Электроник и лена ушли на 2 этаж, я полагаю."
    me "Пойдём?"
    mi "Д-да..."
    play sound sfx_open_door_1 
    scene bg int_admin_cabinet with dissolve
    "Мы вошли в первый кабинет."
    dv "Никого."
    me "Идём дальше."
    play sound sfx_close_door_1 
    scene bg black with dissolve
    pause 2.5
    scene bg int_director_office_day
    show mi sad pioneer at cleft
    show dv sad pioneer at cright
    with dissolve
    "Мы зашли в последнюю комнату."
    me "И тут пусто..."
    mi "Ну, зато мы теперь убедились."
    me "Да..."
    "Удостоверившись, что на первом этаже никого нет, мы вышли на улицу ждать Лену и Электроника."
    scene bg ext_admin_day with dissolve
    $ save_name = ('День 3. Что у вас произошло?')
    play ambience ambience_camp_center_day fadein 3
    "..."
    "..."
    "Мы их ждали, ещё около двадцати минут, и мне это надоело."
    me "Ну где можно шляться так долго?"
    dv "Может проверим?"
    me "Я схожу, подождите здесь."
    scene bg int_admin_hall2 with dissolve
    play ambience ambience_int_cabin_day fadein 2
    "Побродив пару минут по этажу, я услышал дверь за которыми были звуки..."
    th "Звуки чего?{w} борьбы?{w} Нет менее активные."
    play sound sfx_open_door_1
    "Открыв дверь я увидел неожиданную картину."
    scene cg reflection_el_un with dissolve
    "Электроник лежал на Лене держа её за руки и просто смотрел ей в глаза."
    play sound man_otkashlyalsya
    me "Извините, что прерываю, но что у вас тут происходит?"
    scene bg int_office_day
    show un shocked pioneer at cleft
    show el shocked pioneer at cright
    with dissolve
    "Эл тут же вскочил с Лены и даже не мог составить связанное предложение."
    el "Я... ну... это...{w} э...{w} упал..."
    show un normal pioneer with dspr
    un "Всё в порядке просто недоразумение."
    show el surprise pioneer with dspr
    "Казалось, что Электроник удивился словам Лены."
    el "Ну, в общем-то да..."
    me "Ладно, с кем не бывает.{w} Вы всё проверили?"
    show el sad pioneer with dspr
    el "Да... никого."
    me "Тоже."
    "..."
    me "Пошлите нас внизу ждут."
    un "Да..."
    $ save_name = ('День 3. Мираж?')
    scene bg ext_admin_day
    show mi shocked pioneer at cleft
    show dv shocked pioneer at cright
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Выйдя мы увидели Мику, застывшую на месте и Алису, которая, пыталась её растормошить."
    play music music_list["orchid"] fadein 7
    me "Что случилось?!"
    dv "Она опять..."
    "Я встал прямо перед Мику, достал сигарету и выдул дым прямо ей в лицо."
    play sound zazheg_sigaru
    window hide dissolve
    hide dv with dissolve
    $ renpy.pause(3.5, hard = True)
    show mi shocked pioneer close at center with dissolve
    $ renpy.pause(4.0, hard = True)
    show mi dontlike pioneer close with dspr
    window show dissolve
    mi "Ты чего!?"
    me "С добрым утром. Что опять?"
    show mi sad pioneer close with dspr
    "Мику пыталась сдержать слёзы."
    mi "Я, я... я видела... там..."
    me "Что? Что ты видела?"
    mi "Ульяну..."
    me "Так это же отлично!"
    play sound soul_cry
    show mi cry pioneer close with dspr
    mi "Она вышла из кустов в состоянии точно не совместимым с жизнью и...{w} и...{w} и позвала меня."
    "Мику зарыдала."
    me "Это как?{w} Ульяна зомби?"
    mi "Д-да..."
    "..."
    show mi cry pioneer
    show el shocked pioneer at cright 
    with dissolve
    el "Но ведь зомби не бывает! Это же антинаучно!"
    show dv normal pioneer at fright with dissolve
    dv "Ты за последние пару дней хоть что-то научное видел?"
    show el sad pioneer with dspr
    el "Ну...{w} нет..."
    me "Мику, ты уверена, что видела её?"
    mi "Ну... Она когда я обернулась на своё имя я увидела её, моргнула и её нет."
    me "Тогда может тебе показалось? Переволновалась там из-за этих сверчков, вот и померещилось."
    th "Хотя я даже сам, мало в это верю."
    show mi sad pioneer with dspr
    mi "Возможно.{w} Думаю, что да."
    me "Тогда, пока остановимся на этом варианте."
    show el normal pioneer with dspr
    stop music fadeout 3
    el "Пожалуй."
    dv "Может пойдём перекусим, а то я проголодалась уже со всей этой беготней."
    me "Да, было бы славно."
    "Переглянувшись, мы тронулись полдничать."
    "..."
    scene bg black with dissolve
    pause 2.0
    scene bg int_dining_hall_sunset with dissolve 
    play ambience ambience_dining_hall_empty fadein 2
    "Алиса сказала, что устала и готовить не будет, поэтому мы взяли булочек с кефиром."
    show mi sad pioneer at right with dissolve
    mi "Я что-то кушать не очень хочу..."
    show dv normal pioneer with dissolve 
    dv "Точно? Если ночью захочешь, то никто не пойдёт."
    mi "Точно, говорю же вам."
    me "Как знаешь."
    "Алиса осталась уговаривать Мику поесть."
    th "Заботливая была бы жена..."
    scene bg int_dining_hall_table_day_back
    show el normal pioneer at right
    show un serious pioneer at fleft
    with dissolve
    "А я, в свою очередь, пожав плечами сел за столик к Электронику и Лене."
    "Между ними чувствовалось какое-то напряжение."
    th "Наверное, из-за того инцидента в административном корпусе."
    el "Я это... пойду."
    "Эл уже хотел пойти на выход, но я его остановил."
    me "Стоять!{w} Ни куда ты один не пойдёшь!"
    show el angry pioneer at right with dspr
    el "Почему это!?"
    me "Как минимум чтобы не исчезнуть как все, а как максимум чтобы тебя не настиг убийца Слави."
    show el sad pioneer at right with dspr
    el "Да, ты прав, прости..."
    hide un with dissolve
    "Лена, за время пока Электроник планировал сбежать, доела и подошла к девочкам."
    "..."
    me "Ты куришь?"
    show el surprise pioneer with dspr
    el "Что?{w} Нет конечно!"
    me "А сейчас бы закурил?"
    show el sad pioneer with dspr
    el "С тем что происходит, наверное, да..."
    me "Тогда пошли."
    show el surprise pioneer with dspr
    el "Куда?"
    me "На перекур."
    el "А откуда у тебя сигареты?"
    me "Тебя это только сейчас смутило?"
    el "А когда ещё должно было?"
    me "Ну, например, когда я Мику в лицо выдохнул дым."
    show el normal pioneer with dspr
    el "А-а-а...{w} точно.{w} Тогда просто не до этого было."
    me "Ладно, пошли уже."
    play sound sfx_open_door_campus_1  
    play music i_drive fadein 5
    scene bg ext_dining_door_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    "Покинув столовую, я сразу же закурил."
    play sound zazheg_sigaru
    "..."
    show el normal pioneer with dissolve
    el "Ну давай, попробую."
    me "Погодь."
    "  "
    pause 1.5
    me "Держи."
    "Я протянул Электронику пачку сигарет и зажигалку."
    el "Спасибо."
    play sound zatyaga
    $ renpy.pause (3.2, hard=True)
    play sound el_cough
    show el normal pioneer with dspr
    el "Ой не, гадость какая..."
    me "Тогда давай назад."
    "Он так и поступил."
    show el smile pioneer with dspr
    el "Хорошего тебе перекура, а я пожалуй вернусь."
    me "Мерси."
    play sound sfx_open_door_1
    hide el with dissolve
    "..."
    play sound sfx_close_door_campus_1
    pause 0.2 
    play sound kurit
    th "Эх...{w} помню в прошлой жизни я всё время курил..."
    th "Всё бросить хотел, а теперь зачем? "
    th "Здоровье тут бесконечное, от сигарет не умру."
    th "Хотя даже если б умер, то курил.{w} И курил бы даже больше."
    th "Хотя в последнее время происходит много нового."
    th "У меня даже тяга к жизни появилась."
    th "..."
    play sound kurit
    th "Возможно даже настоящую Алису встретил, кто знает."
    th "Если она будет запоминать циклы как я, то быть может, снова начну жить, а не существовать."
    th "Главное чтобы циклы были не такими как этот..."
    th "Интересно, что хуже застрять в таком цикле с человеком или одному в обычном цикле?"
    th "Хороший вопрос..."
    th "Если бы мне прямо сейчас дали бы такой выбор, я бы не знал, что ответить."
    play sound kurit
    th "С одной стороны в прошлом лагере, я точно не хотел бы остаться."
    th "А с другой...{w} Со всей этой чертовщиной..."
    th "Вдруг как мы выйдем со столовой, начнётся игра на выживание с убийцей Слави."
    th "Или с вот этими сверчками."
    "..."
    play sound kurit
    th "И что это, всё-таки, за стрекотание было?"
    th "..."
    th "Вообще ноль идей..."
    "..."
    stop music fadeout 3
    $ save_name = ('День 3. Не-Ульяна...')
    play sound sfx_bush_leaves
    "И вдруг не с того, не с всего, опять раздался шорох из кустов."
    th "Да ёпт...{w} опять?"
    th "..."
    "Из кустов ожидаемо никто не вышел."
    th "Проверю тогда, не хватало ещё чтобы какая-то хрень неизведанная по кустам пряталась."
    scene bg ext_dining_hall_near_sunset with dissolve
    "Как только я пошёл на встречу этому звуку, он снова повторился."
    play sound sfx_bush_leaves
    th "В этот раз не уйдёшь!"
    "Сделав ещё пару шагов..."
    play music fearmusic_4 fadein 2
    scene cg epilogue_mi_3 with dissolve
    "Оттуда всё таки вылезла \"какая-то хрень неизведанная\"."
    "От вида этого...{w} существа, отдалённо похожего на Ульянку, из моего рта выпала сигарета."
    us "Семён...{w} как...{w} твои...{w} дела?.."
    me "Пару секунд назад было не так уж и плохо..."
    "Мы просто стояли и смотрели друг на друга, я был в таком шоке, что даже не передать."
    th "Ладно, там лагеря цикличные, но ходячие мертвецы..."
    "..."
    el "Эй! Ты чего так долго?"
    "Услышав Электроника я обернулся."
    scene bg ext_dining_hall_near_sunset 
    show el normal pioneer far
    with dissolve
    me "Там...{w} это..."
    me "Посмотри туда..."
    el "Куда?"
    "Электроник сразу же начал оглядываться."
    el "Семён, да что не так-то?"
    me "Ты не видишь?"
    el "Да что я должен видеть?!"
    "Я обернулся назад, но на месте где была Зомби-Ульяна уже никого не было."
    hide el with dissolve
    th "Ага."
    th "..."
    th "Теперь тут два варианта:{w} Либо я окончательно тронулся умом, либо...{w} либо что?{w} Либо галлюцинации меня настигают..."
    th "И Мику тоже?{w} Одинаковые?"
    th "Либо это действительно не померещилось и сейчас где-то по лагерю ходит ходячий мертвец."
    show el surprise pioneer far with dissolve
    me "Забей..."
    stop music fadeout 3
    el "Ладно."
    "Все уже закончили свои дела в столовой, а потому, мы направились на площадь."
    $ save_name = ('День 3. Затишье.')
    play ambience ambience_camp_center_evening fadein 2
    scene bg ext_square_sunset
    show un normal pioneer at fleft
    with dissolve
    un "И куда теперь?"
    show mi sad pioneer at cleft with dissolve
    mi "Я бы поспала немного после всей этой чертовщины."
    me "Пошли тогда."
    play ambience ambience_int_cabin_evening fadein 2
    scene bg int_house_of_mt_sunset with dissolve
    me "Алис подежуришь?"
    show dv sad pioneer with dspr
    dv "Да..."
    hide mi
    hide un
    hide el
    with dissolve
    "Мику легла рядом со мной, Лена на соседнюю кровать, а Эл решил, что пока не хочет спать."
    me "Алис, разбудишь меня вечером или если что-то произойдёт, хорошо?"
    show dv normal pioneer with dspr
    dv "Конечно."
    "Алиса очень нежно прошептала свою фразу."
    hide dv with dissolve
    me "Спасибо."
    "Я закрыл глаза и сразу же погрузился в сон."

    if dv2_ochki >= 2:
        jump somesing_new_dvache_d4
    else:
        jump somesing_new_odinochka1


label somesing_new_dvache_d4:
    stop ambience fadeout 2
    show blink
    window hide dissolve
    pause 1.7
    $ backdrop = "night"
    $ new_chapter(4, "День 4. Карты расскрыты.")
    $ renpy.pause(1, hard=True)
    $ volume(1.0, "music")    
    $ backdrop = "night"
    $ night_time()    
    $ persistent.sprite_time = "night"
    $ renpy.pause(1, hard=True)
    play ambience ambience_int_cabin_night fadein 2
    scene bg int_house_of_mt_night2 
    play sound krik_uzhasa
    show unblink
    window show dissolve
    "Меня разбудил крик с улицы."
    play music hell fadein 4
    "Резко вскочив с кровати я осмотрел кровати и шезлонг."
    "На них лежали только Мику и Электроник."
    th "Твою мать!"
    "В ту же секунду я пулей вылетел из домика..."
    stop ambience fadeout 2
    play sound sfx_open_door_kick 
    scene bg ext_house_of_mt_night_without_light with dissolve
    "И просто замер в шоке."
    scene cg Ubivasha_noch_alisa_kill with dissolve
    "На улице я лицезрел как Алиса в ужасе отползает от Лены, а та подходит к ней с веревкой в руках, явно не с добрыми намерениями."
    th "Не каждый же день такое увидишь..."
    un "Упс!{w} Нас заметили!{w} Что же нам делать Алиса?"
    menu:
        "Разбудить всех":
            $ alisagood_ochki += 2
            $ alisabad_ochki -= 2
        "Без раздумий кинуться спасти Алису":
            $ alisabad_ochki += 2
            $ alisagood_ochki -= 2

    if alisagood_ochki >= 2:
        jump somesing_new_good_dvend
    else:
        jump somesing_new_bad_dvend



label somesing_new_bad_dvend:
    th "Что ты стоишь дурак?{w} Она её в любой момент может убить!"


label somesing_new_good_dvend:
    th "Не надо действовать на эмоциях, мало ли к чему это может привести."
    th "Например я кинусь на неё, а она меня этой верёвкой задушит."
    me "Лена, зачем ты это делаешь?"
    un "А как ты думаешь?"
    me "Не знаю я!{w} Отпусти её, она ни в чём не виновата!"
    un "Да-а-а-а?..{w} Ошибаешься, милый.{w} Моему счётчику грехов ДваЧе уже идти некуда - место закончилось."
    me "Она не та, о ком ты думаешь!"
    un "Да плевать мне!{w} Я хочу её убить и это главное моё желание сейчас!"
    th "Нет...{w} Так с ней не договориться, надо будить всех, вместе мы сможем её заломить."
    th "Наверное..."
    th "Но нужно действовать как можно быстрее, сейчас каждая секунда на вес золота."
    th "Тогда... {w} Сейчас!"
    scene bg int_house_of_mt_night2 with dissolve
    play sound sfx_open_door_strong 
    me "РОТА ПОДЪЁМ!!!" with hpunch
    show el surprise pioneer
    show mi scared pioneer at fright
    with dspr
    "Спящие пионеры тут же вскочили."
    el "Что такое?"
    me "На улицу! Бегом и без вопросов!" with vpunch
    scene bg ext_house_of_mt_night_without_light with dissolve
    "Но когда мы вышли на улицу, ни Алисы, ни Лены там уже не было."
    show el angry pioneer with dissolve 
    el "И зачем ты нас разбудил?"
    show mi dontlike pioneer at left with dissolve 
    mi "Да, знаешь ли, плохая выдалась шутка."
    me "Да какая к херам шутка?!" with vpunch
    show mi scared pioneer
    show el scared pioneer
    with dspr
    me "Где по-вашему Алиса и Лена?"
    show el surprise pioneer with dspr
    el "И вправду..."
    mi "Что с ними?.."
    me "Только что я услышал как кто-то кричал на улице, сразу же выбежал и увидел как Лена подходит с верёвкой к Алисе, которая, от неё в ужасе отползала."
    show el scared pioneer with dspr
    el "Тогда где они?"
    me "Мне откуда знать?{w} Я как только это увидел, сразу же забежал к вам."
    show mi sad pioneer with dspr
    mi "Тогда надо быстрее искать их пока, пока..."
    me "Да!{w} Поэтому вы идите к домику Лены, а я...{w} не знаю, куда-нибудь к столовой!{w} Куда угодно!"
    el "Хорошо."
    "Электроник и Мику, более не о чём не спрашивая, побежали к домику Лены."
    scene bg int_house_of_mt_night2 with dissolve
    "А я забежал в домик за той монтировкой, которую мы взяли с Алисой, когда осматривали лагерь на наличие людей."
    th "Где же, где же..."
    "..."
    me "Вот оно!"
    stop music fadeout 2
    "Более не задерживаясь я, чуть ли не выбив дверь, рванул из домика."
    $ save_name = ('День 4. Только бы успеть...')
    play sound sfx_open_door_kick 
    play music run fadein 2
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "..."
    "..."
    th "И куда мне бежать?!"
    th "Чёрт, чёрт, чёрт!"
    th "Вообще ничего в голову не лезет!{w} Я же наизусть всё должен знать!"
    th "..."
    th "Библиотека!"
    th "Точно!{w} Там тихое и далёкое место, да и к тому же неподалёку."
    "..."
    scene bg ext_library_night with dissolve
    "Подбежав к библиотеке, там и вправду нашлись Алиса и..." 
    show un evilsmile2 pioneer far at cleft
    show dv cry2 pioneer far at fleft
    with dissolve
    th "Лена?{w} Не думаю...{w} Надо ей прозвище какое-то придумать."
    th "Убиваша, например."
    th "Тьфу!{w} О чём я думаю!"
    "Более не медля, я кинулся со своей фомкой на Лену."
    hide dv with dspr
    show un evilsmile2 pioneer with dspr 
    me "Получай, сука!"
    show un ubv_surprise pioneer close with dspr
    play sound sfx_punch_washstand
    hide un with dspr
    "И со всей силы ударил её по голове."
    show dv cry2 pioneer with dissolve
    me "Живая?"
    dv "..."
    dv "Д-да..."
    me "Тогда быстрее побежали к остальным!"
    show dv sad pioneer with dspr
    dv "А-ага..."
    "Взяв Алису за руку, мы побежали."
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "..."
    dv "А г-где ост-тальные?"
    me "У домика Мику."
    dv "Я-ясно."
    "..."
    scene bg ext_house_of_un_night with dissolve
    stop music fadeout 3
    $ save_name = ('День 4. Живая!')
    "На адреналине мы прибежали очень быстро."
    play ambience ambience_camp_center_night fadein 2
    show el surprise pioneer far at fright
    show mi serious pioneer far at cright
    show dv sad pioneer at cleft 
    with dissolve
    el "Семён, что слу..."
    show mi cry_smile pioneer at center with dspr
    mi "Алиса!"
    "Мику кинулась обнимать пострадавшую."
    mi "Алиса, я... я так переживала...{w} Слава богу всё обошлось."
    show dv shy pioneer with dspr
    dv "Спасибо...{w} Мику..."
    show el scared pioneer at fright with dspr
    el "Это конечно всё хорошо, но что с Леной?"
    show dv sad pioneer with dspr
    me "Я её вырубил."
    show mi shocked pioneer at cright 
    show el normal pioneer 
    with dspr
    el "Хорошо, но тогда надо её связать чтобы такого больше не было."
    show mi shocked pioneer at cright with dspr
    mi "Идёмте тогда быстрее."
    me "Это не обязательно, я хорошо её приложил, можно не спешить."
    el "Извини за вопрос, но, ты не высокого мнения о себе?"
    me "Так я ж не с хука её вырубил."
    show el surprise pioneer with dspr
    el "А как?"
    me "Монтировкой."
    el "Даже спрашивать не буду..."
    show mi normal pioneer with dspr
    mi "Ладно, пошлите уже."
    scene bg black with dissolve
    window hide dissolve
    pause 3.0
    scene bg ext_library_night with dissolve
    window show dissolve
    $ save_name = ('День 4. Сюрприз.')
    "Когда мы вернулись к библиотеке наш ждал сюрприз."
    play music creepy fadein 4
    show el surprise pioneer at left
    show mi serious pioneer 
    show dv scared pioneer at right
    with dissolve
    el "И где?"
    dv "Он-на... она б-была тут."
    me "Прямо на этом месте..."
    show el angry pioneer with dspr
    el "Ты же говорил, что хорошо её приложил!"
    me "Простите...{w} Но всё равно!{w} Как она могла от такого сильного удара по башке, так быстро очухаться?"
    el "Значит не такой уж и сильный удар был!"
    me "Алиса."
    show dv shocked pioneer with dspr
    dv "Д-да?"
    me "Скажи, я сильно ударил Лену по голове?"
    dv "Д-довольно сильно, да."
    me "Могла ли она так быстро очухаться?"
    dv "Я биологию прогуливала, откуда мне знать?"
    me "А я вот, читал книги по анатомии. Не могла она за 20 минут, от удара куском железа по голове очнуться...{w} так быстро в себя не приходят!"
    el "Но пришла же!"
    show mi sad pioneer with dspr
    mi "М-мальчики, не с-сортись, п-пожалуйста."
    "Мику уже готова была разрыдаться, если мы не остановимся."
    me "Да, пожалуй...{w} У нас сейчас по лагерю бродит сошедшая с ума пионерка-маньячка, а мы тут разорались."
    el "Да ты понимаешь, что из-за твоего \"Можем не спешить, я её хорошо приложил\", мы её упустили!"
    me "Да, но кто ж зна..."
    "Электроник ещё строже посмотрел на меня."
    me "Простите..."
    el "Так и быть, но ты сильно провинился!"
    mi "Электроник, не забывай, что только из-за него Алиса сейчас живая."
    show el sad pioneer with dspr
    el "Э-э-э...{w} ну...{w} да..."
    show dv dontlike pioneer with dspr
    dv "Это правда, извинись перед Семёном, ты в отличии от него, даже не проснулся."
    el "Ну...{w} ладно, да...{w} прости, Семён...{w} я всё-таки не пример подражания. Но ты тоже виноват."
    me "Каюсь..."
    "..."
    show mi normal pioneer 
    show dv sad pioneer 
    with dspr
    dv "М-может пойдём спать?"
    me "И куда же?"
    dv "Я не знаю... но я очень хочу спать... я ведь не спала ещё, всю ночь дежурила..."
    me "А почему ты меня не разбудила, как я просил?"
    dv "Я...{w} забыла...{w} прости..."
    me "Проехали..."
    show mi serious pioneer with dspr
    mi "Мы можем в моём клубе поспать."
    show el surprise pioneer with dspr
    el "Мысль хорошая, только вот, мы на полу спать будем?"
    show mi upset pioneer with dspr 
    mi "Ну почему же..."
    show mi normal pioneer with dspr 
    mi "Мы можем из кладовки в моём клубе достать матрасы и на них спать, только вот их там много, нам все доставать прийдётся скорее всего, хотя можно и не все, но лучше все, они там просто завалены, до них добраться, тоже работа не лёгкая..."
    show el normal pioneer with dspr
    me "Мику, если честно, я ничего не понял, но поступим так, как ты скажешь."
    show mi smile pioneer with dspr
    mi "Хорошо-хорошо."
    dv "Т-только вот...{w} по какому пути пойдём?{w} Ведь где-то в лагере сейчас ходит...{w} эта тварь...{w} И кто знает, что ей на ум прейдёт."
    dv "Вдруг она высочит на нас с топором посреди дороги..."
    me "Точно...{w} Тогда давайте через лес пойдём."
    show mi scared pioneer with dspr
    mi "А мы не заблудимся?"
    me "Не бойтесь, я знаю этот лес как свои пять пальцев."
    el "Ты так же про Лену говорил..."
    "Я грозно посмотрел в сторону Электроника."
    show el scared pioneer with dspr
    "Он сразу же забыл свою придирку."
    show dv normal pioneer 
    show mi serious pioneer 
    show el normal pioneer 
    with dspr
    stop music fadeout 4
    "Мы ещё немного обсудили план действий в случае если встретим Лену-убивашу и двинулись к клубу Мику."
    scene bg black with dissolve
    window hide dissolve 
    $ renpy.pause(1.7, hard = True)
    scene bg ext_musclub_night with dissolve
    $ save_name = ('День 4. Ночь в клубу Мику.')
    window show dissolve
    "  "
    scene bg ext_near_musclub_night with dissolve
    "Прибывши к муз. клубу, Мику вспомнила, что у неё нет с собой ключей."
    show mi upset pioneer 
    show el normal pioneer at right
    show dv sad pioneer at left
    with dissolve
    mi "Блин..."
    me "Что такое?"
    show mi sad pioneer with dspr
    mi "Я ключи не брала..."
    me "Плохо...{w} А может ты забыла закрыть?"
    mi "Может...{w} Сейчас проверю."
    play sound sfx_open_door_1 
    show mi smile pioneer with dspr
    mi "Открыто!"
    me "Отлично."
    scene bg int_musclub_night with dissolve
    play ambience ambience_music_club_night fadein 3
    "..."
    show mi smile pioneer with dspr
    mi "Ну,{w} за работу."
    scene bg black with dissolve
    "Мы с Электроником, под руководством Мику, быстро достали все матрасы из кладовки."
    scene bg int_musclub_night_with_matras with dissolve
    show mi normal pioneer 
    show dv sadness pioneer at cleft 
    show el sad pioneer at right
    with dissolve
    dv "А кто дежурить будет?"
    me "Давайте так: Сперва я дежурю часа два, потом Мику, мы с ней больше всего спали, а после Мику Эл, дальше уже день будет."
    mi "Я согласна."
    el "Да, давайте так."
    me "Тогда спокойной ночи всем."
    hide dv
    hide mi 
    hide el
    with dissolve
    "Все пожелали мне того же и завалились спать."
    th "Ну, а мне ещё часа два предстоит пробыть наедине со своими мыслями."
    "..."
    th "Теперь можно подумать, что вообще только что произошло."
    th "Я проснулся от крика, выйдя на улицу, я застал Лену за убийством Алисы."
    th "Сразу же разбудил всех и вывел на улицу, но там уже не было ни Лены, ни Алисы."
    th "Дальше я побежал к библиотеке и не прогадал, вырубил Лену, забрал Алису и мы побежали обратно к Мику и Элу."
    th "Когда мы нашли их, мы решили вернуться к Лене."
    th "Но когда мы вернулись её уже небыло."
    th "Потом мы пришли сюда..."
    th "..."
    th "Во всей этой истории три несостыковки:"
    th "Первая - это сам факт того, что Лена сошла с ума."
    th "Почему?{w} Спишем на то, что в этот цикл всё по-другому."
    th "Вторая несостыковка - заключается в том, что я забежал в домик буквально на пару секунд, а когда мы вышли никого уже не было."
    th "Выходит, что Лена как-то схватила Алису и убежала."
    th "Предположим, что так и было, но вопрос как у неё хватило на это сил, остаёться открытым."
    th "Хотя есть ещё вариант, что она взяла Алису за руку, а она в шоковом состоянии не смогла сопротивляться."
    th "..."
    th "Да, остановимся на этом варианте."
    th "..."
    th "И самая главная, третья несостыковка - это то, почему Лена так быстро пришла в сознание.{w} От удара такой силы, можно было и кони двинуть, а она сама пришла в себя, так ещё и за 20 минут."
    th "..."
    th "На это счёт у меня даже предположений нету..."
    th "..."
    th "А!{w} Ещё же вчерашняя мистика есть..."
    th "Зомби-Ульяна и сверчки..."
    th "Со сверчками вообще ничего не ясно..."
    th "А зомби..."
    th "Галюцинация это была или всё же нет?"
    th "..."
    th "С одной стороны, Электроник её не успел заметить."
    th "А с другой...{w} А с другой её видела Мику."
    th "Правда в тот раз её не видел я..."
    th "..."
    th "Тьфу!{w} Совсем запутался!"
    th "Ладно, сейчас это на втором плане, по крайней мере пока что..."
    "..."
    "..."
    "Спустя около двух часов моих раздумий над этим всем, я разбудил Мику."
    show mi happy pioneer close with dissolve
    me "Мику...{w} Вставай!{w} Дежурить пора."
    mi "Мням..."
    th "Её кошмары точно не мучают..."
    me "Мику!"
    show mi scared pioneer close with dspr
    mi "А?{w} Что?{w} Что такое?"
    me "Дежурить вставай.{w} Я спать хочу."
    show mi sad pioneer close with dspr
    mi "А, да, хорошо сейчас встану."
    me "Спокойного дежурства."
    show mi normal pioneer with dspr 
    mi "Спокойной ночи."
    "Мику встала, а я лёг на её место."
    stop ambience fadeout 5
    hide mi with dissolve
    th "Надеюсь, сейчас высплюсь..."
    show blink
    window hide dissolve
    $ renpy.pause(4.5, hard = True)
    $ save_name = ('День 4. Опять?')
    play sound krik_uzhasa
    hide blink 
    show unblink
    window show dissolve
    play music Hunx fadein 7
    "И снова я проснулся от крика с улицы."
    th "Ага, выспаться он захотел..."
    "Через две секунды я вылетел на улицу."
    play sound sfx_open_door_strong 
    scene bg ext_musclub_night with dspr
    "Там я увидел то, что никак не ожидал увидеть."
    play sound sfx_hell_crickets_2 loop fadein 2
    $ save_name = ('День 4. Опять...')
    scene cg ulz_1 with dissolve
    "Ульяну..."
    scene cg ulz_2 with dspr
    "Ульяну-зомби..."
    "Она посмотрела в мою сторону..."
    "А я просто уставился на неё."
    "..."
    th "Соберись, тряпка!"
    stop sound 
    play sound sfx_face_slap 
    pause 0.65
    play sound sfx_hell_crickets_2 loop fadein 0.3
    "Дав себе пощёчину я влетел в зомби с ноги."
    me "За Сталина, сука!"
    stop sound fadeout 1
    play sound sfx_lena_hits_alisa 
    scene bg ext_musclub_night with dspr
    "Пока оно валялось, Мику подбежала ко мне."
    show mi shocked pioneer with dissolve
    me "В клуб, быстро!"
    mi "А ты?"
    me "Я тоже!{w} Побежали!"
    scene bg ext_near_musclub_night with dissolve
    pause 0.25
    play sound sfx_close_door_1  
    scene bg int_musclub_night_with_matras with dspr
    $ save_name = ('День 4. Не показалось...')
    me "Фух..."
    show mi cry pioneer with dissolve
    play sound soul_cry
    mi "В-всё таки... м-мне не п-показалось..."
    me "Да..."
    "..."
    mi "Боже...{w} сколько это будет ещё продолжаться!?..."
    play sound soul_cry
    mi "Почему?{w} Почему именно я?!{w} Чем я так согрешила?.."
    me "..."
    "Мне было нечего сказать."
    th "В отличии от неё, я догадываюсь чем я согрешил..."
    me "Мы сделаем всё, чтобы выбраться."
    show mi sad pioneer with dspr
    mi "Сделаем-то, но выберемся ли?"
    me "Не знаю..."
    mi "И я..."
    "..."
    mi "Кстати опять был этот стрёкот..."
    me "Хм, и правда..."
    mi "Выходит, что он исходит от этой..{w} Ульяны?"
    me "Скорее всего."
    mi "То есть...{w} Уже в админ корпусе?.."
    me "Да, тем более ты ещё и увидела её потом."
    stop music fadeout 6
    mi "Так что нам делать?{w} Оно вроде не идёт сюда."
    me "Точно не спать."
    mi "Это понятно...{w} но чем заняться?"
    me "Не знаю..."
    mi "Может Электроника разбудить?"
    me "А сколько времени?"
    mi "Сейчас..."
    "Мику посмотрела на часы."
    mi "3:50"
    me "Думаю можно{w}, даже нужно."
    play ambience ambience_music_club_night fadein 3
    hide mi with dissolve
    me "Проснись и пой!"
    show el surprise pioneer with dissolve
    el "Что такое?"
    me "У нас ЧП."
    el "Что случилось?"
    me "Зомби-Ульяна...{w} не показалась..."
    show el scared pioneer with dspr
    el "..."
    el "И что делать?"
    me "Вот, думаем."
    el "И что придумали?"
    me "Ничего."  
    hide el with dspr
    show mi sad pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    "Электроник встал с матраса и присоединился к нашим раздумиям."
    me "У кого-нибудь есть идеи?"
    mi "..."
    el "..."
    me "Тогда слушайте."
    show mi surprise pioneer at cleft
    show el surprise pioneer at cright
    with dspr
    me "Сейчас в лагере не безопасно."
    "Все кивнули."
    me "Поэтому лучше уйти из лагеря."
    el "И как ты собрался реализовать это? Отсюда до Райцентра...{w} далеко!"
    me "Нет-нет, ты что...{w} конечно бессмыслено идти туда пешком..."
    mi "Тогда, что ты хочешь сделать."
    me "Пойдём в бункер в старом лагере."
    show mi shocked pioneer with dspr
    el "Идея недурная...{w} а план какой?"
    me "Вот над этим надо подумать..."
    "..."
    show el normal pioneer with dspr
    el "Думаю нужно взять вещи первой необходимости."
    me "Да, но где?"
    el "Можно в клубах.{w} Они ближе всего."
    me "Хорошо..."
    el "А насчёт остального плана: Мику останется с Алисой, мы пойдём в клубы, возьмём необходимое, вернёмся за девочками и пойдём в этот бункер."
    me "Пойдёт{w}, сделаем так."
    el "Когда пойдём?"
    me "Давай сейчас.{w} Зачем медлить?"
    el "Незачем, идём."
    mi "А если Ульяна ещё за дверью?"
    me "Если она ещё там, мы сразу зайдём назад."
    show mi sad pioneer with dspr
    mi "Ладно, удачи вам, возвращайтесь по быстрее..."
    el "Конечно."
    me "Постараемся."
    "..."
    play sound sfx_close_door_1  
    play ambience ambience_camp_center_night fadein 2
    scene bg ext_near_musclub_night with dissolve
    pause 1.3
    show el smile pioneer with dissolve
    play music napryagis2 fadein 6
    el "Хух...{w} Как на войну отправляемся."
    me "Кто знает..."
    show el normal pioneer with dissolve
    me "Кстати...{w} что у вас там из необходимого?"
    show bg ext_musclub_night with dissolve
    el "Ну, там есть набор для похода, его и возьмём."
    me "Там прям всё-всё есть?"
    el "Думаю, больше чем то, что в нём лежит, нам не понадобится.{w} Разве что аптечка."
    me "Насчёт этого не беспокойся, в бункере она имеется."
    el "А ты откуда знаешь?"
    me "Главное, что знаю."
    el "Давай чтобы не как с Ле..."
    me "Да что ты заладил с этой Леной!{w} Всегда теперь мне будешь вспоминать её?" with vpunch
    show el sad pioneer with dspr
    el "..."
    el "Нет."
    me "Ну вот и всё."
    "Дальше, до клубов мы шли молча."
    "..."
    scene bg ext_clubs_night with dissolve
    pause 1.0
    show el smile pioneer with dissolve 
    el "Тут постоишь или поможешь мне в поисках?"
    me "Тут подожду."
    show el sad pioneer with dspr 
    "Электроник совсем не ожидал такого ответа и расстроился."
    me "Да ладно-ладно помогу я тебе."
    show el normal pioneer with dspr
    el "Ага."
    play sound sfx_open_door_clubs 
    play ambience ambience_int_cabin_night fadein 2
    scene bg int_clubs_male_night_light  with dissolve 
    pause 1.0
    show el normal pioneer with dissolve
    el "Я поищу в кладовой, а ты тут, возможно Шурик доставал его, он хотел пойти кое-куда за деталями."
    th "Знаем не понаслышке.{w} И знаем, что Шурик ничего не доставал."
    th "Поэтому, вместо поисков, можно посвятить время праздости."
    play sound sfx_open_door_clubs_nextroom
    hide el with dissolve
    scene bg black with dissolve 
    $ renpy.pause (2.0, hard = True)
    scene bg int_clubs_male_night_light with dissolve 
    pause 1.0
    "Через пару минут Электроник вышел с какой-то сумкой."
    play sound sfx_open_door_clubs_nextroom
    show el smile pioneer with dissolve
    el "Нашёл!"
    me "Вот и славно, возвращаемся."
    play sound sfx_open_door_clubs
    scene bg ext_clubs_night with dissolve
    play ambience ambience_camp_center_night 
    "Мы уже соберались идти, но вдруг...{w} откуда-то раздался скрип."
    play sound sfx_carousel_squeak 
    show el surprise pioneer with dissolve
    el "Ты слышал?"
    me "Похоже, что это ворота."
    show el scared pioneer with dspr
    el "А если там Лена?"
    me "Принеси из клубов что-то похожее на оружие."
    el "Ты хочешь проверить?.."
    me "Да."
    el "Сейчас принесу."
    play sound sfx_open_door_clubs
    hide el with dissolve
    th "Мда...{w} Говорят, что женщины живут дольше мужчин...{w} Теперь я, кажеться, понимаю почему."
    th "Мы в лагере вместе с зомби и маньячкой, поэтому, конечно же стоит пойти на скрип ворот посреди ночи!"
    th "Хорошо, что я хоть догадался оружие взять."
    play sound sfx_open_door_clubs
    show el normal pioneer with dissolve
    el "Это самое нормальное, из того что было..."
    "В руках Электроника была бита и арматура."
    "Биту он протянул мне."
    me "Сойдёт.{w} Потопали давай."
    show el scared pioneer with dspr
    el "Может всё-таки не пойдём?"
    th "Здравый смысл говорит мне поддержать Электроника, но интерес выигрывает у страха."
    me "Раз решили идти, то идём.{w} К тому же, мы вооружены."
    el "Л-ладно..."
    stop music fadeout 2
    scene bg ext_no_bus_night with dissolve 
    show el normal pioneer with dissolve
    el "Вроде бы никого...{w} Наверное это ветер..."
    "Я уже хотел было согласиться, но внезапно Эл заметил что-то вдали."
    show el surprise pioneer with dspr
    el "Смотри!"
    me "Что? Куда?"
    show el smile pioneer with dspr
    el "Автобус! Там!"
    stop ambience fadeout 8
    play sound sfx_hell_crickets_3 loop fadein 13
    "Как только я посмотрел в ту сторону, от \"Автобуса\" начал исходить такое же стрекотание как и от зомби несколько минут назад."
    th "Если, действительно от зомби исходит этот звук, то выходит, что это..."
    show el shocked pioneer with dspr
    play music grind fadein 8.5
    el "Это не похоже на автобус."
    th "Это толпа зомби!?"
    scene cg epilogue_mi_5 with dissolve
    "Буквальвально через 10 секунд уже можно было различить этих тварей."
    us "Семён..."
    us "Электроник..."
    us "Как...{w} ваши...{w} дела?.."
    el "Эт-то..."
    scene bg ext_camp_entrance_night
    show el shocked pioneer 
    with dspr
    me "Валим! Скорее!" with vpunch
    "Электроник никак не отреагировал."
    me "Серёга!"
    el "Эт-т{w}-т-т..."
    "Больше не было времени, чтобы приводить Эла в себя, поэтому я просто бросил биту, взял его за руку и побежал."
    scene bg ext_clubs_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    th "Сколько ещё можно!"
    th "Какая к чёрту толпа Ульян?!{w} Это вообще как?"
    stop sound fadeout 5
    scene bg ext_musclub_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    th "Как от них спасться?"
    th "Ну прибежим мы назад, а дальше что?"
    th "Дверь эту толпу не выдержит."
    scene bg ext_near_musclub_night with dspr
    "..."
    play sound sfx_open_door_kick 
    scene bg int_musclub_night_with_matras 
    show mi scared pioneer 
    with dspr 
    mi "Что такое?!"
    me "Бежим!"
    mi "Почему?!"
    me "Ульяны!"
    mi "Ульян{b}ы{/b}?"
    me "Да!{w} Скорее!"
    scene bg ext_near_musclub_night with dspr 
    "Я с Электроником, более не секунду не задерживаясь выбежали на улицу."
    show mi scared pioneer with dspr 
    mi "Куда?"
    me "В старый корпус!"
    scene bg ext_musclub_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (50,50)
        ease 0.20pos (0, 0)
        ease 0.20pos (-50,50)
        repeat
    "Через мгновение мы уже рванули с места."
    th "Главное по пути на них не наткнуться, оружия-то больше нет..."
    "..."
    $ renpy.pause (3.0, hard=True)
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (55,55)
        ease 0.20pos (0, 0)
        ease 0.20pos (-55,55)
        repeat
    $ renpy.pause (3.0, hard=True)
    scene bg ext_square_night with dissolve
    "Когда все выбежали на площадь, я вспомнил!"
    show mi scared pioneer with dspr
    me "Блять!" with vpunch
    mi "Что?"
    me "Алиса!" with hpunch
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (55,55)
        ease 0.20pos (0, 0)
        ease 0.20pos (-55,55)
        repeat
    th "Как я мог забыть о ней?!"
    th "Я же ей обещал..."
    th "Как? как, чёрт возьми, я забыл?"
    play sound sfx_hell_crickets_3 loop fadein 3
    "Возле общих кружков уже были эти твари-Ульяны."
    scene bg ext_musclub_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (65,65)
        ease 0.20pos (0, 0)
        ease 0.20pos (-65,65)
        repeat
    th "Слава богу они ещё не добрались..."
    th "Только вот, это не значит, что я успею."
    "На финишной прямой я побежал ещё быстрее, хотя мне казалась, что это было невозможно."
    scene bg ext_near_musclub_night with dspr
    pause 0.2
    play sound sfx_open_door_kick
    scene bg int_musclub_night_with_matras with dspr
    me "АЛИСА!!!" with hpunch
    show dv scared pioneer with dspr
    "Алиса аж подпрыгнула от такого крика."
    dv "Что случилось?{w} Где все?!"
    me "Бежим! Через окно!"
    hide dv with dissolve
    "Алиса, ничего не спрашивая выскочила в открытое окно."
    scene bg ext_path_night with dissolve
    play sound sfx_boat_impact 
    "И я за ней."
    show dv shocked pioneer with dissolve
    dv "И к-куда?"
    me "На площадь, живо!" 
    scene bg ext_path_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (60,60)
        ease 0.20pos (0, 0)
        ease 0.20pos (-60,60)
        repeat
    $ renpy.pause (3.0, hard = True)
    th "Я же ещё и ничего не сказал Мику и Элу!"
    th "И где нам их искать?"
    th "..."
    scene bg ext_path2_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (60,60)
        ease 0.20pos (0, 0)
        ease 0.20pos (-60,60)
        repeat
    th "Надеюсь они пойдут в старый лагерь."
    $ renpy.pause (3.0, hard = True)
    "..."
    scene bg ext_square_night with dissolve 
    stop music fadeout 4
    play ambience ambience_camp_center_night fadein 3
    "В скором времени я с Алисой выбежал на площадь."
    "Ребят, разумееться, тут уже не было."
    show dv scared pioneer with dissolve
    play music Frightening_Unknown fadein 14
    dv "А где?.."
    me "Остальные?"
    "Алиса кивнула."
    me "Вероятно, решили, что оставаться в центре лагеря, где бродят зомби-Ульяны и сумасшедшая пионерка-убийца - не лучшая идея."
    show dv shocked pioneer with dspr
    dv "Л-логично..."
    me "Поэтому идём в старый корпус, возможно, там удасться пересечься."
    dv "А з-зачем нам туда?.."
    me "Мы решили, что в лагере оставаться больше нельзя."
    dv "Почему именно туда?"
    me "Поменьше вопросов, леди.{w} С минуты на минуту эта орда может прийти сюда."
    dv "Л-ладно..."
    "Стараясь идти как можно тише, мы отправились в путь."
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (15,15)
        ease 0.20pos (0, 0)
        ease 0.20pos (-15,15)
        repeat
    "Шли молча. Старались вообще не издавать звуков."
    $ renpy.pause (4.0, hard = True)
    scene bg ext_house_of_dv_night with dissolve
    "Но возле своего домика, Алиса всё же прервала тишину."
    show dv sad pioneer with dissolve
    dv "М-может возьмём что-нибудь?"
    me "Не стоит, самое необходимое у них есть."
    play sound sfx_bush_leaves 
    show dv scared pioneer with dspr
    dv "Ч-что это?"
    me "Шорох."
    show dv angry pioneer with dspr
    dv "Спасибо Кэп!"
    me "Давай лучше уйдём."
    th "По предыдущему опыту знаю, что на шорохи лучше не ходить..."
    show dv sad pioneer with dspr
    dv "Давай."
    scene bg ext_houses_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (15,15)
        ease 0.20pos (0, 0)
        ease 0.20pos (-15,15)
        repeat
    $ renpy.pause (3.0, hard = True)
    scene bg ext_path_night with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (15,15)
        ease 0.20pos (0, 0)
        ease 0.20pos (-15,15)
        repeat
    dv "А ты помнишь куда идти?"
    me "Наизусть."
    dv "Долго ещё?"
    me "Минут пятнадцать."
    $ renpy.pause (2.0, hard = True)
    scene bg ext_path2_night with dissolve2:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (15,15)
        ease 0.20pos (0, 0)
        ease 0.20pos (-15,15)
        repeat
    $ renpy.pause (3.0, hard = True)
    stop music fadeout 3
    scene bg ext_old_building_night with dissolve
    "..."
    me "Мы на месте."
    show dv scared pioneer with dissolve
    dv "Выглядит крипово..."
    me "В любом случае, тут безопаснее."
    show dv sad pioneer with dspr
    dv "Наверное..."
    scene bg int_old_building_night with dissolve
    play music staryy_dom fadein 8
    show dv sad pioneer close at fright with dissolve
    "Зайдя в здание, мы наткнулись на Электроника, который пытался открыть люк, и Мику, плачущую в углу."
    me "Салют всем нашим!"
    show el surprise pioneer far at fleft
    show mi cry pioneer at cleft 
    with dissolve
    mi "С-с-семён?"
    me "Собственной персоной.{w} С Алисой, кстати."
    show mi cry_smile pioneer close at cright with dspr
    "Мику кинулась обнимать нас."
    mi "Я... я думала ты...{w} вы не вернётесь..."
    me "Всё хорошо. Все живы-здоровы."
    mi "Как же я рада!"
    show el smile pioneer far with dspr
    el "Семён!{w} С возвращением!"
    show el normal pioneer far with dspr
    el "И спасибо...{w} за то, что не бросил меня на корм этим тварям."
    me "Пустяки.{w} Лучше скажи, что ты с этим люком возишься?"
    show el sad pioneer far with dspr
    el "Подойди сюда."
    hide mi
    hide dv 
    with dissolve
    show el sad pioneer at cleft with dissolve 
    el "Вот попробуй его открыть."
    "Я попробывал."
    play sound sfx_open_metal_hatch
    "И даже никак не хитря, у меня вышло."
    stop music fadeout 5
    show el surprise pioneer with dissolve 
    me "И что сложного?"
    el "Э-э-э...{w} как?"
    me "Взял люк и открыл. Или тебе нужна пошаговая инструкция?"
    show el scared pioneer with dissolve 
    el "Нет. Давай залезать лучше."
    me "Тогда доставай фонарик из своего набора \"юного путешественика по подземельям\"."
    show el normal pioneer with dissolve
    el "Хорошо."
    me "Девочки, харош обниматься!{w} Нам пора."
    scene bg int_catacombs_entrance with dissolve 
    play ambience ambience_catacombs fadein 2
    play music bitva fadein 12.5
    show el normal pioneer at left with dissolve
    show dv normal pioneer at right 
    show mi normal pioneer
    with dissolve
    el "А куда нам? Направо или налево?"
    me "За мной."
    show mi shocked pioneer with dspr
    mi "Ты тут ориентируешься?"
    me "Да."
    th "Прошу только не спрашивай откуда..."
    show mi smile pioneer with dspr
    mi "Здорово!"
    th "Спасибо.{w} Не хватало сейчас ещё перед ней объясняться..."
    scene bg int_catacombs_door with dissolve 
    show dv surprise pioneer at right with dspr
    dv "Вот он!"
    show el smile pioneer at left with dspr
    el "Мы спасены!"
    me "Рано раслабляться.{w} Когда уедем отсюда, тогда и можно радоваться."
    show el sad pioneer with dspr
    el "Момент бы хоть не портил..."
    "Не отреагировав на слова Эла, я принялся открывать дверь."
    play sound sfx_metal_door_handle_rattle
    pause 0.5
    play sound sfx_metal_door_handle_rattle
    pause 0.5
    play sound sfx_metal_door_handle_rattle
    "Однако дверь, в отличии отлюка, не подавалась."
    me "Да что ж такое..."
    show el scared pioneer with dspr
    el "Заело может..."
    me "Может..."
    dv "И что нам делать?"
    show mi dontlike pioneer with dspr
    play sound stuk_metal
    mi "Открой! Открой! Открой-Открой!"
    me "Мику успокойся, так делу не поможешь."
    show el normal pioneer with dspr
    el "Если в дверь стучать и просить её открыться, она не откроется."
    "Но внезапно произошло то, что никто не мог ожидать."
    sh "Твари! Уже сюда добрались!"
    show el surprise pioneer 
    show dv surprise pioneer
    show mi shocked pioneer
    with dspr
    "..."
    el "Шурик??!" with vpunch
    th "Это...{w} многое меняет."
    play sound stuk_metal
    show el smile pioneer with dspr
    el "Шурик!{w} Это я Электроник!{w} Твой лучший друг!"
    el "Помнишь мы ещё всё время в кружке проводили, робота строили..."
    sh "Серёжа?!"
    el "Да!"
    pause 1.0
    "Шурик сразу же кинулся открывать дверь."
    play sound sfx_open_metal_hatch
    scene bg int_catacombs_living with dissolve
    stop ambience fadeout 2
    $ persistent.sprite_time = "sunset"
    show el smile pioneer at left 
    show mi normal pioneer at cright
    show dv normal pioneer at fright
    with dissolve
    show sh surprise pioneer far with dissolve
    "Когда мы зашли, он на пару секунд растерялся."
    show sh smile pioneer at cleft with dspr
    "Но собравшись с мыслями он кинулся обнимать своего друга."
    sh "Слава богу..."
    el "А ты...{w} что тут делаешь?"
    show sh normal pioneer at center with dspr
    sh "Присаживайтесь. Cейчас всё вам расскажу."
    hide sh
    hide mi
    hide dv
    hide el
    with dissolve
    play sound sfx_bed_squeak1 
    show sh serious pioneer at right with dissolve
    sh "Позавчера я решил снова пойти за деталями, только в этот раз дойти."
    sh "После обеда пошёл."
    sh "Провозившись тут до вечера, решил, что пора назад."
    sh "Походя по лесу я услышал странные звуки..."
    show sh scared pioneer with dspr
    sh "Там я увидел этих тварей."
    me "Ульян?"
    sh "Да."
    sh "И я застал их за едой..."
    sh "Они ели Виолу..."
    mi "Т-то есть все пропали...{w} потому что их съели?.."
    show sh serious pioneer with dspr
    sh "Ну почему же..."
    sh "Может другие тоже прячуться как я."
    me "Сам-то в это веришь?"
    show sh upset pioneer with dspr
    sh "..."
    sh "Нет, пожалуй..."
    me "Ладно, что дальше было?"
    sh "Дальше они меня заметили, а я убежал обратно в бункер."
    me "То есть, на этом всё?"
    sh "Почти."
    "Вся компания вопросительно взглянула на Шурика."
    show sh smile pioneer with dspr
    sh "Я же просто так здесь штаны не просиживал."
    "..."
    show sh normal_smile pioneer with dspr
    sh "Я конструировал оружие против них!"
    show el surprise pioneer at fleft with dissolve
    el "И как?"
    sh "Оно в шкафчике."
    me "А что именно?"
    "Саня принялся доставать свои шедевры."
    show sh normal pioneer at fright with dspr
    sh "Так... смотри, тут пара гвоздомётных узи... арбалет... и... кучу холодного оружия. {w}Оно тут было."
    me "Ясно."
    sh "Арбалет стреляет камешками, а их в шахте полно."
    me "Это, конечно, уравнивает наши шансы, но вечно же мы не сможем от них отбиваться, а чтоб от всех избавиться этого не хватит."
    show sh normal pioneer at right with dissolve
    sh "Ты хочешь сказать, что нам нужен план?"
    me "В целом, да."
    sh "Вы же ещё помните что мы в пионерском лагере?"
    th "Такое не забудешь..."
    show mi shocked pioneer at cleft 
    show dv sad pioneer at left 
    with dissolve 
    dv "Нет."
    mi "И что это меняет?"
    show sh smile pioneer at right with dspr
    sh "Многое!"
    show sh normal pioneer with dspr
    sh "Вы в курсе, что сегодня поледний день смены?"
    th "Точно!{w} Мы же попали сюда на 5 день!"
    me "Автобус!"
    sh "Бинго!"
    sh "К обеду, через шахту, мы вылезем на площадь, если встретим Ульян, будем отбиваться от них, если нет, то дойдём до остановки к автобусу."
    show el surprise pioneer with dspr
    el "Ты откуда знаешь, что там есть выход?"
    sh "Излазил там всё за эти дни."
    show el normal pioneer with dspr
    el "Понял."
    dv "А если...{w} автобуса не будет?.."
    show sh serious pioneer with dspr
    sh "Вот если не будет, тогда и будем думать!"
    me "Звучит многообещающе, стоит попробывать."
    hide sh
    hide dv
    hide el 
    hide mi
    with dissolve
    stop music fadeout 1
    show un evilsmile2 pioneer with dissolve
    un "Это, конечно, интересный план, но вы не учли один момент."
    un "Меня."


label somesing_new_odinochka1:





